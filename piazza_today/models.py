from django.db import models

class Meal(models.Model):
    meal = models.CharField(max_length = 200)
    time = models.TimeField()
    day = models.DateField()
    resturant = models.TextField()

    def __str__(self):
        return self.meal

class Food(models.Model):
    item = models.TextField(blank = True, null = True)
    meal = models.ForeignKey(Meal)
    def __str__(self):
        return self.item

class Offline(models.Model):
    pass

class Snitch(models.Model):
    pass