from __future__ import unicode_literals
from django.db import models
import re

'''
	The only preexisting code is the validate function
'''
class ManageUser(models.Manager):
	def validate(self, info):
		emailValidate = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		nameValidate = re.compile(r'^[A-Za-z]+ [A-Za-z]+$')

		# Dictionary of potential error messages
		errorMessages = {
			'name': 'Name is not valid. Name must be at least 2 characters and not contain any numbers or special characters.',
			'email': 'Email is not valid.'
		}

		# This list will hold any errors that need to be thrown in messages.
		returnErrors = []

		# Validate the first name that was entered.
		if len(info['name']) < 2 or not nameValidate.match(info['name']):
			returnErrors.append(errorMessages['name'])

		# Validate the email that was entered.
		if len(info['email']) < 1 or not emailValidate.match(info['email']):
			returnErrors.append(errorMessages['email'])

		return returnErrors

	def addTraveler(self, info):
		# Stringify interests into the interests variable
		interests = ', '.join(info['interests'])

		self.create(name = info['name'], email = info['email'], location = info['location'], interests = interests)

		confirmMsg = 'Welcome Traveler! You\'re ready to go!'

		confirm = (True, confirmMsg)

		return confirm

	# def getTraveler(self, info):


	def addGuide(self, info):
		# Stringify expertise into the expertise variable
		expertise = ','.join(info['expertise'])

		self.create(name = info['name'], email = info['email'], location = info['location'], expertise = expertise)

		confirmMsg = 'Welcome Guide! You\'re ready to go!'

		confirm = (True, confirmMsg)

		return confirm

	# def getGuide(self, info):



# Create your models here.
class Traveler(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=100)
	location = models.CharField(max_length=100, default='Washington DC')
	interests = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ManageUser()

	def __str__(self):
		print self.name

class Guide(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=100)
	location = models.CharField(max_length=100, default='Washington DC')
	expertise = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ManageUser()

	def __str__(self):
		print self.name
