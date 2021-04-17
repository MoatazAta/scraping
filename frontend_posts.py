import streamlit as st
from backend import *
def app():
    st.title('Facebook Posts')
    # st.write('lets discover posts')
    page = st.text_input("Facebook username", "")
    if st.button("Submit"):
        download_facebook_post(page)

    st.write('Filter posts')
    myquery = st.text_input("", "")
    if st.button("get posts"):
      listOFposts = readFromDB("tweets" , "yair_ntenyaho" ,myquery)
      st.write(listOFposts['tweet'])

