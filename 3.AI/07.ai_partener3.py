import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",  # emoji百宝箱：https://emoji6.com/zh
    # 布局（占满整个区域）
    layout="wide",
    # 控制的是侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)


# 保存会话信息
def save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
        new_session = {
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages,
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature
        }

        # 如果sessions目录不存在，则创建
        if not os.path.exists("sessions"):
            os.makedirs("sessions")

        # 保存会话信息到文件
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(new_session, f, ensure_ascii=False, indent=2)


# 生成会话标识
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# 加载所有的会话列表信息
def load_sessions():
    sessions_list = []
    # 加载sessions目录下的文件
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                sessions_list.append(filename[:-5])  # 去掉.json后缀
    sessions_list.sort(reverse=True)  # 降序排列
    return sessions_list


# 加载指定会话信息函数
def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.current_session = session_data["current_session"]
                st.session_state.messages = session_data["messages"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
    except Exception as e:
        st.error(f"加载会话信息失败 {session_name}: {e}")


# 删除会话信息函数
def delete_session(session_name):
    try:
        # 判断会话json文件是否存在
        if os.path.exists(f"sessions/{session_name}.json"):
            # os.remove() 删除指定路径的会话json文件
            os.remove(f"sessions/{session_name}.json")

        # 如果删除的会话是当前正在使用的会话
        if session_name == st.session_state.current_session:
            # 清空页面所有聊天消息列表
            st.session_state.messages = []
            # 生成全新会话名，切换为新空白会话
            st.session_state.current_session = generate_session_name()

    except Exception:
        # 捕获所有异常，前端弹出错误提示
        st.error("删除会话失败！")


# 大标题
st.title("AI智能伴侣")

# Logo
st.logo("🌏️")

# 创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY：环境变量的名字，值就是DeepSeek的API_KEY的值 ---> 该值可通过终端配置：“open ~/.zshrc”）
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 系统提示词
system_prompt = """
    你叫 %s，现在是用户的真实伴侣，请完全代入伴侣角色。
    规则：
    1．每次只回1条消息
    2．禁止任何场景或状态描述性文字
    3．匹配用户的语言
    4．回复简短，像微信聊天一样
    5．有需要的话可以用❤️🌸等emoji表情
    6．用符合伴侣性格的方式对话
    7．回复的内容，要充分体现伴侣的性格特征
    
    伴侣性格：
    - %s
    
    你必须严格遵守上述规则来回复用户。
"""

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 初始化昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"

# 初始化性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的东北姑娘"

# 会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()

# 左侧的侧边栏 - with:streamlit中上下文管理器
with st.sidebar:
    # 会话信息
    st.subheader("AI控制面板")

    # 新建会话
    if st.button("新建会话", width="stretch", icon="✏️"):
        # 1.保存当前会话信息
        save_session()

        # 2.创建新的会话
        if st.session_state.messages:  # 如果聊天信息非空，True；否则，False
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun()  # 重新运行当前页面

    # 会话历史
    st.text("会话历史")
    sessions_list = load_sessions()
    for session in sessions_list:
        col1, col2 = st.columns([4, 1])  # 创建两列，比例为4:1
        with col1:
            # 加载会话信息
            if st.button(session, width="stretch", icon="📖", key=f"load_{session}",
                         type="primary" if session == st.session_state.current_session else "secondary"):  # 三元运算符：<true_value> if 条件表达式 else <false_value>
                load_session(session)
                st.rerun()

        with col2:
            # 删除会话信息
            if st.button("", width="stretch", icon="❌", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    # 分割线
    st.divider()

    st.subheader("伴侣信息")

    # 昵称输入框
    nick_name = st.text_input("昵称", placeholder="请输入昵称", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name

    # 性格输入框
    nature = st.text_area("性格", placeholder="请输入性格", value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

# 展示现有的聊天信息
st.text(f"会话名称：{st.session_state.current_session}")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("请输入内容")
if prompt:
    # 用户输入信息展示到页面
    st.chat_message("user").write(prompt)
    print("----输出到终端调试的信息，调用大模型，生成回复---->", prompt)

    # 将用户输入信息添加到会话状态中
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 与AI大模型进行交互（参数）
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages,  # 会话记忆能力
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型的回复（流式输出的方式）
    response_message = st.empty()  # 创建一个空的组件，用于展示大模型返回的结果

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content

            # 将大模型的回复展示到页面
            response_message.chat_message("assistant").write(full_response)

    # 将大模型的回复添加到会话状态中
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    # 保存会话信息
    save_session()
