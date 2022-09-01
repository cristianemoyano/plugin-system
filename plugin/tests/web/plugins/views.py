import sys
import os
from typing import Any

from django.http import HttpResponse, Http404
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
  package_name:str = ''
  if request.method == 'POST':
        project_id: str = request.POST.get('project_id')
        package_name: str = request.POST.get('package_name')
        package_version: str = request.POST.get('package_version')
        file_name: str = request.POST.get('file_name')
        download_url: str = PackageService.get_download_url(
          project_id=project_id,
          package_name=package_name,
          package_version=package_version,
          file_name=file_name,
        )
        try:
          PackageService.download_package(url=download_url, output_dir='packages/hello')
        except Exception as exc:
          raise Http404(f"Error package: {exc}")
  html: str = f"Download Success: {package_name}"
  return HttpResponse(html)

def upload(request) -> HttpResponse:
  package_name:str = ''
  if request.method == 'POST':
        project_id: str = request.POST.get('project_id')
        package_name: str = request.POST.get('package_name')
        package_version: str = request.POST.get('package_version')
        file_name: str = request.POST.get('file_name')
        upload_url: str = PackageService.get_upload_url(
          project_id=project_id,
          package_name=package_name,
          package_version=package_version,
          file_name=file_name,
        )
        try:
          PackageService.upload_package(url=upload_url, path_file=f'{package_name}.zip')
        except Exception as exc:
          raise Http404(f"Error package: {exc}")
  html: str = f"Upload Success: {package_name}"
  return HttpResponse(html)

def zip(request) -> HttpResponse:
  package: str = ''
  if request.method == 'POST':
        package: str = request.POST.get('package')
        try:
          PackageService.zip_package(package, f'packages/{package}')
        except Exception as exc:
          raise Http404(f"Error: {exc}")
  html: str = f"Zip Success: {package}"
  return HttpResponse(html)