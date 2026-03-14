import streamlit as st  
import streamlit_authenticator as stauth  
from menu import menu
from database import users_dict
st.set_page_config(layout="wide")
st.session_state.setdefault("authentication_status", False)
# Redirecting if needed
menu()

st.title("Welcome Back!")


authenticator = stauth.Authenticate(users_dict,
    "ab", "ab", 0, "abcdef")

name, authentication_status, username = authenticator.login(
    "main", "Log-in into your account"
)


if authentication_status==False:
    st.error("Incorrect credentials")
    register_button= st.button("Don't have an account yet? Register here!")
    if register_button:
        st.switch_page("pages/user_registration_page.py")

if authentication_status:
    st.success("Login Sucessful")
    st.session_state.authentication_status = True
    st.session_state.username = username
    st.session_state.name = name
    menu(change=True)
if authentication_status==None:
    st.warning("Please enter your email and password")
    register_button= st.button("Don't have an account yet? Register here!")
    if register_button:
        st.switch_page("pages/user_registration_page.py")