# from django.shortcuts import render
# from django.http import HttpResponse, Http404
# from django.template import TemplateDoesNotExist
# from django.template.loader import get_template

from urllib import request
from django.views.generic import ListView, DetailView
from .models import Prayer
from django.shortcuts import render, redirect
from .forms import PrayerForm
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

class PrayerListView(ListView):
    model = Prayer
    template_name = 'texty/prayer_list.html'
    context_object_name = 'prayers'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  # Отримуємо параметр "q" з рядка запиту
        if query:
            queryset = queryset.filter(name__icontains=query)  # Фільтруємо за назвою
        return queryset


@login_required
def add_prayer(request):
    if request.method == 'POST':
        form = PrayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('texty:prayer_list')
    else:
        form = PrayerForm()
    return render(request, 'texty/add_prayer.html', {'form': form})


class PrayerDetailView(DetailView):
    model = Prayer
    template_name = 'texty/prayer_detail.html'
    context_object_name = 'prayer'







# def index(request):
#     return render(request, 'texty/index.html')


# def mol_pages(request, page):
#     try:
#         template = get_template('texty/' + page + '.html')
#     except TemplateDoesNotExist:
#         raise Http404
#     return HttpResponse (template.render(request=request))