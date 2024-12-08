from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template

# Create your views here.
def index(request):
    return render(request, 'texty/index.html')


def mol_pages(request, page):
    try:
        template = get_template('texty/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse (template.render(request=request))