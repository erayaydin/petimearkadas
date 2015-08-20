from django import forms
from .models import Advert, Profile
from django.conf import settings
from django.contrib.auth.models import User

class AdvertCreateForm(forms.ModelForm):

    def __init__(self,user,*args,**kwargs):
        super (AdvertCreateForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['profile'].queryset = Profile.objects.filter(user=user)

    class Meta:
        model = Advert
        fields = ['profile', 'message']

    def clean(self):
        super(AdvertCreateForm, self).clean()
        form_data = self.cleaned_data
        return form_data

class PetCreateForm(forms.ModelForm):

    def __init__(self,user,*args,**kwargs):
        super (PetCreateForm,self ).__init__(*args,**kwargs) # populates the post

    class Meta:
        model = Profile
        fields = ['petName', 'petAge', 'petRelation', 'petType', 'petSick', 'petSex', 'petImage']

    def clean(self):
        super(PetCreateForm, self).clean()
        form_data = self.cleaned_data
        return form_data

class UserForm (forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','email',)