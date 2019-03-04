from django.shortcuts import render,redirect
from storey.models import *
from storey.forms import *
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from mimetypes import guess_type
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse,Http404

def home(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'home.html', context)


def register(request):
    context={}
    errors=[]
    context['errors']=errors
    try:
        if request.method =='GET':
        	register_form = RegistrationForm()
        	context['register_form']=register_form
        	return render(request,'register.html',context)
        register_form=RegistrationForm(request.POST)
        if not register_form.is_valid():
            context={'register_form':register_form}
            return render(request, 'register.html', context)

        new_user = User.objects.create_user(username  =register_form.cleaned_data['username'],
                                            password  =register_form.cleaned_data['password'],
                                            email     =register_form.cleaned_data['email'],)
        new_myuser=Retailer(user=new_user,
                            username=new_user.username,
                            email=register_form.cleaned_data['email'],
                            )
        # If you wish to activate your account after clicking on the activation link, you should add 
        new_user.is_active=False
        new_user.save()
        new_myuser.save()
        
        # Senging email part 
        token=default_token_generator.make_token(new_user)
        message="""Welcome to MS&F Club. Please click the link below to verify your email 
                   address and complete the registeration of your account:
                   http:// %s%s
                """ %(request.get_host(),reverse('confirm',args=(new_user.username,token)))
        send_mail(subject='Verify your email address',
                  message=message,
                  from_email='xinzez@andrew.cmu.edu',
                  recipient_list=[new_myuser.email],
                  fail_silently=False,
                 )
        message="An email has been sent to the email you entered when registeration,please click the link to confirm your account"
        context={'message':message}
        return render(request,'register.html',context)
    except Exception as error:
        print(error)
        context['errors']='Invalid operation'
        return render(request,'error.html',{})

def confirm_email(request,username,token):
    context={}
    try:
        user=User.objects.get(username=username)
        print(user)
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            login(request,user)
            return redirect(reverse('user_portal'))
    except Exception as error:
        print(error)
        context['']=RegistrationForm()
        return render(request,'register.html',context)


def get_website(request):
	retailer = Retailer.objects.get(user=request.user)
	shop = Shop.objects.get(retailer=retailer)
	return Shopwebsite.objects.get(shop=shop)

def user_portal(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'user_portal.html', context)

def edit_template(request):
    context = {}
    if request.method == 'GET':
        retailer = Retailer.objects.get(user=request.user)
        if len(Shop.objects.filter(retailer=retailer))<=0:
            shop           = Shop(retailer=retailer)
            shop.save()
            shopwebsite    = Shopwebsite(shop=shop)
            shopwebsite.save()
            homepage       = Homepage(website=shopwebsite)
            homepage.save()
            homepageheader = HomepageHeader(homepage=homepage)
            homepageheader.save()
            homepagefooter = HomepageFooter(homepage=homepage)
            homepagefooter.save()
            homepagenavbar = HomepageNavbar(homepage=homepage)
            homepagenavbar.save()
        return render(request, 'edit_template.html', context)

def edit_footer(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'homepage_footer.html', context)

def get_photo(request,id):
    navbar  = HomepageNavbar.objects.get(id=id)
    if not navbar.logo:
        raise Http404
    content_type = guess_type(navbar.logo.name)
    return HttpResponse(navbar.logo, content_type=content_type)

@login_required
def viewHomepage(request):
	context  = {}
	website  = get_website(request) 
	homepage = Homepage.objects.get(website=website) 
	header   = HomepageHeader.objects.get(homepage=homepage) 
	context['header'] = header
	return render(request, 'storey/edit_template.html', context)


"""

All edit template method goes here
"""

def editHomepageFooter(request):
    context = {}
    retailer    = Retailer.objects.get(user=request.user)
    shop        = Shop.objects.get(retailer=retailer)
    shopwebsite = Shopwebsite.objects.get(shop=shop)
    homepage    = Homepage.objects.get(website=shopwebsite)
    footer      = HomepageFooter.objects.get(homepage=homepage)
    if request.method == 'GET':
    	context = {'form': HomepageFooterForm(instance=footer),'footer':footer}
    	return render(request, 'homepage_footer.html', context)
    context['footer']   = footer
    form = HomepageFooterForm(request.POST,request.FILES, instance=footer)
    if not form.is_valid():
    	context['form'] = form
    	return render(request, 'json/homepage_footer.json', context, content_type='application/json')
    footer.isVisible         = request.POST['isVisible']
    footer.link_1            = request.POST['link_1']
    footer.link_1_content    = request.POST['link_1_content']
    footer.link_2            = request.POST['link_2']
    footer.link_2_content    = request.POST['link_2_content']
    footer.promotion         = request.POST['promotion']
    footer.promotion_content = request.POST['promotion_content']
    return render(request, 'json/homepage_footer.json', context, content_type='application/json')

def editHomepageHeader(request):
    context = {}
    retailer    = Retailer.objects.get(user=request.user)
    shop        = Shop.objects.get(retailer=retailer)
    shopwebsite = Shopwebsite.objects.get(shop=shop)
    homepage    = Homepage.objects.get(website=shopwebsite)
    header      = HomepageHeader.objects.get(homepage=homepage)
    print('Balei')
    context = {'form': HomepageHeaderForm(instance=header),'header':header }
    return render(request, 'homepage_header.html', context)

def editHeaderAjax(request):
    context = {}
    retailer    = Retailer.objects.get(user=request.user)
    shop        = Shop.objects.get(retailer=retailer)
    shopwebsite = Shopwebsite.objects.get(shop=shop)
    homepage    = Homepage.objects.get(website=shopwebsite)
    header      = HomepageHeader.objects.get(homepage=homepage)
    form = HomepageHeaderForm(request.POST,request.FILES, instance=header)
    if not form.is_valid():
        context['form']=form
        print('A')
        return render(request, 'json/homepage_header.json', context, content_type='application/json')
    header.save()
    print(header.logo)
    header_info = {
        'header_logo':str(header.logo),
        'header_text':str(header.text),
        }
    print('B')
    header_info = json.dumps(header_info)
    print(header_info)
    return HttpResponse(header_info, content_type='application/json')

def editHomepageNavbar(request):
    context = {}
    retailer    = Retailer.objects.get(user=request.user)
    shop        = Shop.objects.get(retailer=retailer)
    shopwebsite = Shopwebsite.objects.get(shop=shop)
    homepage    = Homepage.objects.get(website=shopwebsite)
    navbar      = HomepageNavbar.objects.get(homepage=homepage)
    print('Balei')
    context = {'form': HomepageNavbarForm(instance=navbar),'navbar':navbar }
    return render(request, 'homepage_navbar.html', context)

def editNavbarAjax(request):
    context = {}
    retailer    = Retailer.objects.get(user=request.user)
    shop        = Shop.objects.get(retailer=retailer)
    shopwebsite = Shopwebsite.objects.get(shop=shop)
    homepage    = Homepage.objects.get(website=shopwebsite)
    navbar      = HomepageNavbar.objects.get(homepage=homepage)
    form = HomepageNavbarForm(request.POST,request.FILES, instance=navbar)
    if not form.is_valid():
        context['form']=form
        print('A')
        return render(request, 'json/homepage_navbar.json', context, content_type='application/json')
    navbar.save()
    print(navbar.logo)
    navbar_info = {
        'navbar_logo':str(navbar.logo),
        'navbar_text':str(navbar.text),
        'navbar_height':navbar.logo_height,
        'navbar_width':navbar.logo_width,
        'current_navbar_id': navbar.id
        }
    print('B')
    navbar_info = json.dumps(navbar_info)
    print(navbar_info)
    return HttpResponse(navbar_info, content_type='application/json')

def editHomepageProductDemo(request):
	context = {}
	if request.method == 'GET':
		return render(request, 'homepage_product_demo.html', {})
	form = HomepageHeaderForm(request.POST,request.FILES, instance=header)
	if not form.is_valid():
		return render(request, 'json/homepage_header.json', context, content_type='application/json')

	form.save()
	return render(request, 'json/homepage_header.json', context, content_type='application/json')

def editHomepageDemo(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'homepage_demo.html', context)

def editProductPage(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'product_demo.html', context)

