from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
#User Login done with facebook
class fbUser(models.Model):
	GENDER_CHOICES = (('M','Male'),('F','Female'),('O','Other'))
	fbid = models.CharField(max_length=40,null=True,blank=True)
	gmailid = models.CharField(default=0,max_length=40,null=True,blank=True)
	username = models.CharField(max_length=40,unique=True,blank=False,null=False)
	email = models.EmailField(null=False,blank=False,unique=True)
	gender = models.CharField(max_length=2,default=0,choices=GENDER_CHOICES,null=False,blank=False)
	phone = PhoneNumberField(unique=True,null=True,blank=True,help_text=('Only Indian'))

	def __unicode__(self):
		return self.name