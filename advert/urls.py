from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='adv_index'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'advert/login.html'}, name="adv_login"),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="adv_logout"),
    url(r'^register$', views.register, name="adv_register"),
    url(r'^advert/(?P<advert_id>[0-9]+)$', views.show, name='adv_show'),
    url(r'^user/(?P<username>[A-Za-z0-9\.\-\_]+)$', views.profile, name='adv_profile'),
]