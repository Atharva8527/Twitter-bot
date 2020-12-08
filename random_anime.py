from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import *
import time
def suggest():
    #connecting to your web browser
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--silent")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-logging")
    options.add_argument("--mute-audio")

    options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    driver = webdriver.Chrome(executable_path=PATH,options=options)
    #searching the page
    driver.get("https://www.randomanime.org/custom-list/")
    time.sleep(5)
    #searching an element based on the xpath
    driver.find_element_by_xpath("/html/body/main/section/footer/button[2]").click()

    time.sleep(5)

    title = driver.find_elements_by_xpath("/html/body/main/header/div[1]/div[2]/h2/span[1]")
    for post in title:
        name = post.text


    print(name)
    return name

    driver.close()
