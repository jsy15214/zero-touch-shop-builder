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
	text        = models.CharField(max_length=40,default='')
	logo        = models.ImageField(upload_to='storey',default='storey/default-user-image.png', blank=True)

class HomepageNavbar(models.Model):
	homepage    = models.OneToOneField(Homepage,on_delete=models.CASCADE)
	isVisible   = models.BooleanField(default=True)
	text        = models.CharField(max_length=40,default='')
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

class CollectionpageAllignment(models.Model):
	website = models.OneToOneField(Shopwebsite, on_delete=models.CASCADE)
	row = models.IntegerField(default='')
	col = models.IntegerField(default='')
	sorting = models.BooleanField(default=True)
	filtering = models.BooleanField(default=True)

class CollectionpageDetail(models.Model):
	website = models.OneToOneField(Shopwebsite, on_delete=models.CASCADE)
	commenting = models.BooleanField(default=True)


class Product(models.Model):
	name    	= models.CharField(max_length=40)
	price  		= models.CharField(max_length=40, blank= True, default='')
	description = models.CharField(max_length=400, default='')
	CATEGORY_CHOICES = (
	('Man', 'Man'),
	('Woman', 'Woman'),
	('Kids', 'Kids'),
	)
	category = models.CharField(max_length = 40, choices=CATEGORY_CHOICES, default = "man")
	quantity	= models.IntegerField(blank= True, default=1)
	picture     = models.ImageField(upload_to='storey', blank=True, default='')

class ProductDemo(models.Model):
	user      = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	name_1 = models.CharField(max_length=40, default='')
	description_1 = models.CharField(max_length=300, default='')
	picture_1 = models.ImageField(upload_to='storery', blank=True, default='')
	name_2 = models.CharField(max_length=40, default='')
	description_2 = models.CharField(max_length=300, default='')
	picture_2 = models.ImageField(upload_to='storery', blank=True, default='')
