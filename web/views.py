from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader, TemplateDoesNotExist

def index(request):
    return render(request, 'index.html')

def frontend(request, page='index'):
    try:
        template = loader.get_template(page + '.html')
    except TemplateDoesNotExist:
        raise Http404("Page " + page + " does not exist")
    return HttpResponse(template.render({}, request))

