"""
1. 什么是 Streamlit？
Streamlit 是一个可以基于 Python 代码快速搭建 Web 网页的 Python 库，尤其适配数据科学、机器学习领域的项目开发。

2. Streamlit 的使用步骤？
安装依赖：执行命令pip install streamlit完成库的安装
页面开发：调用 Streamlit 提供的 API 编写代码，搭建网页的内容与交互逻辑
启动服务：执行命令streamlit run xxx.py（xxx.py 为你的代码文件名）运行项目，打开网页查看效果

streamlit官方文档：
https://docs.streamlit.io/

运行程序，当前文件夹路径终端：streamlit run 02.streamlit入门.py
"""
import streamlit as st

# 设置也没的配置项
st.set_page_config(
    page_title="Streamlit入门",
    page_icon="🧊",
    # 布局
    layout="wide",
    # 控制的是侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# 大标题
st.title('Streamlit 入门演示')
st.header('Streamlit 一级标题')
st.subheader('Streamlit 二级标题')

# 段落文字
st.write(
    "Get started with Streamlit! Set up your development environment and learn the fundamental concepts, and start coding!")
st.write(
    "Develop your Streamlit app! Our API reference explains each Streamlit function with examples. Dive deep into all of our features with conceptual guides. Try out our step-by-step tutorials.")
st.write(
    "Deploy your Streamlit app! Streamlit Community Cloud our free platform for deploying and sharing Streamlit apps. Streamlit in Snowflake is an enterprise-class solution where you can house your data and apps in one, unified, global system. Explore all your options!")
st.write(
    "Knowledge base is a self-serve library of tips, tricks, and articles that answer your questions about creating and deploying Streamlit apps.")

# 图片
st.image('./Streamlit入门程序.png', width=300)
st.image('Streamlit入门程序.png', width=200)

# 音频
st.audio('https://doc-audio.streamlit.app/~/+/media/bd783c112d70d61d823e6cc2ba07a910ab7f2ceb3413f469fa4b4e57')

# 视频
st.video('https://static.streamlit.io/examples/star.mp4')

# Logo
st.logo("https://doc-logo.streamlit.app/~/+/media/741ec0d841fdc835bd1699e8117e946d9bce84aebd71f5e28eab2b36.png")

# 表格
student_data = {
    "姓名": ["王林", "李木婉", "张三", "李四", "王五"],
    "语文": [88, 90, 84, 75, 93],
    "数学": [90, 84, 83, 93, 73],
}
st.table(student_data)

# 输入框
name = st.text_input("请输入姓名", "张三")
st.write("您输入的姓名为：", name)

password = st.text_input("请输入密码", type="password")
st.write("您输入的密码为：", password)

# 单选按钮
gender = st.radio("请选择你哪的性别", ["男", "女", "未知"], index=2)
st.write("您的性别为:", gender)
