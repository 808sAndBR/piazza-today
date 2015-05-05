from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
from datetime import date, datetime
from piazza_today.models import Meal, Food
import requests

def handle(self, *args, **options):
    self.stdout.write('\nScraping started at %s\n' % str(datetime.datetime.now()))
        
    r =requests.get('https://zerocater.com/m/BYFJ/')
    soup = BeautifulSoup(r.text)

    def menu_scrape():
        d = datetime.isocalendar(date.today())
        today_match = date.today().isoformat()
        f = soup.find_all("div", {"data-date": today_match})
        meal_num = 1
        for x in f:
            menu_info(str(x),meal_num)
            meal_num += 1

    def menu_info(days_soup,meal_num):
        days_soup = BeautifulSoup(days_soup)
        resturant = days_soup.find("h1", { "class" : "vendor-name"}).string[1:]
        day = date.today().isoformat()
        meal = days_soup.find("h3", { "class" : "order-name"}).string
        which_meal = meal_num
        new_meal = Meal.objects.create(meal=meal, day=day, resturant=resturant, which_meal=which_meal)
        food_items_soup = BeautifulSoup(str(days_soup.find_all("h4", { "class" : "item-name" })))
        for yummy in food_items_soup.stripped_strings:
            if yummy != "," and yummy != "[" and yummy != "]":
                item = yummy 
                new_food = Food.objects.create(item=item, meal=new_meal)
        print "..............................."
