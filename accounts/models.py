from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class types(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	is_delete = models.BooleanField(default=0)

class industry_type(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	is_delete = models.BooleanField(default=0)

class details(models.Model):
	first_name = models.CharField(max_length=250, null=True, blank=True)
	middle_name = models.CharField(max_length=250, null=True, blank=True)
	last_name = models.CharField(max_length=250, null=True, blank=True)
	email = models.CharField(max_length=250, null=True, blank=True)
	phone = models.CharField(max_length=250, null=True, blank=True)
	business_phone = models.CharField(max_length=250, null=True, blank=True)
	business_description = models.TextField(null=True, blank=True)
	company_name = models.CharField(max_length=250, null=True, blank=True)
	title = models.CharField(max_length=250, null=True, blank=True)
	website = models.CharField(max_length=250, null=True, blank=True)
	photo_path = models.FileField(upload_to='profile_photo/', null=True)
	account_type = models.ForeignKey(types, on_delete=models.SET_NULL, null=True, blank=True)
	industry_type = models.ForeignKey(industry_type, on_delete=models.SET_NULL, null=True, blank=True)
	status = models.CharField(max_length=250, null=True, default="unverified")
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now_add=True)
	history = models.TextField(null=True, blank=True)
	userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class address_info(models.Model):
	street = models.CharField(max_length=250, null=True, blank=True)
	city = models.CharField(max_length=250, null=True, blank=True) 
	state = models.CharField(max_length=250, null=True, blank=True)
	code = models.CharField(max_length=250, null=True, blank=True)
	country = models.CharField(max_length=250, null=True, blank=True)
	address_type = models.CharField(max_length=250, null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now_add=True)
	history = models.TextField(null=True, blank=True)
	userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class password_category(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	is_delete = models.BooleanField(default=0)

class password_manager(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	username = models.CharField(max_length=250, null=True, blank=True)
	password = models.CharField(max_length=250, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	url = models.CharField(max_length=250, null=True, blank=True)
	category = models.ForeignKey(password_category, on_delete=models.SET_NULL, null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now_add=True)
	history = models.TextField(null=True, blank=True)
	userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)