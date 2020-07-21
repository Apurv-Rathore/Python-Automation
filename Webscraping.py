import selenium
from selenium import webdriver

from bs4 import BeautifulSoup
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome('C:/Users/ABC/Desktop/chromedriver.exe')
name = []
ratings = []
driver.get('https://www.imdb.com/chart/top/')

content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('td',attrs={'class':'titleColumn'}):
    name.append(str(a.text).strip())

for b in soup.findAll('td' , attrs={'class':'ratingColumn imdbRating'}):
    ratings.append(str(b.text).strip())


for i in range(10):
    print(name[i],ratings[i])
    print("------------------------")

