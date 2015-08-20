from django.shortcuts import render

from .models import Advert, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import AdvertCreateForm, PetCreateForm, UserForm

# İlan listesi (/)
def index(request):

    adverts = Advert.objects.all().order_by("-id")
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

def create(request):
    if request.method == 'POST':
        form = AdvertCreateForm(request.user, request.POST)

        if form.is_valid():
            new_advert = form.save()
            return HttpResponseRedirect('/')
    else:
        form = AdvertCreateForm(request.user)
    return render(request, "advert/create.html", {
        'form': form
    })

# Profil sayfası (/user/<username>)
def profile(request, username):
    user = User.objects.get(username=username)
    profiles = Profile.objects.filter(user=user)
    adverts = Advert.objects.filter(profile__user__id=user.id)
    return render(request, "advert/profile.html", { "user": user, "profiles": profiles, "adverts": adverts, "request": request })

def profileEdit(request, username):
    if username == request.user.username:
        if request.method == "POST":
            form = UserForm(request.POST, instance=request.user)
            if form.is_valid():
                user_profile = form.save()
                return HttpResponseRedirect(reverse("adv_profileEdit", args=[request.user.username]))
        else:
            form = UserForm(instance=request.user)
        return render(request, "advert/profileEdit.html", { "form": form })
    else:
        HttpResponseRedirect("/")

def petCreate(request):
    if request.method == 'POST':
        form = PetCreateForm(request.user, request.POST)

        if form.is_valid():
            new_pet = form.save(commit=False)
            new_pet.user = request.user
            if 'petImage' in request.FILES:
                new_pet.petImage = request.FILES["petImage"]
            new_pet.save()
            return HttpResponseRedirect('/')
    else:
        form = PetCreateForm(request.user)
    return render(request, "advert/petcreate.html", {
        'form': form
    })

def petEdit(request, pet_id):
    pet = Profile.objects.get(id=pet_id)
    if request.method == 'POST':
        form = PetCreateForm(request.user, request.POST, instance=pet)

        if form.is_valid():
            new_pet = form.save(commit=False)
            if 'petImage' in request.FILES:
                new_pet.petImage = request.FILES["petImage"]
            new_pet.save()
            return HttpResponseRedirect(reverse('adv_petEdit', args=[new_pet.id]))
    else:
        form = PetCreateForm(request.user, instance=pet)
    return render(request, "advert/petedit.html", {
        'form': form,
        'pet': pet
    })

def passwordChange(request, username):
    pass