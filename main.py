import streamlit as st
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>HOME</h1>", unsafe_allow_html=True)

col1,col2=st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Archiet Viswajit Tanwar")
    content='''I'm Archiet Tanwar, a B.Tech student in Information Technology from India. I'm passionate about programming and love building practical projects that help me learn and grow. I primarily work with Python and have explored tools like Streamlit, PySimpleGUI, and the PIL library for image processing. I enjoy creating simple apps like to-do lists, attendance trackers, and basic image editing tools. Along the way, I’ve developed a strong interest in backend development, JSON data handling, and networking concepts. I prefer a hands-on approach to learning and often look for quick, clear examples to understand things better. I usually mix Hindi and English when I ask for help or discuss ideas casually, and I’m always excited to try new tech and improve my skills.'''
    st.info(content)