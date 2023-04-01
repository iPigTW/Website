import streamlit as st
st.set_page_config(page_title="iPig's Website", page_icon=":pig:", layout="wide", initial_sidebar_state="expanded")
st.sidebar.title("iPig's Website")
st.sidebar.success("Select a page above")
with st.container():
    st.header("My projects")
    left_column, right_column = st.columns(2)

    with left_column:
        st.write("Here are some of my projects:")
        st.write("- [RoPig(Discord Bot)](https://discord.com/api/oauth2/authorize?client_id=1058641797431169106&permissions=8&scope=bot)")
        st.write("- [Piggy Selfbot](https://link-center.net/201315/piggy-selfbot)")
