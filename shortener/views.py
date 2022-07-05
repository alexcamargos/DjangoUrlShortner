from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from .models import ShortUUIDModel
from .models import UniformResourceLocator


# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        id = ShortUUIDModel().unique_identifier
        new_link = UniformResourceLocator(url=link, uuid=id)
        new_link.save()

        return HttpResponse(id)


def access_url(request, id):
    url = UniformResourceLocator.objects.get(uuid=id)
    return redirect(url.url)
