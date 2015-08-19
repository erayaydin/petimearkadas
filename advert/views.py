from django.shortcuts import render

from .models import Advert, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

# İlan listesi (/)
def index(request):

    adverts = Advert.objects.all()
    return render(request, "advert/index.html", {
        "adverts": adverts
    })

# İlan detay sayfası (/advert/<advert_id>)
def show(request, advert_id):

    advert = Advert.objects.get(id=advert_id)
    return render(request, "advert/show.html", {
        "advert": advert
    })

# Kayıt sayfası (/register)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "advert/register.html", {
        'form': form,
    })

# Profil sayfası (/user/<username>)
def profile(request, username):
    user = User.objects.get(username=username)
    profiles = Profile.objects.filter(user=user)
    return render(request, "advert/profile.html", { "user": user, "profiles": profiles })