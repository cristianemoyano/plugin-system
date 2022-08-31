from django.http import HttpResponse
from django.template import loader

def index(request) -> HttpResponse:
  template = loader.get_template('index.html')
  return HttpResponse(template.render())