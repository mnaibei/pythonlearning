from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json


#print(urlpage)

driver = webdriver.Chrome("/usr/bin/chromedriver")

driver.get("https://www.pigiame.co.ke/apartments-for-rent/nairobi?location=kilimani")

#html = driver.execute_script("return document.documentElement.outerHTML")

sel_soup = BeautifulSoup(r.content, 'html.parser')

#print(sel_soup.findAll("apartments-for-rent"))