import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "/Users/Rehan/Downloads/chromedriver_win32/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
d = webdriver.Chrome(chromedriver)
d.maximize_window()
d.get("https://www.google.co.in/flights?lite=0#flt=PNQ..2019-04-30*.PNQ.2019-05-04;c:INR;e:1;sd:1;t:h")
time.sleep(1)
d.find_element_by_xpath("//*[@id='flt-app']/div[2]/main[1]/div[3]/div/div[3]/div/div[2]/div[2]").click()
time.sleep(2)
d.find_element_by_xpath("//*[@id='sb_ifc50']/input").send_keys("Nagpur")
time.sleep(2)
d.find_element_by_xpath("//*[@id='sb_ifc50']/input").send_keys(Keys.ARROW_DOWN)
time.sleep(2)
d.find_element_by_xpath("//*[@id='sb_ifc50']/input").send_keys(Keys.ENTER)
time.sleep(2)
d.find_element_by_xpath("//*[@id='flt-app']/div[2]/main[1]/div[3]/div/div[3]/div/div[4]/floating-action-button").click()
time.sleep(2)
count = 1
while count <= 4:
    d.find_element_by_xpath("/html/body").send_keys(Keys.ARROW_DOWN)
    count = count + 1
    time.sleep(1)
print(count)
if count >= 5:
    time.sleep(5)
    d.quit()
