from django.urls import path,re_path
from django.conf.urls import url

import storey.views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login', auth_views.LoginView.as_view(template_name='login.html'),name = 'login'),
    url(r'^register', storey.views.register, name ='register'),
	url(r'^user_portal', storey.views.user_portal, name = 'user_portal'),
	url(r'^edit_template', storey.views.edit_template, name = 'edit_template'),
	re_path(r'^photo/(?P<id>[a-zA-Z0-9]+)$', storey.views.get_photo,name='photo'),
	url(r'^confirm/(?P<username>[a-zA-Z0-9]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})', storey.views.confirm_email, name = 'confirm'),
	url(r'^edit_template', storey.views.edit_template, name = 'edit_template'),
	url(r'^viewHomepage', storey.views.viewHomepage, name = 'viewHomepage'),
	url(r'^editHomepageFooter', storey.views.editHomepageFooter, name ='editHomepageFooter'),
	url(r'^editHomepageNavbar', storey.views.editHomepageNavbar, name ='editHomepageNavbar'),
	url(r'^editHomepageHeader', storey.views.editHomepageHeader, name ='editHomepageHeader'),
	url(r'^editHomepageDemo', storey.views.editHomepageDemo, name ='editHomepageDemo'),
	url(r'^editHeader', storey.views.editHeaderAjax, name ='editHomepageHeader_AJAX'),
	url(r'^editNavbar', storey.views.editNavbarAjax, name ='editHomepageNavbar_AJAX'),
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
	url(r'^demo_picture_1/(?P<username>\S+)$', storey.views.get_demo_picture_1, name = 'demo_picture_1'),
	url(r'^demo_picture_2/(?P<username>\S+)$', storey.views.get_demo_picture_2, name = 'demo_picture_2'),
        url(r'^demo_info', storey.views.demo_info, name='demo_info')
	]
