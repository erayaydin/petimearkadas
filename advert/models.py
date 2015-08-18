from django.db import models
from django.contrib.auth.models import User

class PetType(models.Model):
	name = models.CharField(max_length=255)

class Profile(models.Model):
	user    = models.ForeignKey(User)
	petName = models.CharField(max_length=255)
	petAge  = models.IntegerField()
	petRelation = models.SmallIntegerField()
	petType = models.ForeignKey(PetType)
	petSick = models.BooleanField()

class Advert(models.Model):
	user     = models.ForeignKey(User)
	datetime = models.DateTimeField(auto_now=True)
	message  = models.TextField()