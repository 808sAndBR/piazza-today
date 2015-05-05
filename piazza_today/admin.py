from django.contrib import admin
from .models import Snitch, Offline, Food, Meal

# Register your models here.
admin.site.register(Snitch)
admin.site.register(Offline)
admin.site.register(Food)
admin.site.register(Meal)