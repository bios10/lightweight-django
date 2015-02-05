import os
import sys

from django.conf import settings
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', '#l2jhgy9&-*pp2)jn1re3ld^f##p-(1w!95g^j-q$ts(25i308')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


def placeholder(request, width, height):
    # TODO: Rest of the view will go here
    return HttpResponse('Ok')


def index(request):
    return HttpResponse('Hello World!')

urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
    url(r'^$', index),
)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)