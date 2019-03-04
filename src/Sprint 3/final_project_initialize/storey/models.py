from django.db import models
from django.contrib.auth.models import User


class Retailer(models.Model):
	user      = models.ForeignKey(User, on_delete=models.CASCADE)
	username  = models.CharField(max_length=40)
	firstname = models.CharField(max_length=40)
	lastname  = models.CharField(max_length=40)
	email     = models.EmailField(max_length=40)
	store     = models.CharField(max_length=40,unique=True)

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

class ShopUser(models.Model):
	username  = models.CharField(max_length=40)
	password  = models.CharField(max_length=40)
	
"""
Shop website models
"""

class Homepage(models.Model):
	website = models.OneToOneField(Shopwebsite, on_delete=models.CASCADE)

class HomepageHeader(models.Model):
	homepage    = models.OneToOneField(Homepage,on_delete=models.CASCADE)
	text        = models.CharField(max_length=40,default='Welcome to my website')
	logo        = models.ImageField(upload_to='storey',default='storey/header-default.jpg', blank=True)

class HomepageNavbar(models.Model):
	homepage    = models.OneToOneField(Homepage,on_delete=models.CASCADE)
	text        = models.CharField(max_length=40,default='My Website')
	logo        = models.ImageField(upload_to='storey',default='storey/logo.png', blank=True)
	logo_height = models.IntegerField(default=80)
	logo_width  = models.IntegerField(default=80)

class HomepageProductDemo(models.Model):
	homepage          = models.OneToOneField(Homepage,on_delete=models.CASCADE)
	name_1 	 	  	  = models.CharField(max_length=40, default='Fully Responsive Design')
	description_1     = models.CharField(max_length=300, default="When you use a theme created by Start Bootstrap,\
																 you know that the theme will look great on any device, \
																 whether it's a phone, tablet, or desktop the page will \
																 behave responsively!")
	picture_1 	      = models.ImageField(upload_to='storey', blank=True, default='storey/product_demo_1_default.jpg')
	name_2 		      = models.CharField(max_length=40, default='Updated For Bootstrap4')
	description_2     = models.CharField(max_length=300, default="Newly improved, and full of great utility classes, Bootstrap 4\
																 is leading the way in mobile responsive web development! All of \
																 the themes on Start Bootstrap are now using Bootstrap 4!")
	picture_2 	      = models.ImageField(upload_to='storey', blank=True, default='storey/product_demo_2_default.jpg')	

class HomepageFooter(models.Model):
	homepage          = models.OneToOneField(Homepage,on_delete=models.CASCADE)
	Shopname          = models.CharField(max_length=40,default='Shop Name')
	Company           = models.CharField(max_length=40,default='Company Name')

class CollectionpageAllignment(models.Model):
	website = models.OneToOneField(Shopwebsite, on_delete=models.CASCADE)
	row = models.IntegerField(default='4')
	col = models.IntegerField(default='4')
	sorting = models.BooleanField(default=True)
	filtering = models.BooleanField(default=True)
	
class CollectionpageDetail(models.Model):
	website = models.OneToOneField(Shopwebsite, on_delete=models.CASCADE)
	commenting = models.BooleanField(default=True)


class Product(models.Model):
	shop_name = models.CharField(max_length=40, default='', null=True)
	name    	= models.CharField(max_length=40)
	price  		= models.FloatField(default=1.0)
	description = models.CharField(max_length=400, default='')
	CATEGORY_CHOICES = (
	('Man', 'Man'),
	('Woman', 'Woman'),
	('Kids', 'Kids'),
	)
	category    = models.CharField(max_length = 40, choices=CATEGORY_CHOICES, default = "man")
	quantity	= models.IntegerField(blank= True, default=1)
	picture     = models.ImageField(upload_to='storey', blank=True, default='')



class Order(models.Model):
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE, default=None)
	#customer = models.ForeignKey(ShopUser, on_delete=models.CASCADE, default=None)
	isCurrentOrder = models.BooleanField(default=True)
	placedDate = models.DateTimeField('date placed', default=None, blank = True)
	ship_status = models.BooleanField(default=False, blank=True)

	def get_totalPrice(self):
		items = Item.objects.filter(order=self)
		total = 0
		for item in items:
			total += item.get_totalPrice()
		return total


class Item(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	number = models.IntegerField(blank= True, default=1)

	def get_totalPrice(self):
		return self.product.price * self.number


