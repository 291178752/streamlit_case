import streamlit as st

# hmbb
name = st.text_input('请输入你的名字')
age = st.slider('请输入你的年龄', 0, 100, 25)

st.write(f'你好，{name}！你的年龄是{age}岁。')