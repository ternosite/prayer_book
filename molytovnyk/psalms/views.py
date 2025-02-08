from django.views.generic import ListView, DetailView
from .models import Psalm
from django.shortcuts import render, redirect


class PsalmListView(ListView):
    model = Psalm
    template_name = 'psalms/psalm_list.html'
    context_object_name = 'psalms'


class PsalmDetailView(DetailView):
    model = Psalm
    template_name = 'psalms/psalm_detail.html'
    context_object_name = 'psalm'



