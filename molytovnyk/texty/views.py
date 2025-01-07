# from django.shortcuts import render
# from django.http import HttpResponse, Http404
# from django.template import TemplateDoesNotExist
# from django.template.loader import get_template

from django.views.generic import ListView
from .models import Prayer

class PrayerListView(ListView):
    model = Prayer
    template_name = 'texty/prayer_list.html'
    context_object_name = 'prayers'







# def index(request):
#     return render(request, 'texty/index.html')


# def mol_pages(request, page):
#     try:
#         template = get_template('texty/' + page + '.html')
#     except TemplateDoesNotExist:
#         raise Http404
#     return HttpResponse (template.render(request=request))