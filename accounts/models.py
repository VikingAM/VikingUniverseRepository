from django.db import models
from django.contrib.auth.models import User
from payment.models import sessions

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
	profile_picture = models.FileField(upload_to='profile_photo/', null=True, blank=True)
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
	zip_code = models.CharField(max_length=250, null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now_add=True)
	history = models.TextField(null=True, blank=True)
	userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class user_validation(models.Model):
	userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	verification_code = models.CharField(max_length=250)
	status = models.BooleanField(default=0)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(null=True, blank=True)

class password_category(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	is_delete = models.BooleanField(default=0)

class password_reset_code(models.Model):
	code = models.CharField(max_length=250, null=True, blank=True)
	userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	status = models.BooleanField(default=0)
	create_date = models.DateTimeField(auto_now_add=True)

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
	status = models.BooleanField(default=1)

class credit_score(models.Model):
	amount = models.IntegerField(null=True, blank=True)
	credit = models.IntegerField(null=True, blank=True, default=0)
	paid = models.BooleanField(default=0)
	create_date = models.DateTimeField(auto_now_add=True)
	userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	sessionId = models.ForeignKey(sessions, on_delete=models.SET_NULL, null=True, blank=True)
	status = models.BooleanField(default=1)

class invoice(models.Model):
	create_date = models.DateTimeField(auto_now_add=True)
	userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	payment_method = models.CharField(max_length=250, null=True, blank=True)
	product_name = models.CharField(max_length=250, null=True, blank=True)
	product_description = models.CharField(max_length=250, null=True, blank=True)
	amount = models.IntegerField(null=True, blank=True)
	quantity = models.IntegerField(null=True, blank=True)
	status = models.BooleanField(default=1)
