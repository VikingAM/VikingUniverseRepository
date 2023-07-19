from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class issue_type(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	is_delete = models.BooleanField(default=0)

class issue(models.Model):
	title = models.CharField(max_length=250, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	issue_type = models.ForeignKey(issue_type, on_delete=models.SET_NULL, null=True, blank=True)
	is_delete = models.BooleanField(default=0)
	ticket_status = models.CharField(max_length=250, null=True, blank=True, default="Pending")
	percentage = models.CharField(max_length=250, null=True, blank=True, default=0)
	create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	due_date = models.DateTimeField(null=True, blank=True)
	update_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	history = models.TextField(null=True, blank=True)
	userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class issue_file(models.Model):
	issue =models.ForeignKey(issue, on_delete=models.SET_NULL, null=True, blank=True)
	name = models.CharField(max_length=250, null=True, blank=True)
	issue_file = models.FileField(upload_to='issue_upload/', null=True)
	is_delete = models.BooleanField(default=0)
	create_date = models.DateTimeField(auto_now_add=True)
	history = models.TextField(null=True, blank=True)

class issue_responders(models.Model):
	issue = models.ForeignKey(issue, on_delete=models.SET_NULL, null=True, blank=True)
	responder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	is_delete = models.BooleanField(default=0)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now_add=True)
	history = models.TextField(null=True, blank=True)

class issue_comment(models.Model):
	comment = models.TextField(null=True, blank=True)
	is_delete = models.BooleanField(default=0)
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	issue =models.ForeignKey(issue, on_delete=models.SET_NULL, null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now_add=True)
	history = models.TextField(null=True, blank=True)

class issue_comment_file(models.Model):
	commentId = models.ForeignKey(issue_comment, on_delete=models.SET_NULL, null=True, blank=True)
	comment_file_name = models.CharField(max_length=250, null=True, blank=True)
	comment_file = models.FileField(upload_to='issue_upload/', null=True)
	is_delete = models.BooleanField(default=0)
	create_date = models.DateTimeField(auto_now_add=True)
	history = models.TextField(null=True, blank=True)

class task_cetegory_theme(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	short_description = models.TextField(null=True)
	is_delete = models.BooleanField(default=0)
	
	def __str__(self):
		return self.name
		
class task_category(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	short_description = models.TextField(null=True)
	parent = models.CharField(max_length=250, null=True, blank=True)
	theme = models.ForeignKey(task_cetegory_theme, on_delete=models.SET_NULL, null=True, blank=True)
	status = models.BooleanField(default=1)
	is_delete = models.BooleanField(default=0)

class task_services(models.Model):
	name = models.CharField(max_length=250, null=True, blank=True)
	short_description = models.TextField(null=True)
	category = models.ForeignKey(task_category, on_delete=models.SET_NULL, null=True, blank=True)
	is_delete = models.BooleanField(default=0)

class task(models.Model):
	title = models.CharField(max_length=250, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	category = models.ForeignKey(task_category, on_delete=models.SET_NULL, null=True, blank=True)
	due_date = models.DateTimeField(null=True, blank=True)
	urgency = models.CharField(max_length=250, null=True, blank=True, default="Low")
	task_percentage = models.IntegerField(default=0)
	create_date = models.DateTimeField(auto_now_add=True)
	end_date = models.DateTimeField(null=True, blank=True)
	update_date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=250, null=True, blank=True, default="Open")
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	is_delete = models.BooleanField(default=0)

class task_file(models.Model):
	task =models.ForeignKey(task, on_delete=models.SET_NULL, null=True, blank=True)
	issue_file = models.FileField(upload_to='task_upload/', null=True)
	is_delete = models.BooleanField(default=0)
	create_date = models.DateTimeField(auto_now_add=True)
	history = models.TextField(null=True, blank=True)

class task_responders(models.Model):
	task =models.ForeignKey(task, on_delete=models.SET_NULL, null=True, blank=True)
	responder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	is_delete = models.BooleanField(default=0)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now_add=True)
	history = models.TextField(null=True, blank=True)

class task_comment(models.Model):
	comment = models.TextField(null=True, blank=True)
	is_delete = models.BooleanField(default=0)
	task = models.ForeignKey(task, on_delete=models.SET_NULL, null=True, blank=True)
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now_add=True)
	history = models.TextField(null=True, blank=True)

class task_comment_file(models.Model):
	comment =models.ForeignKey(task_comment, on_delete=models.SET_NULL, null=True, blank=True)
	comment_file = models.FileField(upload_to='task_upload/', null=True)
	is_delete = models.BooleanField(default=0)
	create_date = models.DateTimeField(auto_now_add=True)
	history = models.TextField(null=True, blank=True)