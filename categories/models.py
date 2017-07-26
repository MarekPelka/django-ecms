from django.db import models

# Create your models here.
class Product(models.Model):
	link = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	order = models.IntegerField(default=0)
	description = models.TextField()
	def __str__(self):
		return self.title
	
class Application(models.Model):
	link = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	order = models.IntegerField(default=0)
	description = models.TextField()
	def __str__(self):
		return self.title
	
class Home(models.Model):
	title = models.CharField(max_length=200)
	order = models.IntegerField(default=0)
	description = models.TextField()
	def __str__(self):
		return self.title

class Contact(models.Model):
	title = models.CharField(max_length=200)
	order = models.IntegerField(default=0)
	description = models.TextField()
	def __str__(self):
		return self.title