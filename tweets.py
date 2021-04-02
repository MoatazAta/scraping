import pandas as pd
import pymongo

import twint


def download_tweets_twint():
    # https://github.com/twintproject/twint/wiki
    a = twint.Config()

    a.Username = 'YairNetanyahu'
    a.Limit = 10
    # a.Since = "2020-02-01"
    a.Store_csv = True
    a.Output = a.Username + ".csv"
    a.Lang = "he"

    # a.Search = "from:@santi_ABASCAL vox"

    # a.User_full = True
    # a.Pandas = True

    x = twint.run.Search(a)


""" ------------------------------- Write to MONGODB -------------------------------------- """


def addRow(dict):
    # connect to mongoDB(database)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # localhost:27017

    mydb = myclient["tweets"]

    mycolumn = mydb["yair_ntenyaho"]  # add new column "customers" to  "mydatabase" table

    x = mycolumn.insert_one(dict.copy())


def readData():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["tweets"]
    mycol = mydb["yair_ntenyaho"]

    myquery = {"date": "2021-04-01"}

    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)


def writeToDataBase():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # localhost:27017

    mydb = myclient["mydatabase"]

    print(myclient.list_database_names())
    dblist = myclient.list_database_names()
    if "mydatabase" in dblist:  # check if "mydatabase" table exist in mongodb
        print("The database exists.")
    mycolumn = mydb["customers"]  # add new column "customers" to  "mydatabase" table
    print(mydb.list_collection_names())
    collist = mydb.list_collection_names()
    if "customers" in collist:
        print("The collection exists.")
    mydict = {"name": "AAA", "address": "BBBB"}  # the data that we would add it to "customers".
    x = mycolumn.insert_one(mydict)  # add to mongodb


# def download_facebook_post(page):
#     driver = webdriver.Chrome()
#     driver.get('https://www.facebook.com/' + page + '/')
#     for scroll in range(5):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
#     posts = driver.find_elements_by_class_name("userContentWrapper")
#     result = []
#     for post in posts:
#         row = {}
#     row.update({"scrap_type": "facebook"})
#     row.update({"page": page})
#     time_element = post.find_element_by_css_selector("abbr")
#     utime = time_element.get_attribute("data-utime")
#     row.update({"utime": utime})
#     text = ""
#     text_elements = post.find_elements_by_css_selector("p")
#     for elm in text_elements:
#         text += elm.text
#     row.update({"post": text})
#     result.append(row)
#     driver.close()
#     return result


def process_csv(csv_path):
    data_dict = {}
    df = pd.read_csv(csv_path)
    columns = df.columns
    index = 0
    for i in range(len(df)):
        for col in columns:
            data_dict[col] = str(df.loc[i][index])
            index += 1
        addRow(data_dict)
        index = 0


""" =====================================---[ Main ]---================================ """
# process_csv("YairNetanyahu.csv")
readData()
