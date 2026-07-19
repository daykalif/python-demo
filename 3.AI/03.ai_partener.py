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
system_prompt = "你是一名非常可爱的AI助理，你的名字叫小甜甜，请你使用温柔可爱的语气回答用户的问题"

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

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
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型的回复（非流式输出的方式）
    print(response.choices[0].message.content)

    # 将大模型的回复展示到页面
    st.chat_message("assistant").write(response.choices[0].message.content)

    # 将大模型的回复添加到会话状态中
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
