from django.conf.urls import url, include
from . import views

urlpatterns = [

	url(r'^guides/dashboard$', views.guideDashboard, name='guideDashboard'),
	url(r'^guides/signup$', views.guideSignup, name='guideSignup'),
	url(r'^guides$', views.guides, name='guides'),

	url(r'^travelers/dashboard$', views.travelerDashboard, name='travelerDashboard'),
	url(r'^travelers/signup$', views.travelerSignup, name='travelerSignup'),
	url(r'^$', views.travelers, name='travelers'),

]
