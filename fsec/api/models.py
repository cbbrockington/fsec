from django.db import models

# Create your models here.

class Member(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	email = models.CharField(max_length=64)
	phone_number = models.CharField(max_length=10)
	preference = models.CharField(max_length=64)
	supervisor = models.CharField(max_length=64)
