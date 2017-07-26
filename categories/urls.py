from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^home/$', views.home, name='home'),
	#url(r'^contact/$', views.contact, name='contact'),
]
'''
    url(r'^products/$', views.products, name='products_index'),
	url(r'^products/(?P<product_link>[\w\-]+)/$', views.pdetail, name='product_detail'),
	url(r'^applications/$', views.applications, name='applications_index'),
	url(r'^applications/(?P<applications_link>[\w\-]+)/$', views.adetail, name='application_detail'),
'''