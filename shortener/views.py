from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from .models import UniformResourceLocator, RedirectClickCount
from .misc import url_click_processor



# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        user = request.user

        new_link = UniformResourceLocator(url=link, created_by=user)
        new_link.save()

        return HttpResponse(new_link.alias)


def redirect_to_long_url(request, id):
    url = UniformResourceLocator.objects.get(alias=id)

    url_click_processor(request, url)

    return redirect(url.get_url())
