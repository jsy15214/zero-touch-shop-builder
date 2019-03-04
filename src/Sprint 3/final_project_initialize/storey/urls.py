from django.urls import path,re_path
from django.conf.urls import url

import storey.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login', auth_views.LoginView.as_view(template_name='login.html'),name = 'login'),
    url(r'^register', storey.views.register, name ='register'),
    url(r'^shopwebsite_homepage/(?P<shop_name>[a-zA-Z0-9]+)', storey.views.shopHomepage,name = 'shopwebsite_homepage'),
    # url(r'^shopwebsite_login', storey.views.shopwebsite_login,name = 'shopwebsite_login'),
    # url(r'^shopwebsite_register',storey.views.shopwebsite_register, name ='shopwebsite_register'),
	url(r'^user_portal', storey.views.user_portal, name = 'user_portal'),
	url(r'^edit_template', storey.views.edit_template, name = 'edit_template'),
	url(r'^confirm/(?P<username>[a-zA-Z0-9]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})', storey.views.confirm_email, name = 'confirm'),
	url(r'^edit_template', storey.views.edit_template, name = 'edit_template'),
	url(r'^editHomepageFooter', storey.views.editHomepageFooter, name ='editHomepageFooter'),
	url(r'^editHomepageNavbar', storey.views.editHomepageNavbar, name ='editHomepageNavbar'),
	url(r'^editHomepageHeader', storey.views.editHomepageHeader, name ='editHomepageHeader'),
	url(r'^editHomepageDemo', storey.views.editHomepageDemo, name ='editHomepageDemo'),
	url(r'^editCollectionpageAllignment', storey.views.editCollectionpageAllignment, name ='editCollectionpageAllignment'),
	url(r'^editCollectionpageDetail', storey.views.editCollectionpageDetail, name ='editCollectionpageDetail'),
	url(r'^editProductPage', storey.views.editProductPage, name ='editProductPage'),
	url(r'^editProductDetail', storey.views.editProductDetail, name ='editProductDetail'),
	url(r'^manageProductCategory', storey.views.manageProductCategory, name ='manageProductCategory'),
	url(r'^manageProductList', storey.views.manageProductList, name ='manageProductList'),
	url(r'^view_category', storey.views.view_category, name ='view_category'),
	url(r'^editShoppingCart', storey.views.editShoppingCart, name ='editShoppingCart'),
	url(r'^addProduct', storey.views.addProduct, name ='addProduct'),
	url(r'^createProduct', storey.views.create_product, name ='create_product'),
	url(r'^picture/(?P<id>\S+)$', storey.views.get_picture, name = 'picture'),
	url(r'^edit_product', storey.views.edit_product, name ='edit_product'),
	url(r'^delete_product', storey.views.delete_product, name ='delete_product'),
	url(r'^update_product/(?P<id>\S+)$', storey.views.update_product, name ='update_product'),
    url(r'^shopShoppingCart', storey.views.shopShoppingCart, name='shopShoppingCart'),
    url(r'^shopCollectionList/(?P<shop_name>[a-zA-Z0-9]+)/(?P<order_id>\S+)$', storey.views.shopCollectionList, name='shopCollectionList'),
    url(r'^shopProductDetail/(?P<shop_name>[a-zA-Z0-9]+)/(?P<order_id>\S+)/(?P<id>\S+)$', storey.views.shopProductDetail, name='shopProductDetail'),
    url(r'^sortByPriceHL/(?P<shop_name>[a-zA-Z0-9]+)/(?P<order_id>\S+)$', storey.views.sortByPriceHL, name='sortByPriceHL'),
    url(r'^sortByPriceLW/(?P<shop_name>[a-zA-Z0-9]+)/(?P<order_id>\S+)$', storey.views.sortByPriceLW, name='sortByPriceLW'),
    url(r'^sortByAvailability/(?P<shop_name>[a-zA-Z0-9]+)/(?P<order_id>\S+)$', storey.views.sortByAvailability, name='sortByAvailability'),
    url(r'^filterByCategory/(?P<shop_name>[a-zA-Z0-9]+)/(?P<order_id>\S+)/(?P<category_id>\S+)$', storey.views.filterByCategory, name='filterByCategory'),
    url(r'^addToShoppingCart/(?P<shop_name>[a-zA-Z0-9]+)/(?P<order_id>\S+)/(?P<product_id>\S+)$', storey.views.addToShoppingCart, name='addToShoppingCart'),
    url(r'^deleteFromShoppingCart/(?P<shop_name>[a-zA-Z0-9]+)/(?P<order_id>\S+)/(?P<item_id>\S+)$', storey.views.deleteFromShoppingCart, name='deleteFromShoppingCart'),
    url(r'^viewShoppingCart/(?P<shop_name>[a-zA-Z0-9]+)/(?P<order_id>\S+)$', storey.views.viewShoppingCart, name='viewShoppingCart'),
    url(r'^placeOrder/(?P<shop_name>[a-zA-Z0-9]+)/(?P<order_id>\S+)$', storey.views.placeOrder, name='placeOrder'),
    url(r'^orderOverview', storey.views.orderOverview, name='orderOverview'),
    url(r'^orderDetail', storey.views.orderDetail, name='orderDetail'),
    url(r'^ship/(?P<order_id>\S+)$', storey.views.ship, name='ship')
	]
	
