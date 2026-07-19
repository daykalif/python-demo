import streamlit as st
import os
from openai import OpenAI

# 设置也没的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",  # emoji百宝箱：https://emoji6.com/zh
    # 布局（占满整个区域）
    layout="wide",
    # 控制的是侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)

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

# 左侧的侧边栏 - with:streamlit中上下文管理器
with st.sidebar:
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
