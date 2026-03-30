import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "dashboard", "index.html")

try:
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    components.html(html_content, height=1200, scrolling=True)
    
except FileNotFoundError:
    st.error(f"파일을 찾을 수 없습니다. 경로 확인: {html_path}")
    st.write("현재 폴더 내 파일들:", os.listdir(current_dir))
