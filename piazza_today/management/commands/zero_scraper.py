from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
from datetime import date, datetime
import requests

def handle(self, *args, **options):
    self.stdout.write('\nScraping started at %s\n' % str(datetime.datetime.now()))
        
        r =requests.get('https://zerocater.com/m/BYFJ/')
        soup = BeautifulSoup(r.text)

        def menu_scrape():
            d = datetime.isocalendar(date.today())
            #this matches the format of zerocator
            #today_match = str(d).replace(', ','-').replace('(','').replace(')','')
            today_match = date.today().isoformat()
            print today_match
            f = soup.find_all("div", {"data-date": today_match})
            for x in f:
                menu_info(str(x))

        def menu_info(days_soup):
            days_soup = BeautifulSoup(days_soup)
            print days_soup.find("h1", { "class" : "vendor-name"}).string
            food_items = []
            food_descriptions = []
            food_items_soup = BeautifulSoup(str(days_soup.find_all("h4", { "class" : "item-name" })))
            for yummy in food_items_soup.stripped_strings:
                if yummy != "," and yummy != "[" and yummy != "]":
                    food_items.append(yummy)
            print food_items
