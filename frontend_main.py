import streamlit as st

import frontend_posts
import frontend_tweets

PAGES = {
    "posts": frontend_posts,
    "tweets": frontend_tweets
}

st.sidebar.title('Lab1')
selection = st.sidebar.selectbox('Select Dataset', list(PAGES.keys()))
page = PAGES[selection]
page.app()
