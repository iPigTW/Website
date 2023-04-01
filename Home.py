import streamlit as st
st.set_page_config(page_title="iPig's Website", page_icon=":pig:", layout="wide", initial_sidebar_state="expanded")
st.sidebar.title("iPig's Website")
st.sidebar.success("Select a page above")

with st.container():
    st.title("Welcome to iPig's Website!")
    st.write("This is a website made by iPig using Streamlit.")
    st.write("This website is still under development")

