# from django.shortcuts import render
# from django.http import HttpResponse, Http404
# from django.template import TemplateDoesNotExist
# from django.template.loader import get_template

from urllib import request
from django.views.generic import ListView
from .models import Prayer
from django.shortcuts import render, redirect
from .forms import PrayerForm
from django.contrib.auth.decorators import login_required

class PrayerListView(ListView):
    model = Prayer
    template_name = 'texty/prayer_list.html'
    context_object_name = 'prayers'

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







# def index(request):
#     return render(request, 'texty/index.html')


# def mol_pages(request, page):
#     try:
#         template = get_template('texty/' + page + '.html')
#     except TemplateDoesNotExist:
#         raise Http404
#     return HttpResponse (template.render(request=request))