import time
import tkinter as tk
from selenium import webdriver

""" ================================---  [ GUI ] ---================================  """
# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, height=25, command=r.destroy)
# button.pack()
# r.mainloop()

""" ================================---  Write to MONGODB ---================================  """


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


""" ================================--- [ Main ]---================================ """
# res = download_facebook_post("ChampionsLeague")
# print(len(res))
