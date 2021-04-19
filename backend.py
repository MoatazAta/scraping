import time
from selenium import webdriver

import pandas as pd
import pymongo

import twint

""" ================================--- Read and Write data from mongoDB ---================================  """

""" -------- read posts|tweets from mongoDB -------- """


def readFromDB(database, column, myquery):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[database]
    mycol = mydb[column]

    mydoc = mycol.find(myquery)

    return mydoc


""" -------- write posts|tweets to mongoDB -------- """


def writeToDB(dict, database, column):
    # connect to mongoDB(database)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # localhost:27017

    mydb = myclient[database]

    mycolumn = mydb[column]  # add new column "customers" to  "mydatabase" table

    x = mycolumn.insert_one(dict.copy())


""" ================================--- Tweets ( twint ) ---================================  """

""" -------- Download Tweets ( twint ) -------- """


def download_tweets_twint(username):
    # https://github.com/twintproject/twint/wiki
    a = twint.Config()
    a.Username = username
    a.Limit = 10
    a.Since = "2020-02-01"
    a.Store_csv = True
    a.Output = a.Username + ".csv"
    a.Lang = "he"
    # a.Search = "from:@santi_ABASCAL vox"
    # a.User_full = True
    # a.Pandas = True

    x = twint.run.Search(a)


""" -------- Insert tweets to database -------- """


def insert_Tweets(csv_path, database, column):
    data_dict = {}
    df = pd.read_csv(csv_path)
    columns = df.columns
    index = 0
    for i in range(len(df)):
        for col in columns:
            data_dict[col] = str(df.loc[i][index])
            index += 1
        writeToDB(data_dict, database, column)
        index = 0


""" =================================== Facebook Posts ======================================  """

""" -------- download posts from any page -------- """


def download_facebook_post(page):
    driver = webdriver.Chrome(r"chromedriver.exe")
    driver.get('https://www.facebook.com/' + page + '/')
    for scroll in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    posts = driver.find_elements_by_class_name("userContentWrapper")
    result = []
    for post in posts:
        row = {}
        row.update({"scrap_type": "facebook"})
        row.update({"page": page})
        time_element = post.find_element_by_css_selector("abbr")
        utime = time_element.get_attribute("data-utime")
        row.update({"utime": utime})
        text = ""
        text_elements = post.find_elements_by_css_selector("p")
        for elm in text_elements:
            text += elm.text
        row.update({"post": text})
        result.append(row)
    driver.close()
    insert_posts(result, "posts", page)


""" -------- write posts to mongoDB -------- """


def insert_posts(list, database, column):
    for element in list:
        writeToDB(element, database, column)

download_facebook_post("playstation")