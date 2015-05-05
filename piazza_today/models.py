from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

class Meal(models.Model):
    meal = models.CharField(max_length = 200)
    day = models.DateField()
    resturant = models.TextField()
    which_meal = models.IntegerField(default = 5)

    def __str__(self):
        return self.meal

class Food(models.Model):
    item = models.TextField(blank = True, null = True)
    meal = models.ForeignKey(Meal)
    def __str__(self):
        return self.item

class Offline(models.Model):
    person = models.ForeignKey(User)
    date_leaving = models.DateField(default=date.today)
    date_returning = models.DateField(default=date.today)
    
    def __str__(self):
        return self.person.first_name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birthdate = models.DateField()
    aniversery = models.DateField(default=date.today)

    def __str__(self):
        return self.person.first_name

class Snitch(models.Model):
    person = models.ForeignKey(User)
    win_date = models.DateField(default=date.today)
    email_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.person.first_name

class Gamenight(models.Model):
    person = models.ForeignKey(User)
    win_date = models.DateField(default=date.today)
    catagory = models.CharField(max_length = 200)

    def __str__(self):
        return self.person.first_name

class EventType(models.Model):
    celibration = models.CharField(max_length = 200)

    def __str__(self):
            return self.celibration

class TeamEvent(models.Model):
    event_name = models.CharField(max_length = 200)
    event_date = models.DateField(default=date.today)
    start_time = models.TimeField(default=datetime.now().time())
    end_time = models.TimeField(default=datetime.now().time())
    created_by = models.ForeignKey('auth.User')
    event_type = models.ForeignKey(EventType)

    def __str__(self):
            return self.event_name
        