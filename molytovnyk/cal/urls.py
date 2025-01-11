# from django import views
from django.urls import path
from .views import today_holiday, add_holiday


app_name = 'cal'

urlpatterns = [
    path('', today_holiday, name='today_holiday'),
    path('add', add_holiday, name='add_holiday'),
]