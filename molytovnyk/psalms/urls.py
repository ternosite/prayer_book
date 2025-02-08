from django.urls import path
from .views import PsalmListView


app_name = 'psalms'

urlpatterns = [
    path('', PsalmListView.as_view(), name='psalm_list')
]