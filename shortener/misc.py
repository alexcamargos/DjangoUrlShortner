from django.utils import timezone

from .models import RedirectClickCount


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