import time
import pymongo
from selenium import webdriver

""" ================================---  Write to MONGODB ---================================  """


def addRow(dict, database, column):
    # connect to mongoDB(database)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # localhost:27017

    mydb = myclient[database]

    mycolumn = mydb[column]  # add new column "customers" to  "mydatabase" table

    x = mycolumn.insert_one(dict.copy())


def addPostsToMongoDB(list, database, column):
    for element in list:
        addRow(element, database, column)


def download_facebook_post(page):
    driver = webdriver.Chrome(r"C:\Users\Moataz\Desktop\chromedriver_win32 (3)\chromedriver.exe")
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

    return result


""" ------------------------------- Read From MONGODB -------------------------------------- """


def readData(database, column, myquery):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[database]
    mycol = mydb[column]

    mydoc = mycol.find(myquery)
    return mydoc


""" ================================--- [ Main ]---================================ """
# res = download_facebook_post("ChampionsLeague")
# addPostsToMongoDB(res,"posts","UEFA")
myquery = {"post": { "$regex": "^S" } }
mydoc = readData("posts", "UEFA", myquery)
for x in mydoc:
    print(x)
