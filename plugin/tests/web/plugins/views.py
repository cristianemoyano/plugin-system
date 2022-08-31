from typing import Any
from django.http import HttpResponse
from django.template import loader
from .models import Plugins

def index(request) -> HttpResponse:
  plugins: Any = Plugins.objects.all().values()
  template: Any = loader.get_template('index.html')
  context: dict[str, Any] = {
    'plugins': plugins,
  }
  return HttpResponse(template.render(context, request))
