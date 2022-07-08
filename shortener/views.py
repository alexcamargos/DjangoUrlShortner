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

def list_links(request):
    links = UniformResourceLocator.objects.all()
    return render(request, 'list_urls.html', {'links': links})


def redirect_to_long_url(request, alias):
    url = UniformResourceLocator.objects.get(alias=alias)

    url_click_processor(request, url)

    return redirect(url.get_full_url())
