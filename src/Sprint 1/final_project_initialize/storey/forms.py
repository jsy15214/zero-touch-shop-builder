from django import forms
from django.forms import ModelForm

from storey.models import *

class HomepageHeaderForm(forms.ModelForm):
	class Meta:
		model = HomepageHeader
		exclude = ('homepage',)
		widgets = {'isVisible':forms.CheckboxInput(attrs={'label': 'Delete this section'}),
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
		widgets = {'isVisible':forms.CheckboxInput(attrs={'label': 'Delete this section'}),
            'link_1':forms.TextInput(attrs={'placeholder': 'Link 1'}),
			'link_1_content':forms.TextInput(attrs={'placeholder': 'URL'}),
			'link_2':forms.TextInput(attrs={'placeholder': 'Link 2'}),
			'link_2_content':forms.TextInput(attrs={'placeholder': 'URL'}),
			'promotion':forms.TextInput(attrs={'placeholder': 'Promotion'}),
			'promotion_content':forms.TextInput(attrs={'placeholder': 'URL'}),
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

	storey    = forms.CharField(max_length = 40,
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
