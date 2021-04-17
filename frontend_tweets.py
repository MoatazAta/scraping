import streamlit as st
from backend import *
def app():
    st.title('Twitter tweets')
    username = st.text_input("twitter username", "")
    if st.button("Submit"):
        download_tweets_twint(username)
        csv_path = username + '.csv'
        insert_Tweets(csv_path, "tweets", username)



    st.write('Filter tweets')
    date = st.text_input("Date", "yyyy-mm-dd")
    if st.button("get tweets"):
        myquery = {"date": date}
        mydoc = readFromDB("tweets", username, myquery)
        for row in mydoc:
            st.write("tweet: " + row['tweet'])
