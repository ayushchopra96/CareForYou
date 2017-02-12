from __future__ import unicode_literals

from django.db import models
from register.models import MyUser
from django.utils.deconstruct import deconstructible

# Create your models here.
class Test(models.Model):
	def def_val():
		val = MyUser.objects.get_or_create(uid=1)
		return val

	STATUS_CHOICES = (('D','Delivered'),('E','Executing'),('S','Submitted'))
	TEST_NO = (('1','t1'),('2','t2'),('3','t3'))
	username = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)
	status = models.CharField(max_length=5,choices=STATUS_CHOICES,default=0,null=True,blank=True)
	test_id = models.CharField(max_length=6,choices=TEST_NO,default=0)

	def __unicode__(self):
		return str(self.username)
		#return [self.test_id,unicode(self.username)]
