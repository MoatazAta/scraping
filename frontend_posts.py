import streamlit as st
from backend import *


def app():
    st.title('Facebook Posts')
    page = st.text_input("Facebook username", "")
    if st.button("Submit"):
        download_facebook_post(page)
        st.write("posts downloaded and saved to database :)")

    st.write('Get posts with a specific word')
    word = st.text_input("keyword", "")
    myquery = {"post": {"$regex": "\W*(" + word + ")\W*"}}
    if st.button("get posts"):
        listOFposts = readFromDB("posts", page, myquery)
        counter = 1
        for post in listOFposts:
            st.write(str(counter) + " - post: " + post['post'])
            counter += 1
