from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..users_app.models import Guide, Traveler
from time import sleep
import nexmo
import urllib
import urllib2
import json

def toGuide(request, id):

	matchedGuide = Guide.objects.filter(id=id)

	api_key = 'add_key'

	api_secret = 'add_secret'

	client = nexmo.Client(key=api_key, secret=api_secret)

	response = client.send_message({'from': '12028388322', 'to': '1' + str(matchedGuide[0].phone), 'text': 'A new Traveler has chosen you as their Guide!'})

	response = response['messages'][0]

	if response['status'] == '0':
		print 'Sent message', response['message-id']

		print 'Remaining balance is', response['remaining-balance']
	else:
		print 'Error:', response['error-text']

	sleep(2.00)

	return redirect(reverse('messages:toTraveler'))

def toTraveler(request):

	traveler = Traveler.objects.filter(id = request.session['userId'])

	api_key = 'add_key'

	api_secret = 'add_secret'

	client = nexmo.Client(key=api_key, secret=api_secret)

	response = client.send_message({'from': '12028388322', 'to': '1' + str(traveler[0].phone), 'text': 'Your guide has been contacted. They will reach out to you to start planning your itenerary!'})

	response = response['messages'][0]

	if response['status'] == '0':
		print 'Sent message', response['message-id']

		print 'Remaining balance is', response['remaining-balance']
	else:
		print 'Error:', response['error-text']

	return redirect(reverse('users:travelerDashboard'))
