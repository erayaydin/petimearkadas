from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='adv_index'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'advert/login.html'}, name="adv_login"),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="adv_logout"),
    url(r'^register$', views.register, name="adv_register"),
    url(r'^pet/create$', views.petCreate, name="adv_petCreate"),
    url(r'^pet/(?P<pet_id>[0-9]+)/edit$', views.petEdit, name='adv_petEdit'),
    url(r'^advert/create$', views.create, name='adv_create'),
    url(r'^advert/(?P<advert_id>[0-9]+)$', views.show, name='adv_show'),
    url(r'^password-change$', 'django.contrib.auth.views.password_change', { 'template_name': 'advert/passwordChange.html', 'post_change_redirect': '/' }, name='adv_passwordChange'),
    url(r'^user/(?P<username>[A-Za-z0-9\.\-\_]+)$', views.profile, name='adv_profile'),
    url(r'^user/(?P<username>[A-Za-z0-9\.\-\_]+)/edit$', views.profileEdit, name='adv_profileEdit'),
]