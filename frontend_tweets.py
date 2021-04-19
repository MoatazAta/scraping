from asyncio import sleep

import streamlit as st
from backend import *


def app():
    st.title('Twitter tweets')
    username = st.text_input("twitter username", "")
    if st.button("Submit"):
        download_tweets_twint(username)
        csv_path = username + '.csv'
        sleep(3000)
        insert_Tweets(csv_path, "tweets", username)
        st.write("tweets downloaded and saved to database :)")


    st.write('Get tweets in a specific day')
    date = st.text_input("Date", "yyyy-mm-dd")
    if st.button("get tweets"):
        myquery = {"date": date}
        mydoc = readFromDB("tweets", username, myquery)
        counter = 1
        for row in mydoc:
            st.write(str(counter) + " - tweet: " + row['tweet'])
            counter += 1
