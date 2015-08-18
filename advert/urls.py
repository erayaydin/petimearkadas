from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^advert/(?P<advert_id>[0-9]+)$', views.show, name='show'),
    url(r'^user/(?P<username>[A-Za-z0-9\.\-\_]+)$', views.profile, name='profile'),
]