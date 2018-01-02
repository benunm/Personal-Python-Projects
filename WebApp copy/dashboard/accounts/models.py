# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=100, default='')
	phone = models.IntegerField(default = 0)

class Tempstatus810(models.Model):
	Company_Code = models.CharField(max_length=1000)
	Division_Code = models.CharField(max_length=1000)
	Record_Number = models.CharField(max_length=1000)
	Customer_Number = models.CharField(max_length=1000)
	Customer_Purchase_Order_Number = models.CharField(max_length=1000)
	DATE_INVOICED = models.CharField(max_length=1000)
	DATE_CREATED = models.CharField(max_length=1000)
	DOCTYPE = models.CharField(max_length=1000)
	REMARKS = models.CharField(max_length=1000)





