from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class products(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	description = models.CharField(max_length=250, null=True, blank=True)
	credits = models.CharField(max_length=250, null=True, blank=True)
	stripeId = models.CharField(max_length=250, null=True, blank=True)
	price = models.CharField(max_length=250, null=True, blank=True)
	productType = models.CharField(max_length=250, null=True, blank=True, default="Sub")
	create_date = models.DateTimeField(auto_now_add=True)
	is_delete = models.BooleanField(default=0)


class sessions(models.Model):
	sessionId = models.CharField(max_length=250, null=True, blank=True)
	productId = models.ForeignKey(products, on_delete=models.SET_NULL, null=True, blank=True)
	userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	is_delete = models.BooleanField(default=0)


