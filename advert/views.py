from django.shortcuts import render

from .models import Advert

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

# Giriş sayfası (/login)
def login(request):
    pass

# Kayıt sayfası (/register)
def register(request):
    pass

# Profil sayfası (/user/<username>)
def profile(request, username):
    pass