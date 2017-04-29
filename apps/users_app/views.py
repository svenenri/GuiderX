from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Traveler
from .models import Guide

# Create your views here.
def travelers(request):
	return render(request, 'users_app/travelers/travelers.html')

def travelerSignup(request):

	name = request.POST['name'],
	email = request.POST['travelerEmail'],
	location = request.POST['location']
	interests = request.POST['interests']

	info = {
		'name': name,
		'email': email,
		'location': location,
		'interests': interests
	}
	'''
	RESOLVE ERROR AND IMPLEMENT IN GUIDESIGNUP=> EXCEPTION VALUE: expected string or buffer
	'''
	# validate = Traveler.objects.validate(info)
	#
	# if validate:
	# 	for idx in range(len(validate)):
	# 		messages.error(request, validate[idx])
	# 	return redirect(reverse('users:travelerDashboard'))
	# else:
	# 	added = Traveler.objects.addTraveler(info)
	# 	messages.success(request, added[1])
	# 	return redirect(reverse('users:travelerDashboard'))

	added = Traveler.objects.addTraveler(info)
	messages.success(request, added[1])
	return redirect(reverse('users:travelerDashboard'))

def travelerDashboard(request, id):
	'''
		1. Search for matches based on interests/expertise
		2. Order list by highest number of matches
		3. Serve list to frontend
		4. Display list on dashboard
		5. 'Connect/Select' button to initiate call
	'''
	return render(request, 'users_app/travelers/travelerDashboard.html')

def guides(request):
	return render(request, 'users_app/guides/guides.html')

def guideSignup(request):

	name = request.POST['name'],
	email = request.POST['travelerEmail'],
	location = request.POST['location']
	expertise = request.POST['expertise']

	info = {
		'name': name,
		'email': email,
		'location': location,
		'expertise': expertise
	}

	added = Guide.objects.addGuide(info)
	messages.success(request, added[1])
	return redirect(reverse('users:guideDashboard'))

def guideDashboard(request, id):
	'''
		1. Search for matches based on being selected by Travelers
		2. Order list by last name. (NOTE: List will later be ordered by travel date)
		3. Serve list to frontend
		4. Display list on dashboard
		5. 'Accept' button to initiate call
	'''
	return render(request, 'users_app/guides/guideDashboard.html')

'''
IMPLEMENT LOGOUT W/LOGIN REG APP
'''
# def logout(request):
	# If user is a guide, then return to guide landing page
	# else if user is a traveler, then return to the traveler landing page
