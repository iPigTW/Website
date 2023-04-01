import streamlit as st
import webbrowser
st.set_page_config(page_title="iPig's Website", page_icon=":pig:", layout="wide", initial_sidebar_state="expanded")
st.sidebar.title("iPig's Website")
st.sidebar.success("Select a page above")
with st.container():
    st.header("About me")
    st.write("I am a 13 years old programmer from Taiwan.")
    st.write("I am currently learning Python.")
with st.container():
    st.write("---")
    st.header("Social Medias")
    st.write("[Discord](https://discord.com/users/933240889357254687)")
    st.write("[GitHub](https://'github.com/ipigtw)")
    st.write("[Twitter](https://twitter.com/ipigtw)")
    st.write("[YouTube](https://www.youtube.com/@ipigtaiwan)")
    st.write("[Twitch](https://www.twitch.tv/ipigtw)")
