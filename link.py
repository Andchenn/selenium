from selenium import webdriver
import time

browser = webdriver.Chrome('/home/feng/chromedriver_linux64/chromedriver')
browser.get("https://www.baidu.com")
time.sleep(2)

# link 定位
browser.find_element_by_link_text("贴吧").click()

# Partial Link Text 定位
browser.find_element_by_partial_link_text("贴").click()
time.sleep(2)
browser.quit()
