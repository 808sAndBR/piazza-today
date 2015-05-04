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
    days_soup.find("h1", { "class" : "vendor-name"}
    food_items = []
    food_items_soup = BeautifulSoup(str(days_soup.find_all("h4", { "class" : "item-name" })))
    for yummy in food_items_soup.stripped_strings:
        if yummy != "," and yummy != "[" and yummy != "]":
            food_items.append(yummy)


