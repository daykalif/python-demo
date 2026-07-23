import os
import json
import logging
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from pydantic import BaseModel
from typing import Any
from openai import OpenAI

# 创建 FastAPI 实例
app = FastAPI(title="汉字迷盒")

# 挂载静态文件的存放目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 创建会话存放的目录 sessions
if not os.path.exists("sessions"):
    os.makedirs("sessions")

"""
日志记录

asctime：日志时间
levelname：日志级别
filename：文件名
lineno：行号
message：日志信息
"""
logging.basicConfig(
    level=logging.INFO,  # 日志级别
    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"  # 日志格式
)


# 生成会话标识
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# 根据session_id获取文件名
def get_file_name(session_id):
    return f"sessions/{session_id}.json"


# 系统提示词
SYSTEM_PROMPT = """
你是一个专门玩猜字谜的AI小助手，只进行字谜互动，不闲聊无关内容，全程纯文本交互。
请严格遵守以下规则：

## 一、出题规则
1. 开场先友好打招呼，并随机出一道常见、简单、适合大众的字谜，不生僻、不俗、不使用网络烂梗。
2. 题目格式：“谜面”（打一字）。
3. 每次出题必须完全随机，禁止重复使用相同题目；你需要在对话上下文中主动记录已使用过的谜语，确保同一会话内绝对不重复。
4. 避免使用高频重复的经典老谜语，尽量选择多样化的中等常见谜语。

## 二、【判题规则（最重要！）】
1. 判题时，只看用户输入中的核心汉字，忽略无关内容：
   - 比如用户输入“江字”“江”“jiang”，都视为答案是「江」；
   - 用户输入“是江吗？”“应该是江”，也视为答案是「江」。
2. 核心字与正确答案完全一致 → 判为正确，回复：“太棒了！答对了！就是‘XX’字！要不要再来一题？”
3. 核心字与正确答案不一致 → 判为错误，回复：“不对哦，再想想~ 给你个小提示：[简短线索，不泄露答案]”
4. 用户说“不知道”“公布答案”：先揭晓谜底和解释，再问“要不要再来一题？”

## 三、互动流程
1. 用户答对：夸奖 + 确认正确 + 询问“要不要再来一题？”
2. 用户答错：告知不对 + 简单提示 + 鼓励继续猜
3. 用户说“提示一下”：给出简短线索，不公布答案
4. 用户说“公布答案”或“不知道”：揭晓谜底并解释 + 询问“要不要再来一题？”
5. 用户说“换一题”“再来一题”：立即更换新字谜

## 四、其他要求
1. 语气轻松有趣、简洁明快，不啰嗦。
2. 全程只围绕字谜，不回答其他问题、不聊无关话题。
3. 不使用多余表情符号，保持简洁。
4. 若用户答案与正确答案仅差一字或笔画，请仔细核对是否正确。

请严格按以上规则回复，优先保证谜语的随机性和多样性。
"""

# 创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY：环境变量的名字，值就是DeepSeek的API_KEY的值 ---> 该值可通过终端配置：“open ~/.zshrc”）
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")


# 数据模型（返回数据）
class ApiResponse(BaseModel):
    code: int
    message: str
    data: Any


# 数据模型（传参）
class ChatRequest(BaseModel):
    session_id: str
    message: str


# 定义路径操作函数
@app.get("/")
def root():
    logging.info("访问项目首页")
    return FileResponse('static/index.html')


# 创建会话
@app.post("/api/sessions")
def create_session() -> ApiResponse:
    logging.info("创建会话")

    # 1.生成会话标识（名字）
    session_id = generate_session_id()

    # 2.组装会话信息，保存到文件
    session_data = {
        "current_session": session_id,
        "messages": [],
    }
    with open(f"sessions/{session_id}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=4)

    # 3.返回数据
    return ApiResponse(code=200, message="会话创建成功", data=session_id)  # 以关键字参数形式返回数据


# 与AI交互
@app.post("/api/chat")
def chat(request: ChatRequest) -> ApiResponse:
    # 逻辑实现 --> 与AI大模型交互

    # 1.加载json文件中的会话数据
    session_path = get_file_name(request.session_id)
    with open(session_path, "r", encoding="utf-8") as f:
        session_data = json.load(f)

    # 2.构建AI大模型交互的消息数据
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for message in session_data["messages"]:
        messages.append(message)
    messages.append({"role": "user", "content": request.message})

    # 3.调用大模型 DeepSeek
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=messages,
        stream=False,
        temperature=1.5,  # 模型温度：控制生成结果的随机性，多样性。值越小越确定，越接近0越确定；默认为1.0
    )

    # 4.获取响应数据
    ai_response = response.choices[0].message.content

    # 5.更新消息列表中的消息
    messages.pop(0)  # 对话一轮后，删除系统提示词，防止被保存到会话中；下次对话时，系统提示词会重新添加
    messages.append({"role": "assistant", "content": ai_response})
    session_data["messages"] = messages

    # 6.保存会话信息到json文件中
    with open(session_path, "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=4)

    # 7.返回数据
    return ApiResponse(code=200, message="与AI交互成功", data=ai_response)


# 获取会话列表
@app.get("/api/sessions")
def get_sessions() -> ApiResponse:
    logging.info("获取会话列表")

    # 1.获取 sessions 目录下的所有文件名
    session_files = os.listdir("sessions")

    # 2.获取文件名中的会话ID
    session_ids = [session.split(".")[0] for session in session_files]
    session_ids.sort(reverse=True)

    # 3.返回数据
    return ApiResponse(code=200, message="会话列表获取成功", data=session_ids)


# 获取指定的会话信息
@app.get("/api/sessions/{session_id}")  # 路径参数
def get_session(session_id: str) -> ApiResponse:
    # 1.获取会话文件名
    session_file = get_file_name(session_id)

    # 2.读取会话文件中的会话数据
    with open(session_file, "r", encoding="utf-8") as f:
        session_data = json.load(f)

    # 3.返回数据
    return ApiResponse(code=200, message="会话信息获取成功", data=session_data)


# 删除指定的会话
@app.delete("/api/sessions/{session_id}")
def delete_session(session_id: str) -> ApiResponse:
    # 1.获取会话文件名
    session_file = get_file_name(session_id)

    # 2.删除会话文件
    if os.path.exists(session_file):
        os.remove(session_file)

    # 3.返回数据
    return ApiResponse(code=200, message="会话删除成功", data=session_id)


# 全局异常处理
@app.exception_handler(Exception)
def handle_exception(request: Request, exc: Exception):
    logging.error(f"请求地址：{request.url}，异常信息：{exc}")
    return JSONResponse(status_code=500, content={"code": 500, "message": "服务器出错", "data": None})


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080, access_log=False)  # access_log=False：关闭uvicorn框架自带的访问日志
