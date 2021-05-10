#coding= utf-8
from selenium import  webdriver
from time import  sleep,ctime
import  os

options=webdriver.ChromeOptions()
#chrome浏览器的文件位置
options.binary_location="C:/Program Files/Google/Chrome/Application/chrome.exe"
#浏览器驱动地址
chrome_driver_binary="C:/Program Files/Google/Chrome/Application/chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_binary, chrome_options=options)
#测试的网页，打开网页
driver.get("http://www.baidu.com")
sleep(2)
#找到id为“kw”的控件，输入测试文本Test search
driver.find_element_by_id("kw").send_keys("Test search")
#找到id为“su”的控件，模拟鼠标点击
driver.find_element_by_id("su").click()
sleep(2)
driver.quit()