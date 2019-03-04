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
	url(r'^editProductPage', storey.views.editProductPage, name ='editProductPage_AJAX'),
	]
