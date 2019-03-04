from django.shortcuts import render,redirect
from storey.models import *
from storey.forms import *
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.utils import timezone
from mimetypes import guess_type
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse,Http404
import random

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

"""
Storey - MainPage

"""

def home(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'home.html', context)

@login_required
def user_portal(request):
    context = {}
    if request.method == 'GET':
        retailer = Retailer.objects.get(user=request.user)
        shop     = Shop.objects.get(retailer=retailer)
        context['shop_name'] = shop.name
        return render(request, 'user_portal.html', context)

@login_required
def edit_template(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'edit_template.html', context)

@login_required
def edit_footer(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'homepage_footer.html', context)

def get_website(request):
    retailer = Retailer.objects.get(user=request.user)
    shop     = Shop.objects.get(retailer=retailer)
    return Shopwebsite.objects.get(shop=shop)

"""
All edit template method goes here

"""

"""
Edit Teamplate - Homepage Part

"""
@login_required
def editHomepageHeader(request):
    context     = {}
    shopwebsite = get_website(request)
    homepage    = Homepage.objects.get(website=shopwebsite)
    header      = HomepageHeader.objects.get(homepage=homepage)
    navbar      = HomepageNavbar.objects.get(homepage=homepage)
    demo        = HomepageProductDemo.objects.get(homepage=homepage)
    footer      = HomepageFooter.objects.get(homepage=homepage)
    if request.method == 'GET':
        context = {'form': HomepageHeaderForm(instance=header),'footer':footer,'header':header,'demo':demo,'navbar':navbar}
        return render(request, 'homepage_header.html', context)
    else:
        form = HomepageHeaderForm(request.POST,request.FILES, instance=header)
        if not form.is_valid():
            context['form']=form
            return render(request, 'homepage_header.html', context)
        header.save()
        header_info = {
            'header_logo':str(header.logo),
            'header_text':str(header.text),
            }
        header_info = json.dumps(header_info)
        return HttpResponse(header_info, content_type='application/json')

@login_required
def editHomepageDemo(request):
    context     = {}
    shopwebsite = get_website(request)
    homepage    = Homepage.objects.get(website=shopwebsite)
    navbar      = HomepageNavbar.objects.get(homepage=homepage)
    header      = HomepageHeader.objects.get(homepage=homepage)
    demo        = HomepageProductDemo.objects.get(homepage=homepage)
    footer      = HomepageFooter.objects.get(homepage=homepage)
    if request.method == 'GET':
        demo_form = HomepageProductDemoForm(instance=demo)
        context   = {'header':header,'demo_form':demo_form,'footer':footer,'demo':demo,'navbar':navbar}
        return render(request, 'homepage_demo.html', context)
    elif request.method == 'POST':
        demo_form = HomepageProductDemoForm(request.POST, request.FILES, instance=demo)
        if not demo_form.is_valid():
            context['demo_form'] = demo_form
            return render(request, 'homepage_demo.html', context)
        else:
            demo_form.save()
            demo.save()
            response = {
                'name_1'        : str(demo.name_1),
                'description_1' : str(demo.description_1),
                'name_2'        : str(demo.name_2),
                'description_2' : str(demo.description_2),
                'demo_pic_1'    : str(demo.picture_1),
                'demo_pic_2'    : str(demo.picture_2),
                }
            response = json.dumps(response)
            return HttpResponse(response, content_type='application/json')

@login_required
def editHomepageNavbar(request):
    context = {}
    shopwebsite = get_website(request)
    homepage    = Homepage.objects.get(website=shopwebsite)
    navbar      = HomepageNavbar.objects.get(homepage=homepage)
    header      = HomepageHeader.objects.get(homepage=homepage)
    demo        = HomepageProductDemo.objects.get(homepage=homepage)    
    footer      = HomepageFooter.objects.get(homepage=homepage)
    if request.method == 'GET':
        context = {'form': HomepageNavbarForm(instance=navbar),'footer':footer,'navbar':navbar,'header':header,'demo':demo,}
        return render(request, 'homepage_navbar.html', context)
    else:
        form = HomepageNavbarForm(request.POST,request.FILES, instance=navbar)
        if not form.is_valid():
            context['form']=form
            return render(request, 'homepage_navbar.html', context)
        navbar.save()
        navbar_info = {
            'navbar_logo':str(navbar.logo),
            'navbar_text':str(navbar.text),
            'navbar_height':navbar.logo_height,
            'navbar_width':navbar.logo_width,
            }
        navbar_info = json.dumps(navbar_info)
        return HttpResponse(navbar_info, content_type='application/json')

@login_required
def editHomepageFooter(request):
    context = {}
    shopwebsite = get_website(request)
    homepage    = Homepage.objects.get(website=shopwebsite)
    header      = HomepageHeader.objects.get(homepage=homepage)
    navbar      = HomepageNavbar.objects.get(homepage=homepage)
    demo        = HomepageProductDemo.objects.get(homepage=homepage)
    footer      = HomepageFooter.objects.get(homepage=homepage)
    if request.method == 'GET':
        context = {'footer_form': HomepageFooterForm(instance=footer),'footer':footer,'header':header,'demo':demo,'navbar':navbar}
        return render(request, 'homepage_footer.html', context)
    footer_form = HomepageFooterForm(request.POST, instance=footer)
    if not footer_form.is_valid():
        context['footer_form'] = footer_form
        return render(request, 'homepage_footer.html', context)
    footer_form.save()
    footer_info = {
            'footer_Shopname':str(footer.Shopname),
            'footer_Company' :str(footer.Company),
            }
    footer_info = json.dumps(footer_info)
    return HttpResponse(footer_info, content_type='application/json')


"""
Edit Teamplate - ProductPage Part

"""
@login_required
def editCollectionpageAllignment(request):
    context = {}
    retailer    = Retailer.objects.get(user=request.user)
    shop        = Shop.objects.get(retailer=retailer)
    shopwebsite = Shopwebsite.objects.get(shop=shop)
    allignment  = CollectionpageAllignment.objects.get(website=shopwebsite)
    if request.method == 'GET':
        context = {'form': CollectionpageAllignmentForm(instance=allignment)}
        return render(request, 'product_demo.html', context)

    form = CollectionpageAllignmentForm(request.POST, instance=allignment)
    context['form'] = form
    context['allignment'] = allignment
    if not form.is_valid():
        return render(request, 'json/collectionpage_allignment.json', context, content_type='application/json')
    
    form.save()
    allignment.row = request.POST['row']
    #allignment.col = request.POST['col']
    allignment.sorting = request.POST['sorting']
    allignment.filtering = request.POST['filtering']
    return render(request, 'json/collectionpage_allignment.json', context, content_type='application/json')

@login_required
def editCollectionpageDetail(request):
    context = {}
    retailer    = Retailer.objects.get(user=request.user)
    shop        = Shop.objects.get(retailer=retailer)
    shopwebsite = Shopwebsite.objects.get(shop=shop)
    detail  = CollectionpageDetail.objects.get(website=shopwebsite)
    if request.method == 'GET':
        context = {'form': CollectionpageDetailForm(instance=detail)}
        return render(request, 'product_detail.html', context)

    form = CollectionpageDetailForm(request.POST, instance=detail)
    context['form'] = form
    context['detail'] = detail
    if not form.is_valid():
        return render(request, 'json/collectionpage_detail.json', context, content_type='application/json')
    
    detail.commenting = request.POST['commenting']
    return render(request, 'json/collectionpage_detail.json', context, content_type='application/json')

@login_required
def editProductPage(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'product_demo.html', context)

@login_required
def editProductDetail(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'product_detail.html', context)

@login_required
def manageProductCategory(request):
    context = {}
    if request.method == 'GET':
        category_list = Product.objects.values_list('category', flat = True)
        context['category_list'] = set(category_list)
        retailer = Retailer.objects.get(user=request.user)
        shop     = Shop.objects.get(retailer=retailer)
        context['shop_name'] = shop.name

        return render(request, 'manage_product_category.html', context)

@login_required
def view_category(request):
    context = {}
    if request.method == 'GET':
        product_list = Product.objects.filter(category = request.GET['category'])
        product_list = product_list[::-1]
        context['product_list'] = product_list
        return render(request, 'view_category.html', context)

@login_required
def manageProductList(request):
    context = {}
    if request.method == 'GET':
        retailer = Retailer.objects.get(user = request.user)
        shop = Shop.objects.get(retailer = retailer)
        product_list = Product.objects.filter(shop_name=shop.name)
        product_list = product_list[::-1]
        context['product_list'] = product_list
        context['shop_name'] = shop.name
        return render(request, 'manage_product_list.html', context)

@login_required
def addProduct(request):
    context = {}
    if request.method == 'GET':
        context['form'] = AddProductForm()
        retailer = Retailer.objects.get(user = request.user)
        shop = Shop.objects.get(retailer = retailer)
        context['shop_name'] = shop.name
        return render(request, 'add_product.html', context)

@login_required
def create_product(request):
    context = {}
    retailer = Retailer.objects.get(user = request.user)
    shop = Shop.objects.get(retailer = retailer)
    data = Product.objects.create(shop_name=shop.name,name = request.POST['name'])
    data.save()
    form = AddProductForm(request.POST, request.FILES, instance = data)
    if not form.is_valid():
        context['form'] = form
        return render(request, 'add_product.html', context)
    form.save()
    return redirect('manageProductList')

@login_required
def edit_product(request):
    context = {}
    data = Product.objects.get(id = request.GET['id'])
    if request.method == 'GET':
        context['form'] = EditProductForm(instance = data)
        context['product'] = data
        return render(request, 'edit_product.html', context)

@login_required
def delete_product(request):
    context = {}
    if request.method == 'GET':
        data = Product.objects.get(id = request.GET['id'])
        print(data)
        data.delete()
    product_list = Product.objects.all()
    product_list = product_list[::-1]
    context['product_list'] = product_list
    return render(request, 'manage_product_list.html', context)

@login_required
def update_product(request,id):
    context = {}
    data = get_object_or_404(Product, id = id)
    if not data:
        raise Http404
    form = EditProductForm(request.POST, request.FILES, instance = data)
    if not form.is_valid():
        context['form'] = form
        return render(request, 'edit_product.html', context)
    form.save()
    return redirect('manageProductList')


def get_picture(request,id):
    product = get_object_or_404(Product, id = id)
    if not product.picture:
        raise Http404
    content_type = guess_type(product.picture.name)
    return HttpResponse(product.picture, content_type=content_type)

"""
Functions about order overview and detail
"""

@login_required
def orderOverview(request):
    context = {}
    if request.method == 'GET':
        user = request.user
        retailer = Retailer.objects.get(user = user)
        shop = Shop.objects.get(retailer = retailer)
        order_list = Order.objects.filter(shop = shop).filter(isCurrentOrder=False)
        for order in order_list:
            if not order.ship_status:
                context['ship_status'] = 'ship'
            else:
                context['ship_status'] = 'shipped'
        context['order_list'] = order_list
        context['shop_name'] = shop.name
        return render(request, 'order_overview.html', context)

@login_required
def ship(request, order_id):
    context = {}
    if request.method == 'GET':
        order = Order.objects.get(id = order_id)
        user = request.user
        retailer = Retailer.objects.get(user = user)
        shop = Shop.objects.get(retailer = retailer)
        context['shop_name'] = shop.name
        order_list = Order.objects.filter(shop = shop).filter(isCurrentOrder=False)
        context['order_list'] = order_list
        if not order.ship_status:
            order.ship_status = True
            order.save()
            context['ship_status'] = 'shipped'
        else:
            order.ship_status = False
            order.save()
            context['ship_status'] = 'ship'
    return render(request, 'order_overview.html', context)

@login_required
def orderDetail(request):
    context = {}
    order = Order.objects.get(id = request.GET['id'])
    user = request.user
    retailer = Retailer.objects.get(user = user)
    shop = Shop.objects.get(retailer = retailer)
    items = Item.objects.filter(order = order)
    if request.method == 'GET':
        context['order'] = order
        context['items'] = items
        context['shop_name'] = shop.name
    return render(request, 'order_detail.html', context)

@login_required
def editShoppingCart(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'shopping_cart.html', context)

@login_required
def shopShoppingCart(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'shop_shopping_cart.html', context)



"""
Shopwebsite

"""
def shopHomepage(request,shop_name):
    context = {}
    if request.method == 'GET':
        context = {}
        view_name   = request.user.username 
        shop        = Shop.objects.get(name=shop_name)
        shop_owner  = shop.retailer.username
        shopwebsite = Shopwebsite.objects.get(shop=shop)
        homepage    = Homepage.objects.get(website=shopwebsite)
        header      = HomepageHeader.objects.get(homepage=homepage)
        demo        = HomepageProductDemo.objects.get(homepage=homepage)
        navbar      = HomepageNavbar.objects.get(homepage=homepage)
        footer      = HomepageFooter.objects.get(homepage=homepage)
        order       = Order(shop=shop)
        order.placedDate=timezone.now()
        order.save()
        context = {'header':header,'demo':demo,'navbar':navbar,'footer':footer,'shop_name':shop_name,'shop_owner':shop_owner,'view_name':view_name,'order_id': order.id}
        return render(request, 'shop_homepage.html', context)

def make_view_shoplist(request, shop_name, order_id, product_list):
    context  = {}
    view_name   = request.user.username
    shop        = Shop.objects.get(name=shop_name)
    shop_owner  = shop.retailer.username
    website     = Shopwebsite.objects.get(shop=shop)
    homepage    = Homepage.objects.get(website=website)
    navbar      = HomepageNavbar.objects.get(homepage=homepage)
    footer      = HomepageFooter.objects.get(homepage=homepage)
    cpa         = CollectionpageAllignment.objects.get(website=website) 
    row         = cpa.row
    sorting     = cpa.sorting
    paginator   = Paginator(product_list, row * 3) # Show 3*row products per page
    page        = request.GET.get('page')
    products    = paginator.get_page(page)
    return render(request, 'shop_collection_list.html', {'navbar':navbar,'footer':footer,'products': products, 'sorting': sorting,'shop_owner':shop_owner,'view_name':view_name,'order_id': order_id, 'shop_name':shop_name})

def shopCollectionList(request, shop_name, order_id):
    product_list = Product.objects.filter(shop_name=shop_name)
    return make_view_shoplist(request, shop_name, order_id, product_list)

def shopProductDetail(request, shop_name, order_id, id):
    product = Product.objects.get(id=id)
    context = {}
    view_name   = request.user.username
    shop        = Shop.objects.get(name=shop_name)
    shop_owner  = shop.retailer.username
    website = Shopwebsite.objects.get(shop=shop)
    homepage    = Homepage.objects.get(website=website)
    navbar      = HomepageNavbar.objects.get(homepage=homepage)
    footer      = HomepageFooter.objects.get(homepage=homepage)
    cpd = CollectionpageDetail.objects.get(website=website)
    commenting = cpd.commenting
    return render(request, 'shop_product_detail.html', {'navbar':navbar,'footer':footer,'product': product,'shop_owner':shop_owner,'view_name':view_name, 'order_id':order_id, 'commenting': commenting, 'shop_name':shop_name})

def sortByPriceHL(request, shop_name, order_id):
    product_list = Product.objects.filter(shop_name=shop_name).order_by('-price', '-pk')
    return make_view_shoplist(request, shop_name, order_id, product_list)

def sortByPriceLW(request, shop_name, order_id):
    product_list = Product.objects.filter(shop_name=shop_name).order_by('price', 'pk')
    return make_view_shoplist(request, shop_name, order_id, product_list)

def sortByAvailability(request, shop_name, order_id):
    product_list = Product.objects.filter(shop_name=shop_name).order_by('quantity', 'pk')
    return make_view_shoplist(request, shop_name, order_id, product_list)

def addToShoppingCart(request, shop_name, order_id, product_id):
    order = Order.objects.get(id=order_id)
    product = Product.objects.get(id=product_id)
    item = Item(product=product, order=order)
    item.save()
    return shopCollectionList(request, shop_name, order_id)

def deleteFromShoppingCart(request, shop_name, order_id, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return viewShoppingCart(request, shop_name, order_id)

def viewShoppingCart(request, shop_name, order_id):
    order = Order.objects.get(id=order_id)
    context = {}
    items = Item.objects.filter(order=order)
    context['order_id'] = order_id
    context['shop_name'] = shop_name
    context['items'] = items
    context['total_price'] = order.get_totalPrice()
    return render(request,'shop_shopping_cart.html',context)

def placeOrder(request, shop_name, order_id):
    order = Order.objects.get(id=order_id)
    context = {'order_id':order_id}
    order.isCurrentOrder=False
    order.placedDate = timezone.now()
    order.save()
    return redirect('shopwebsite_homepage', shop_name=shop_name)

"""
Register and Log in - Main_website Part

"""
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
        new_myuser=Retailer(user     = new_user,
                            username = new_user.username,
                            email    = register_form.cleaned_data['email'],
                            store    = register_form.cleaned_data['store'])
        # If you wish to activate your account after clicking on the activation link, you should add 
        new_user.is_active=False
        new_user.save()
        new_myuser.save()
        
        # Senging email part 
        token=default_token_generator.make_token(new_user)
        message="""Welcome to Storey.com. Please click the link below to verify your email 
                   address and complete the registeration of your account:
                   http://%s%s
                """ %(request.get_host(),reverse('confirm',args=(new_user.username,token)))
        send_mail(subject='Verify your email address',
                  message=message,
                  from_email='xinzez@andrew.cmu.edu',
                  recipient_list=[new_myuser.email],
                  fail_silently=False,
                 )
        message="An email has been sent to the email you entered when registeration, please click the link to confirm your account"
        context={'message':message}
        return render(request,'register.html',context)
    except Exception as error:
        print(error)
        context['errors']='Invalid operation'
        return render(request,'error.html',{})

def confirm_email(request,username,token):
    context={}
    try:
        user = User.objects.get(username=username)
        retailer                         = Retailer.objects.get(user=user)
        if default_token_generator.check_token(user,token):
            user.is_active = True
            user.save()
            shop                             = Shop(retailer=retailer,name=retailer.store)
            shop.save()
            shopwebsite                      = Shopwebsite(shop=shop)
            shopwebsite.save()
            homepage                         = Homepage(website=shopwebsite)
            homepage.save()
            homepageheader                   = HomepageHeader(homepage=homepage)
            homepageheader.save()
            homepagefooter                   = HomepageFooter(homepage=homepage)
            homepagefooter.save()
            homepagenavbar                   = HomepageNavbar(homepage=homepage)
            homepagenavbar.save()
            homepagedemo                     = HomepageProductDemo(homepage=homepage)
            homepagedemo.save()
            collectionpageallignment         = CollectionpageAllignment(website=shopwebsite)
            collectionpageallignment.save()
            collectionpagedetail             = CollectionpageDetail(website=shopwebsite)
            collectionpagedetail.save()
            login(request,user)
            return redirect(reverse('user_portal'))
    except Exception as error:
        print(error)
        context['']=RegistrationForm()
        return render(request,'register.html',context)

def make_view_shoplist(request, shop_name, order_id, product_list):
    context  = {}
    shop = Shop.objects.filter(name=shop_name).first()
    website = Shopwebsite.objects.get(shop=shop)
    cpa = CollectionpageAllignment.objects.get(website=website) 
    row = cpa.row
    sorting = cpa.sorting
    filtering = cpa.filtering
    paginator = Paginator(product_list, row * 3) # Show 3*row products per page

    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'shop_collection_list.html', {'products': products, 'sorting': sorting, 'filtering':filtering, 'order_id': order_id, 'shop_name':shop_name})

def shopCollectionList(request, shop_name, order_id):
    product_list = Product.objects.filter(shop_name=shop_name)
    return make_view_shoplist(request, shop_name, order_id, product_list)

def shopProductDetail(request, shop_name, order_id, id):
    product = Product.objects.get(id=id)
    context = {}
    shop = Shop.objects.filter(name=shop_name).first()
    website = Shopwebsite.objects.get(shop=shop)
    cpd = CollectionpageDetail.objects.get(website=website)
    commenting = cpd.commenting
    return render(request, 'shop_product_detail.html', {'product': product, 'order_id':order_id, 'commenting': commenting, 'shop_name':shop_name})

def sortByPriceHL(request, shop_name, order_id):
    product_list = Product.objects.filter(shop_name=shop_name).order_by('-price', '-pk')
    return make_view_shoplist(request, shop_name, order_id, product_list)

def sortByPriceLW(request, shop_name, order_id):
    product_list = Product.objects.filter(shop_name=shop_name).order_by('price', 'pk')
    return make_view_shoplist(request, shop_name, order_id, product_list)

def filterByCategory(request, shop_name, order_id, category_id):
    product_list = Product.objects.filter(shop_name=shop_name)
    c = int('0' + category_id)
    if c == 0:
        product_list = product_list.filter(category='Man')
    elif c == 1:
        product_list = product_list.filter(category='Woman')
    else:
        product_list = product_list.filter(category='Kids')
    return make_view_shoplist(request, shop_name, order_id, product_list)

def sortByAvailability(request, shop_name, order_id):
    product_list = Product.objects.filter(shop_name=shop_name).order_by('quantity', 'pk')
    return make_view_shoplist(request, shop_name, order_id, product_list)

def addToShoppingCart(request, shop_name, order_id, product_id):
    order = Order.objects.get(id=order_id)
    product = Product.objects.get(id=product_id)
    item = Item(product=product, order=order)
    item.save()
    return shopCollectionList(request, shop_name, order_id)

def deleteFromShoppingCart(request, shop_name, order_id, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return viewShoppingCart(request, shop_name, order_id)

def viewShoppingCart(request, shop_name, order_id):
    order = Order.objects.get(id=order_id)
    context = {}

    items = Item.objects.filter(order=order)
    context['order_id'] = order_id
    context['shop_name'] = shop_name
    context['items'] = items
    context['total_price'] = order.get_totalPrice()
    return render(request,'shop_shopping_cart.html',context)

def placeOrder(request, shop_name, order_id):
    order = Order.objects.get(id=order_id)

    context = {'order_id':order_id}
    order.isCurrentOrder=False
    order.placedDate = timezone.now()
    order.save()
    return redirect('shopwebsite_homepage', shop_name=shop_name)
