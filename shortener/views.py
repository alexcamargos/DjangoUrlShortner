from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from .models import UniformResourceLocator


# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        new_link = UniformResourceLocator(url=link)
        new_link.save()

        return HttpResponse(new_link.alias)


def access_url(request, id):
    url = UniformResourceLocator.objects.get(alias=id)
    return redirect(url.get_url())
