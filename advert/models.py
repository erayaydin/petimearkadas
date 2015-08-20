from django.db import models
from django.contrib.auth.models import User

class PetType(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class PetRelation(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Profile(models.Model):
	GENDERS = ((False, 'Erkek'),(True, 'Dişi'))
	SICK = ((False, "Sağlıklı"), (True, "Hasta"))

	user    = models.ForeignKey(User)
	petName = models.CharField(max_length=255)
	petAge  = models.IntegerField()
	petRelation = models.ForeignKey(PetRelation)
	petType = models.ForeignKey(PetType)
	petSick = models.BooleanField(default=0, choices=SICK)
	petSex = models.BooleanField(default=0, choices=GENDERS)

	def __str__(self):
		return self.petName

class Advert(models.Model):
	profile  = models.ForeignKey(Profile)
	datetime = models.DateTimeField(auto_now=True)
	message  = models.TextField()

	def __str__(self):
		return self.message