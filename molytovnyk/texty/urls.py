from django.urls import path
from .views import PrayerListView


app_name = 'texty'

urlpatterns = [
    path('', PrayerListView.as_view(), name='prayer_list'), 
    # path('', index, name='index'), 
    # path('<str:page>/', mol_pages, name='pages'),
]
