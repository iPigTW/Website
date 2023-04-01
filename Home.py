import streamlit as st
st.set_page_config(page_title="iPig's Website", page_icon=":pig:", layout="wide", initial_sidebar_state="expanded")
st.sidebar.title("iPig's Website")
st.sidebar.success("Select a page above")
embed = """
<head>
<meta content="iPig's Website" property="og:title" />
<meta content="Python Programmer" property="og:description" />
<meta content="https://ipigtw.streamlit.app" property="og:url" />
<meta content="#0096ff" data-react-helmet="true" name="theme-color" />
</head>
"""
with st.container():
    st.title("Welcome to iPig's Website!")
    st.write("This is a website made by iPig using Streamlit.")
    st.write("This website is still under development")

