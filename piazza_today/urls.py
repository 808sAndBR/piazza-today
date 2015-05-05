from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^dev/$',views.dev_page),
]