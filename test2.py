from selenium import webdriver
import time

browser = webdriver.Chrome('/home/feng/chromedriver_linux64/chromedriver')
browser.get('https://www.baidu.com')
time.sleep(1)

browser.find_element_by_xpath("//a[contains(text(),'贴吧')]").click()

time.sleep(1)
browser.quit()
