from django.contrib.auth.models import Permission, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Commodity(models.Model):
	name 		= models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	price  		= models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Group(models.Model):
	inv 		= models.CharField(max_length=100)
	cop 		= models.CharField(max_length=200)
	com  		= models.ForeignKey(Commodity, on_delete=models.CASCADE)
	num			= models.IntegerField(default=0)
	# def __str__(self):
	# 	return "A group buying-initiator:%" %(self.inv)



class Movie(models.Model):
	title   	= models.CharField(max_length=200)
	genre  		= models.CharField(max_length=100)
	movie_logo  = models.FileField() 

	def __str__(self):
		return self.title

class Myrating(models.Model):
	user   	= models.ForeignKey(User,on_delete=models.CASCADE) 
	movie 	= models.ForeignKey(Movie,on_delete=models.CASCADE)
	rating 	= models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])
		