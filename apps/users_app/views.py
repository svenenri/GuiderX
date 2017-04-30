from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Traveler
from .models import Guide

def travelers(request):
	return render(request, 'users_app/travelers/travelers.html')

def travelerSignup(request):

	name = request.POST['name'],
	email = request.POST['travelerEmail'],
	phone = request.POST['phone']
	interests = request.POST.getlist('interests')

	info = {
		'name': name,
		'email': email,
		'phone': phone,
		'interests': interests
	}

	added = Traveler.objects.addTraveler(info)
	messages.success(request, added[1])

	request.session['userId'] = added[2]
	return redirect(reverse('users:travelerDashboard'))

def travelerDashboard(request):
	guideMatches = Guide.objects.matchGuides(request.session['userId'])
	for guide in guideMatches:
		guide[0].name = guide[0].name[3:-3]
	matches = {
		'guideMatches': guideMatches
	}
	return render(request, 'users_app/travelers/travelerDashboard.html', matches)

def guides(request):
	return render(request, 'users_app/guides/guides.html')

def guideSignup(request):

	name = request.POST['name'],
	email = request.POST['travelerEmail'],
	phone = request.POST['phone']
	expertise = request.POST.getlist('expertise')

	info = {
		'name': name,
		'email': email,
		'phone': phone,
		'expertise': expertise
	}

	added = Guide.objects.addGuide(info)
	messages.success(request, added[1])
	return redirect(reverse('users:guideDashboard'))

def guideDashboard(request):
	'''
		1. Search for matches based on being selected by Travelers
		2. Order list by last name. (NOTE: List will later be ordered by travel date)
		3. Serve list to frontend
		4. Display list on dashboard
		5. 'Accept' button to initiate call
	'''
	return render(request, 'users_app/guides/guideDashboard.html')
