from django.contrib import admin
from .models import PetType, Profile, Advert, PetRelation

admin.site.register(PetType)
admin.site.register(Profile)
admin.site.register(Advert)
admin.site.register(PetRelation)