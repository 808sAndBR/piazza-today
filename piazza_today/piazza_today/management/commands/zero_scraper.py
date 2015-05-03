from bs4 import BeautifulSoup
from datetime import date, datetime
import requests

r =requests.get('https://zerocater.com/m/BYFJ/')
soup = BeautifulSoup(r.text)

def menu_scrape():
    d = datetime.isocalendar(date.today())
    #this matches the format of zerocator
    today_match = str(d).replace(', ','-').replace('(','').replace(')','')
    f = soup.find_all("div", {"data-date": today_match})
    for x in f:
        today_soup = BeautifulSoup(f)
        menu_info(today_soup)

def menu_info(days_soup):
    #should be able to start pulling data diretly with days_soup.find_all("div", { "class" : "item-name" })
    #and days_soup.find_all("div", { "class" : "vendor-name"}
