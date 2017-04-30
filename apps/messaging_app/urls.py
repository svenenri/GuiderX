from django.conf.urls import url, include
from . import views

urlpatterns = [

	url(r'^traveler$', views.toTraveler, name='toTraveler'),
	url(r'^guide/(?P<id>\d+)$', views.toGuide, name='toGuide')

]
