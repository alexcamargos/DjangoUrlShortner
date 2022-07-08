from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('list', views.list_links, name='list'),
    path('<str:alias>', views.redirect_to_long_url, name='redirect')
]
