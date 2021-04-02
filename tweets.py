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


""" ------------------------------- Read From MONGODB -------------------------------------- """


def readData():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["tweets"]
    mycol = mydb["yair_ntenyaho"]

    myquery = {"date": "2021-04-01"}

    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)


""" =====================================---[ Main ]---================================ """
# process_csv("YairNetanyahu.csv")
# readData()
