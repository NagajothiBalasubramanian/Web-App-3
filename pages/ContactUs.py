import streamlit as st
from send_email import send_email
import pandas

st.header("Contact me")

with st.form(key="email_form"):
    user_email=st.text_input("Your Email address")
    df=pandas.read_csv("topics.csv")
    drop_box=st.selectbox("what topics do you want to discuss", df["topic"])
    user_msg=st.text_area("Your message here")
    message=f"""\
    subject:New message
    from:{user_email}
    {user_msg}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your E-mail was sent successfully")
