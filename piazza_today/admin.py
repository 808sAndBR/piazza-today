from django.contrib import admin
from .models import Snitch, Offline, Food, Meal, UserProfile, Gamenight, EventType, TeamEvent

# Register your models here.
admin.site.register(Snitch)
admin.site.register(Offline)
admin.site.register(Food)
admin.site.register(Meal)
admin.site.register(UserProfile)
admin.site.register(Gamenight)
admin.site.register(EventType)
admin.site.register(TeamEvent)