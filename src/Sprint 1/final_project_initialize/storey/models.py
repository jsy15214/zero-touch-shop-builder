from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Retailer(models.Model):
	user      = models.ForeignKey(User, on_delete=models.CASCADE)
	username  = models.CharField(max_length=40)
	firstname = models.CharField(max_length=40)
	lastname  = models.CharField(max_length=40)
	email     = models.EmailField(max_length=40)
	storename = models.CharField(max_length=40)

	def __unicode__(self):
		return self.firstname+' '+self.lastname

	def __str__(self):
		return self.__unicode__()


class Shop(models.Model):
	retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
	name     = models.CharField(max_length=40,default='my_shop')

class Shopwebsite(models.Model):
	shop  = models.OneToOneField(Shop, on_delete=models.CASCADE)
	url   = models.CharField(max_length=40,default='my_shop')
	theme = models.IntegerField(default = 1)

"""
Shop website models
"""

class Homepage(models.Model):
	website = models.OneToOneField(Shopwebsite, on_delete=models.CASCADE)

class HomepageHeader(models.Model):
	homepage    = models.OneToOneField(Homepage,on_delete=models.CASCADE)
	isVisible   = models.BooleanField(default=True)
	text        = models.CharField(max_length=40,default='This is a homepage header')
	logo        = models.ImageField(upload_to='storey',default='storey/default-user-image.png', blank=True)

class HomepageNavbar(models.Model):
	homepage    = models.OneToOneField(Homepage,on_delete=models.CASCADE)
	isVisible   = models.BooleanField(default=True)
	text        = models.CharField(max_length=40,default='This is a homepage navbar')
	logo        = models.ImageField(upload_to='storey',default='storey/default-user-image.png', blank=True)
	logo_height = models.IntegerField(default=40)
	logo_width  = models.IntegerField(default=40)

class HomepageFooter(models.Model):
	homepage          = models.OneToOneField(Homepage,on_delete=models.CASCADE)
	isVisible         = models.BooleanField(default=True)
	link_1            = models.CharField(max_length=40,default='')
	link_1_content    = models.CharField(max_length=40,default='')
	link_2            = models.CharField(max_length=40,default='')
	link_2_content    = models.CharField(max_length=40,default='')
	promotion         = models.CharField(max_length=40,default='')
	promotion_content = models.CharField(max_length=40,default='')