from selenium import webdriver
import time

browser = webdriver.Chrome('/home/feng/chromedriver_linux64/chromedriver')
browser.get("https://www.baidu.com")
time.sleep(2)

##### 百度输入框的定位方式 ####

# 通过id方式定位
browser.find_element_by_id("kw").send_keys("selenium")
# 通过name方式定位
browser.find_element_by_name("wd").send_keys("selenium")
# 通过tag name方式定位
browser.find_element_by_tag_name("input").send_keys("selenium")
# 通过class name方式定位
browser.find_element_by_class_name("s_ipt").send_keys("selenium")
# 通过css方式定位
browser.find_element_by_css_selector("#kw").send_keys("selenium")
# 通过xpath方式定位
browser.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")

##########################
browser.find_element_by_xpath("//a[contains(text(),'网页')]").click()

browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()
