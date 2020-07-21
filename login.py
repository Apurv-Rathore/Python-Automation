import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome('C:/Users/ABC/Desktop/chromedriver.exe')
class Bot():
    def __init(self):
        self.driver = webdriver.Chrome('C:/Users/ABC/Desktop/chromedriver.exe')

    def get_website(self):
        self.driver.get("https://www.google.com/account/about/")
bot = Bot()
driver.get("https://www.google.com/account/about/")


