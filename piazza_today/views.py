from datetime import date, datetime
from django.shortcuts import render
from .models import Food, Meal, Offline, Snitch, Gamenight
from .querys import Clocks

# Create your views here.
def home_page(request):
    return render(request, 'piazza_today/home_page.html', {})

def dev_page(request):
    lunch = Meal.objects.filter(day = date.today).filter(which_meal = 1)[0]
    dinner = Meal.objects.filter(day = date.today).filter(which_meal = 2)[0]
    lunch_food = Food.objects.filter(meal__meal=str(lunch))[:2]
    dinner_food = Food.objects.filter(meal__meal=str(dinner))[:2]
    current_time = datetime.now()
    pa_time = Clocks().pa_clock()
    lv_time = Clocks().lv_clock()
    header_date = Clocks().head_date()
    return render(request, 'piazza_today/dev_page.html', {'pa_time':pa_time, 'lv_time':lv_time, 'header_date':header_date, 'lunch':lunch, 'dinner':dinner, 'lunch_food':lunch_food, 'dinner_food':dinner_food})