from django.urls import path
from .views import PrayerListView, add_prayer



app_name = 'texty'

urlpatterns = [
    path('', PrayerListView.as_view(), name='prayer_list'), 
    path('add', add_prayer, name='add_prayer'), 
    # path('', index, name='index'), 
    # path('<str:page>/', mol_pages, name='pages'),
]
