from django.urls import path
from .views import index, mol_pages


app_name = 'texty'

urlpatterns = [
    path('', index, name='index'), 
    path('<str:page>/', mol_pages, name='pages'),
]
