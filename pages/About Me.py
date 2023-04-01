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
    discord = st.button("Discord")
    if discord:
        webbrowser.open('https://discord.gg/JpwjCSNe6Z')
    twitter = st.button("Twitter")
    if twitter:
        webbrowser.open('https://twitter.com/iPigTW')
    github = st.button("GitHub")
    if github:
        webbrowser.open('https://github.com/ipigtw')
    youtube = st.button("YouTube")
    if youtube:
        webbrowser.open('https://youtube.com/@ipigtaiwan')
    twitch = st.button("Twitch")
    if twitch:
        webbrowser.open('https://twitch.tv/ipigtw')
