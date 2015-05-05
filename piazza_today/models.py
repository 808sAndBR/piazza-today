from django.db import models
from django.contrib.auth.models import User

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
    date_leaving = models.DateField()
    date_returning = models.DateField()

class Snitch(models.Model):
    pass

class Gamenight(models.Model):
    catagory = models.CharField(max_length = 200)