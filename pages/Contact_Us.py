import streamlit as st
from send_email import send_mail

st.header("Contact Me")

with st.form(key="user_input"):
    email=st.text_input("Enter your email")
    msg=st.text_area("Enter your message")
    button=st.form_submit_button("SUBMIT")
    if button:
        send_mail("email",msg)
