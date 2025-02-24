from django.urls import path
from .views import PrayerListView, add_prayer, PrayerDetailView



app_name = 'texty'

urlpatterns = [
    path('', PrayerListView.as_view(), name='prayer_list'), 
    path('add', add_prayer, name='add_prayer'),
    path('<int:pk>/', PrayerDetailView.as_view(), name='prayer_detail'),
]
