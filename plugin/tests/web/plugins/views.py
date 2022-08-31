import sys
import os
from typing import Any

from django.http import HttpResponse
from django.template import loader

from .models import Plugins

def setup_path() -> None:
    path: str = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir)
    sys.path.append(path)  

setup_path()

from plugin_manager.services import PackageService

def index(request) -> HttpResponse:
  plugins: list = PackageService.list_packages('packages')
  records: Any = Plugins.objects.all().values()
  template: Any = loader.get_template('index.html')
  context: dict[str, Any] = {
    'records': records,
    'plugins': plugins,
  }
  return HttpResponse(template.render(context, request))


def download(request) -> HttpResponse:
  package: str = ''
  if request.method == 'POST':
        package: str = request.POST.get('package')
  html: str = f"Download Success: {package}"
  return HttpResponse(html)

def upload(request) -> HttpResponse:
  package: str = ''
  if request.method == 'POST':
        package: str = request.POST.get('package')
  html: str = f"Upload Success: {package}"
  return HttpResponse(html)

def zip(request) -> HttpResponse:
  package: str = ''
  if request.method == 'POST':
        package: str = request.POST.get('package')
  html: str = f"Zip Success: {package}"
  return HttpResponse(html)