from datetime import date, datetime
from django.shortcuts import render
from .models import Food, Meal, Offline, Snitch, Gamenight, TeamEvent
from .querys import Clocks

# Create your views here.
def home_page(request):
    try:
        lunch = Meal.objects.filter(day = date.today).filter(which_meal = 1)[0]
    except IndexError:
        lunch = "No Lunch Today"
    try:
        dinner = Meal.objects.filter(day = date.today).filter(which_meal = 2)[0]
    except IndexError:
        dinner = "No Dinner Today"
    lunch_food = Food.objects.order_by('-meal__day').filter(meal__meal=str(lunch))[:7]
    dinner_food = Food.objects.filter(meal__meal=str(dinner))[:7]
    current_time = datetime.now()
    pa_time = Clocks().pa_clock()
    lv_time = Clocks().lv_clock()
    header_date = Clocks().head_date()
    events = TeamEvent.objects.filter(event_date__gte=date.today).order_by('event_date')[:5]
    snitch = Snitch.objects.latest('win_date')
    vacation = Offline.objects.filter(date_returning__gte=date.today).filter(date_leaving__lte=date.today).order_by('date_returning')
    gamenight_winner = Gamenight.objects.latest('win_date')
    return render(request, 'piazza_today/home_page.html', {'pa_time':pa_time,
        'lv_time':lv_time, 'header_date':header_date, 'lunch':lunch, 'dinner':dinner,
        'lunch_food':lunch_food, 'dinner_food':dinner_food, 'events':events, 'snitch':snitch,
        'vacation':vacation, 'gamenight_winner':gamenight_winner})

def dev_page(request):
    lunch = Meal.objects.filter(day = date.today).filter(which_meal = 1)[0]
    dinner = Meal.objects.filter(day = date.today).filter(which_meal = 2)[0]
    lunch_food = Food.objects.filter(meal__meal=str(lunch))[:2]
    dinner_food = Food.objects.filter(meal__meal=str(dinner))[:2]
    current_time = datetime.now()
    pa_time = Clocks().pa_clock()
    lv_time = Clocks().lv_clock()
    header_date = Clocks().head_date()
    events = TeamEvent.objects.filter(event_date__gt=date.today)
    snitch = Snitch.objects.latest('win_date')
    vacation = Offline.objects.filter(date_returning__gte=date.today).filter(date_leaving__lte=date.today)
    gamenight_winner = Gamenight.objects.latest('win_date')
    return render(request, 'piazza_today/dev_page.html', {'pa_time':pa_time,
        'lv_time':lv_time, 'header_date':header_date, 'lunch':lunch, 'dinner':dinner,
        'lunch_food':lunch_food, 'dinner_food':dinner_food, 'events':events, 'snitch':snitch,
        'vacation':vacation, 'gamenight_winner':gamenight_winner})
