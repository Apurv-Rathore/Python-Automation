'''
import selenium
from selenium import webdriver

from bs4 import BeautifulSoup
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome('C:/Users/ABC/Desktop/chromedriver.exe')
'''
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome('C:/Users/ABC/Desktop/chromedriver.exe')
email = "thelegend2710"
pas= "apoorv2710"
class Bot():
    def __init(self):
        self.driver = webdriver.Chrome('C:/Users/ABC/Desktop/chromedriver.exe')

    def get_website(self):
        self.driver.get("https://www.google.com/account/about/")

        login = driver.find_element_by_xpath('//*[@id="overview"]/div[1]/div[1]/div[5]/ul/li[2]/a')
        login.click()
bot = Bot()
driver.get("https://github.com/")
login = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
login.click()

em = driver.find_element_by_xpath('//*[@id="login_field"]')
em.click()
em.send_keys(email)

password = driver.find_element_by_xpath('//*[@id="password"]')
password.click()
password.send_keys(pas)

l = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
l.click()
