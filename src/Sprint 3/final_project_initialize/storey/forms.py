from django import forms
from django.forms import ModelForm

from storey.models import *

class HomepageHeaderForm(forms.ModelForm):
	class Meta:
		model = HomepageHeader
		exclude = ('homepage','isVisible')
		widgets = {
            'text':forms.TextInput(attrs={'placeholder': 'Short Description'}),
            'logo':forms.FileInput(),
            }

class HomepageNavbarForm(forms.ModelForm):
	class Meta:
		model = HomepageNavbar
		exclude = ('homepage',)
		widgets = {'isVisible':forms.CheckboxInput(attrs={'label': 'Delete this section'}),
            'text':forms.TextInput(attrs={'placeholder': 'Short Description'}),
            'logo':forms.FileInput(),
            'logo_height':forms.TextInput(attrs={'type':'number', 'min':10,'max':100,'placeholder':'logo height'}),
            'logo_width':forms.TextInput(attrs={'type':'number', 'min':10,'max':100,'placeholder':'logo width'}),
            }

class HomepageFooterForm(forms.ModelForm):
	class Meta:
		model = HomepageFooter
		exclude = ('homepage',)
		widgets = {
            'Shopname':forms.TextInput(attrs={'placeholder': 'Input Shopname'}),
			'Company' :forms.TextInput(attrs={'placeholder': 'Input Company name'}),
            }

class HomepageProductDemoForm(forms.ModelForm):
        class Meta:
            model = HomepageProductDemo
            exclude = {'homepage','isVisible'}
            widgets = {
            'picture_1':forms.FileInput(),
            'picture_2':forms.FileInput(),
            }

class CollectionpageAllignmentForm(forms.ModelForm):
	class Meta:
		model = CollectionpageAllignment
		exclude = ('website','col',)
		widgets = {'row': forms.TextInput(attrs={'type':'number', 'min':1,'max':8,'placeholder':'Number of rows per page'}),
		'col': forms.TextInput(attrs={'type':'number', 'min':3,'max':10,'placeholder':'Number of columns per row'}),
		'sorting': forms.CheckboxInput(attrs={'label': 'Enable sorting'}),
		'filtering': forms.CheckboxInput(attrs={'label': 'Enable filtering'}),
		}

class CollectionpageDetailForm(forms.ModelForm):
	class Meta:
		model = CollectionpageDetail
		exclude = ('website',)
		widgets = {
		'commenting': forms.CheckboxInput(attrs={'label': 'Display Comments'}),
		}
		
class RegistrationForm(forms.Form):
	username  = forms.CharField(max_length = 40)
	firstname = forms.CharField(max_length = 40)
	lastname  = forms.CharField(max_length = 40)
	email     = forms.EmailField()	
	password  = forms.CharField(max_length = 40,
                                label='Password',
                                widget = forms.PasswordInput())
	cpassword = forms.CharField(max_length = 40,
                                label='Confirm password',
                                widget = forms.PasswordInput())

	store     = forms.CharField(max_length = 40,
	                         	label='Your store name',)

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		password  = cleaned_data.get('password')
		cpassword = cleaned_data.get('cpassword')
		if password != cpassword:
			raise forms.ValidationError("Passwords did not match.")
		return cleaned_data

	def clean_username(self):
		username=self.cleaned_data.get('username')
		if User.objects.filter(username__exact=username):
			raise forms.ValidationError("Username is already taken.")
		return username 

	def clean_email(self):
		email=self.cleaned_data.get('email')
		if User.objects.filter(email__exact=email):
			raise forms.ValidationError("This email is already taken.")
		return email

	def clean_store(self):
		store=self.cleaned_data.get('store')
		if Retailer.objects.filter(store__exact=store):
			raise forms.ValidationError("This store name is already taken.")
		return store

class ShopwebsiteLoginForm(forms.Form):
	username  	   = forms.CharField(max_length = 40)
	password_input = forms.CharField(max_length = 40,
                                	 label      = 'Password',
                               	     widget 	= forms.PasswordInput())
	def clean(self):
		cleaned_data 	= super(ShopwebsiteLoginForm, self).clean()
		username        = cleaned_data.get('username')
		password_input  = cleaned_data.get('password_input')
		user     		= ShopUser.objects.get(username__exact=username)
		password 		= user.password
		if password != password_input:
			raise forms.ValidationError("Passwords did not match.")
		return cleaned_data

class ShopwebsiteRegistrationForm(forms.Form):
	username  = forms.CharField(max_length = 40)
	password  = forms.CharField(max_length = 40,
                                label='Password',
                                widget = forms.PasswordInput())
	cpassword = forms.CharField(max_length = 40,
                                label='Confirm password',
                                widget = forms.PasswordInput())

	def clean(self):
		cleaned_data = super(ShopwebsiteRegistrationForm, self).clean()
		password  = cleaned_data.get('password')
		cpassword = cleaned_data.get('cpassword')
		if password != cpassword:
			raise forms.ValidationError("Passwords did not match.")
		return cleaned_data

	def clean_username(self):
		username=self.cleaned_data.get('username')
		if User.objects.filter(username__exact=username):
			raise forms.ValidationError("Username is already taken.")
		return username

class AddProductForm(forms.ModelForm):
	class Meta:
		model = Product
		exclude = ('ID','shop_name')
		widgets = {
		'picture':forms.FileInput(),
		}
	def clean(self):
		cleaned_data = super(AddProductForm, self).clean()
		price = cleaned_data.get('price')
		if price <= 0.0:
			raise forms.ValidationError("Please enter a valid price.")
		return cleaned_data
	


class EditProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['id','name','price','description','category','quantity','picture']
		widgets = {
		'picture':forms.FileInput(),
		'id':forms.HiddenInput()
		}
	def clean(self):
		cleaned_data = super(EditProductForm, self).clean()
		price = cleaned_data.get('price')
		if price <= 0.0:
			raise forms.ValidationError("Please enter a valid price.")
		return cleaned_data

