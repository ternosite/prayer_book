from django.views.generic import ListView, DetailView
from .models import Psalm
from django.shortcuts import render, redirect
from .forms import PsalmForm


class PsalmListView(ListView):
    model = Psalm
    template_name = 'psalms/psalm_list.html'
    context_object_name = 'psalms'


class PsalmDetailView(DetailView):
    model = Psalm
    template_name = 'psalms/psalm_detail.html'
    context_object_name = 'psalm'


def add_psalm(request):
    if request.method == 'POST':
        form = PsalmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('psalms:psalm_list')
    else:
        form = PsalmForm()
    return render(request, 'psalms/add_psalm.html', {'form': form})




