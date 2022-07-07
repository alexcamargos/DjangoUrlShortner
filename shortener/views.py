from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone

from .models import UniformResourceLocator, RedirectClickCount


def get_user_ip_address(request):
    """Returns request's ip address."""

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    
    return ip_address


def url_click_processor(request, url):
    """ Gets or creates a click object and increases its `clicks_count`."""

    # Get the click object for the given url.
    click = RedirectClickCount.objects.get_or_create(link=url,
                                                     clicked_at=timezone.now(),
                                                     ip_address=get_user_ip_address(request))[0]
    # Increase the clicks count.
    click.clicks_count += 1
    click.save()


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


def access_url(request, id):
    url = UniformResourceLocator.objects.get(alias=id)

    url_click_processor(request, url)

    return redirect(url.get_url())
