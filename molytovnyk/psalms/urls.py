from django.urls import path
from .views import PsalmListView, add_psalm, PsalmDetailView


app_name = 'psalms'

urlpatterns = [
    path('', PsalmListView.as_view(), name='psalm_list'),
    path('add', add_psalm, name='add_psalm'),
    path('psalms/<int:pk>/', PsalmDetailView.as_view(), name='psalm_detail'),
]