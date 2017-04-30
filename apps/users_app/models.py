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

		newUser = self.create(name = info['name'], email = info['email'], phone = info['phone'], interests = interests)

		confirmMsg = 'Welcome Traveler! You\'re ready to go!'

		confirm = (True, confirmMsg, newUser.id)

		return confirm

	def addGuide(self, info):
		# Stringify expertise into the expertise variable
		expertise = ', '.join(info['expertise'])

		self.create(name = info['name'], email = info['email'], phone = info['phone'], expertise = expertise)

		confirmMsg = 'Welcome Guide! You\'re ready to go!'

		confirm = (True, confirmMsg)

		return confirm

	def matchGuides(self, id):
		traveler = Traveler.objects.filter(id = id)

		travelerInterests = traveler[0].interests.split()

		guides = Guide.objects.all()

		guideMatches = []

		for guide in range(len(guides)):
			guideExpertise = guides[guide].expertise.split()
			matches = len(set(travelerInterests) & set(guideExpertise))
			if matches > 0:
				matchTuple = (guides[guide], matches)
				guideMatches.append(matchTuple)

		return guideMatches

# Create your models here.
class Traveler(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=100)
	phone = models.IntegerField(default='2025551234')
	interests = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ManageUser()

	def __iter__(self):
		return [
			self.name,
			self.email,
			self.phone,
			self.interests,
			self.created_at,
			self.updated_at
		]

	def __str__(self):
		return self.name

class Guide(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=100)
	phone = models.IntegerField(default='2025551234')
	matchedTraveler = models.ForeignKey(Traveler, default=1, related_name='traveler_match')
	expertise = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ManageUser()

	def __iter__(self):
		return [
			self.name,
			self.email,
			self.phone,
			self.expertise,
			self.created_at,
			self.updated_at
		]

	def __str__(self):
		return self.name
