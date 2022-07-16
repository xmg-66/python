import time
from selenium import webdriver


browser=webdriver.Chrome()  
path=r'E:\python\Scripts\chromedriver.exe'
browser =webdriver.Chrome(path)

browser.maximize_window()
browser.get(r'https://www.baidu.com/')
browser.find_element_by_id('kw').send_keys('python')
time.sleep(2)
browser.find_element_by_id("su").click()
time.sleep(2)




browser.close()
