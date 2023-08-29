from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timesince import timesince
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime
from tickets.models import task_cetegory_theme, task_category, task, task_file, task_comment, task_comment_file, issue, issue_type, issue_comment, issue_comment_file, issue_file
from accounts.models import details
import random, os

# Create your views here.
@login_required(login_url='/accounts/login')
def Addticket(request):
	data = {}
	data['status_code'] = 0
	new_issue = issue()
	if request.POST['type'] != "0":
		issue_type_instance = issue_type.objects.get(pk=request.POST['type'])
	else:
		issue_type_instance = None

	userInstance = User.objects.get(pk=request.user.id)

	new_issue.title = request.POST['title']
	new_issue.description = request.POST['description']
	new_issue.issue_type = issue_type_instance
	new_issue.userId = userInstance
	try:
		new_issue.save()
		data['status_code'] = 1
		data['status_msg'] = "Create successfully!"
	except:
		data['status_code'] = 0
		data['status_msg'] = "Error on adding a ticket!"
		return JsonResponse(data, safe=False)

	return JsonResponse(data, safe=False)


@login_required(login_url='/accounts/login')
def ticketingPage(request):
	issue_types = issue_type.objects.all()
	list_of_issue_ticket = issue.objects.filter(userId=request.user.id);
	profile_details = details.objects.get(userId=request.user.id)
	return render(request, 'ticketing_page.html', {"issue_types":issue_types, "issue_tickets": list_of_issue_ticket, "profile_details": profile_details})

@login_required(login_url='/accounts/login')
def taskDashboard(request):
	profile_details = details.objects.get(userId=request.user.id)
	tickets = task.objects.filter(owner=request.user, is_delete=0).order_by('-create_date')
	return render(request, 'task_dashboard.html', {"profile_details":profile_details, "tickets":tickets})

@login_required(login_url='/accounts/login')
def taskSubmit(request):
	profile_details = details.objects.get(userId=request.user.id)
	category_theme = task_cetegory_theme.objects.filter(is_delete=0)
	return render(request, 'submit_task_page.html', {"profile_details":profile_details, "category_themes": category_theme, "site_url":settings.SITE_URL})

@login_required(login_url='/accounts/login')
def getCategoryServices(request):
	data = {}
	data['status_code'] = 0
	theme_instance = task_cetegory_theme.objects.get(pk=request.POST['CategoryThemeId'])
	list_of_category = task_category.objects.filter(is_delete=0, theme=theme_instance)
	list_of_category_array = {}
	for category in list_of_category:
		current_list = {}
		current_list['id'] = category.pk
		current_list['name'] = category.name
		current_list['parent'] = category.parent
		current_list['description'] = category.short_description
		list_of_category_array[category.pk] = current_list
		data['status_code'] = 1
	data['list_of_category'] = list_of_category_array
	return JsonResponse(data, safe=False)

@login_required(login_url='/accounts/login')
def getCategoryDetailsById(request):
	data = {}
	data['status_code'] = 0

	try:
		list_of_category = task_category.objects.filter(is_delete=0, status=1)
		list_of_category_array = {}
		for category in list_of_category:
			current_list = {}
			current_list['id'] = category.pk
			current_list['name'] = category.name
			current_list['parent'] = category.parent
			current_list['description'] = category.short_description
			list_of_category_array[category.pk] = current_list
		data['list_of_category'] = list_of_category_array
	except:
		data['error_msg'] = "Error on getting categories"
		return JsonResponse(data, safe=False)

	try:
		service_details = task_category.objects.get(pk=request.POST['category_id'])
		data['category_name'] = service_details.name
		data['category_id'] = service_details.pk
	except:
		data['error_msg'] = "Service Does not exists"
		return JsonResponse(data, safe=False)

	try:
		category_theme = task_cetegory_theme.objects.get(pk=service_details.theme.id)
		data['category_theme'] = category_theme.name
		data['category_theme_id'] = category_theme.pk
	except:
		data['error_msg'] = "Category Theme Does not exists" 
		return JsonResponse(data, safe=False)

	try:
		service_parent = task_category.objects.get(pk=service_details.parent)
		data['category_parent_name'] = service_parent.name
		data['category_parent_id'] = service_parent.pk
		data['status_code'] = 1
	except:
		data['error_msg'] = "Category Does not exists" 
		return JsonResponse(data, safe=False)
	return JsonResponse(data, safe=False)

@login_required(login_url='/accounts/login')
def createTask(request):
	data = {}
	data['status_code'] = 0
	new_task = task();
	new_task.title = request.POST['task_name']
	new_task.description = request.POST['task_description']

	try:
		categoryInstance = task_category.objects.get(pk=request.POST['category_id'])
	except:
		data['error_msg'] = "Category Does not exists!"
		return JsonResponse(data, safe=False)

	new_task.category = categoryInstance
	new_task.owner = request.user

	try:
		new_task.save()
		data['status_code'] = 1
	except:
		data['error_msg'] = "error on saving a task!"
		return JsonResponse(data, safe=False)

	return JsonResponse(data, safe=False)


# will add another param if admin user
@login_required(login_url='/accounts/login')
def getTciketByFilter(request):
	data = {}
	data['status_code'] = 0
	try:
		tasks = task.objects.filter(status=request.POST['filter'], owner=request.user.id, is_delete=0)
	except:
		data['error_msg'] = "error on grabing the tickets"
		return JsonResponse(data, safe=False)

	list_of_task = {}
	for easch_task in tasks:
		current_list = {}
		current_list['id'] = easch_task.pk
		current_list['name'] = easch_task.title
		current_list['description'] = easch_task.description
		current_list['create_date'] = easch_task.create_date.strftime("%B %d, %Y")
		current_list['caetgory_name'] = easch_task.category.name
		current_list['task_percentage'] = easch_task.task_percentage
		list_of_task[easch_task.pk] = current_list
	data['list_of_task'] = list_of_task
	data['status_code'] = 1

	return JsonResponse(data, safe=False)

@login_required(login_url='/accounts/login')
def taskDetails(request, task_id):
	profile_details = details.objects.get(userId=request.user.id)
	task_details = task.objects.get(pk=task_id)
	task_attachments = task_file.objects.filter(task=task_id, is_delete=0)
	return render(request, 'task_detailed.html', {"profile_details":profile_details, "task_detail":task_details, "attachments":task_attachments})


@login_required(login_url='/accounts/login')
def editTask(request, task_id):
	user_detail = details.objects.get(userId=request.user.id)
	if request.method == 'POST':
		try:
			task_details = task.objects.get(pk=task_id)
		except:
			data['error_msg'] = "Task does not exists!"
			return redirect("taskDetails", task_id=task_id)
		task_details.title = request.POST['task_title']
		task_details.description = request.POST['edit_description']
		ticket_attachments = request.FILES['ticket_attachments'] if 'ticket_attachments' in request.FILES else None
		if ticket_attachments:
			for f in request.FILES.getlist('ticket_attachments'):
				new_task_file = task_file()
				new_task_file.task = task_details
				new_task_file.name = f.name
				split_tup = os.path.splitext(f.name)
				file_extension = split_tup[1]
				random_number = random.randint(0,1000)
				fs = FileSystemStorage()
				file_name = "tasks_attachments/id_"+str(task_id)+"_"+str(random_number)+""+str(file_extension)
				comment_file = fs.save(file_name, f)
				new_task_file.issue_file = comment_file
				new_task_file.save()
		task_details.save()
	return redirect("taskDetails", task_id=task_id)

@login_required(login_url='/accounts/login')
def postTaskComment(request, task_id):
	user_detail = details.objects.get(userId=request.user.id)
	userInstance = User.objects.get(pk=request.user.id)
	if request.method == 'POST':
		try:
			task_details = task.objects.get(pk=task_id)
		except:
			data['error_msg'] = "Task does not exists!"
			return redirect("taskDetails", task_id=task_id)
		new_task_comment = task_comment()
		new_task_comment.comment = request.POST['task_comment']
		new_task_comment.task = task_details
		new_task_comment.owner = userInstance
		new_task_comment.save()
		task_attachments = request.FILES['task_comment_attachments'] if 'task_comment_attachments' in request.FILES else None
		if task_attachments:
			for f in request.FILES.getlist('task_comment_attachments'):
				new_task_comment_file = task_comment_file()
				new_task_comment_file.name = f.name
				new_task_comment_file.comment = new_task_comment
				split_tup = os.path.splitext(f.name)
				file_extension = split_tup[1]
				random_number = random.randint(0,1000)
				fs = FileSystemStorage()
				file_name = "tasks_attachments/id_"+str(task_id)+"_"+str(random_number)+""+str(file_extension)
				comment_file = fs.save(file_name, f)
				new_task_comment_file.comment_file = comment_file
				new_task_comment_file.save()
		return redirect("taskDetails", task_id=task_id)

@login_required(login_url='/accounts/login')
def updateTaskPercentage(request):
	data = {}
	data['status_code'] = 0
	data["status_msg"] = ""
	user_details = details.objects.get(userId=request.user.id)
	try:
		task_details = task.objects.get(pk=request.POST['task_id'])
	except:
		data['status_msg'] = "Task Does not exists!"
		return JsonResponse(data, safe=False)
	current_date = datetime.now()
	update_history = str(task_details.history)+"\r\n user="+ str(request.user.id) +" updated percentage of task from "+str(task_details.task_percentage)+" to "+str(request.POST['task_percentage'])+" "+str(current_date)
	task_details.history = update_history
	task_details.task_percentage = request.POST['task_percentage']
	try:
		task_details.save()
		data['status_code'] = 1
	except:
		data['status_msg'] = "Error on saving Task!"
		return JsonResponse(data, safe=False)

	return JsonResponse(data, safe=False)

@login_required(login_url='/accounts/login')
def addRevision(request):
	data = {}
	data['status_code'] = 0
	try:
		task_details = task.objects.get(pk=request.POST['task_id'])
	except:
		data['error_msg'] = "Task does not exists!";
		return JsonResponse(data, safe=False)

	new_task_comment =  task_comment()
	new_task_comment.comment = request.POST['revision_comment']
	new_task_comment.task = task_details
	new_task_comment.owner = request.user

	try:
		new_task_comment.save()
		data['status_code'] = 1
	except:
		data['error_msg'] = "Error on saving the revision!";
		return JsonResponse(data, safe=False)
	return JsonResponse(data, safe=False)

@login_required(login_url='/accounts/login')
def taskApprove(request):
	data = {}
	data['status_code'] = 0
	try:
		task_details = task.objects.get(pk=request.POST['task_id'])
	except:
		data['error_msg'] = "Task does not exists!"
		return JsonResponse(data, safe=False)

	task_details.status = "Complete"
	task_details.task_percentage = 100

	try:
		task_details.save();
		data['status_code'] = 1
	except:
		data['error_msg'] = "Error on approving task!"
		return JsonResponse(data, safe=False)
	return JsonResponse(data, safe=False)

@login_required(login_url='/accounts/login')
def getTicketDetails(request):
	data = {}
	data['status_code'] = 0

	try:
		issue_details = issue.objects.get(pk=request.POST['ticket_id'])
		issueOwnder = details.objects.get(userId=issue_details.userId)
		data['status_code'] = 1
	except:
		data['error_msg'] = "Ticket does exists!"
		return JsonResponse(data, safe=False)

	data['issue_name'] = issue_details.title
	data['issue_id'] = issue_details.pk
	data['issue_status'] = issue_details.ticket_status
	data['issue_description'] = issue_details.description
	data['create_date'] = issue_details.create_date.strftime("%B %d, %Y %I:%M %p")
	data['owner_name'] = issueOwnder.first_name+" "+issueOwnder.last_name
	return JsonResponse(data, safe=False)

@login_required(login_url='/accounts/login')
def updateTicketTitle(request):
	data = {}
	data['status_code'] = 0
	data["status_msg"] = ""
	user_details = details.objects.get(userId=request.user.id)
	try:
		tikcet_details = issue.objects.get(pk=request.POST['ticket_id'])
	except:
		data['status_msg'] = "Ticket Does not exists!"
		return JsonResponse(data, safe=False)
	current_date = datetime.now()
	update_history = str(tikcet_details.history)+"\r\n user="+ str(request.user.id) +" updated title from "+str(tikcet_details.title)+" to "+str(request.POST['ticket_title'])+" "+str(current_date)
	tikcet_details.history = update_history
	tikcet_details.title = request.POST['ticket_title']
	try:
		tikcet_details.save()
		data['status_code'] = 1
	except:
		data['status_msg'] = "Error on saving Ticket!"
		return JsonResponse(data, safe=False)

	return JsonResponse(data, safe=False)

@login_required(login_url='/accounts/login')
def updateTicketStatus(request):
	data = {}
	data['status_code'] = 0
	data["status_msg"] = ""
	user_details = details.objects.get(userId=request.user.id)
	try:
		ticket_details = issue.objects.get(pk=request.POST['ticket_id'])
	except:
		data['status_msg'] = "Ticket Does not exists!"
		return JsonResponse(data, safe=False)
	current_date = datetime.now()
	update_history = str(ticket_details.history)+"\r\n user="+ str(request.user.id) +" updated status from "+str(ticket_details.ticket_status)+" to "+str(request.POST['ticket_status'])+" "+str(current_date)
	ticket_details.history = update_history
	ticket_details.update_date = current_date
	ticket_details.user_last_updated = user_details
	ticket_details.ticket_status = request.POST['ticket_status']
	try:
		ticket_details.save()
		data['status_code'] = 1
	except:
		data['status_msg'] = "Error on saving Ticket!"
		return JsonResponse(data, safe=False)

	return JsonResponse(data, safe=False)

@login_required(login_url='/accounts/login')
def UpdateTicketPercentage(request):
	data = {}
	data['status_code'] = 0
	data["status_msg"] = ""
	user_details = details.objects.get(userId=request.user.id)
	try:
		ticket_details = issue.objects.get(pk=request.POST['ticket_id'])
	except:
		data['status_msg'] = "Ticket Does not exists!"
		return JsonResponse(data, safe=False)
	current_date = datetime.now()
	update_history = str(ticket_details.history)+"\r\n user="+ str(request.user.id) +" updated percentage of task from "+str(ticket_details.percentage)+" to "+str(request.POST['ticket_percentage'])+" "+str(current_date)
	ticket_details.history = update_history
	ticket_details.update_date = current_date
	ticket_details.percentage = request.POST['ticket_percentage']
	try:
		ticket_details.save()
		data['status_code'] = 1
	except:
		data['status_msg'] = "Error on saving Ticket!"
		return JsonResponse(data, safe=False)

	return JsonResponse(data, safe=False)

@login_required(login_url='/accounts/login')
def UpdateTicketDescription(request):
	data = {}
	data['status_code'] = 0
	data["status_msg"] = ""
	user_details = details.objects.get(userId=request.user.id)
	try:
		tikcet_details = issue.objects.get(pk=request.POST['ticket_id'])
	except:
		data['status_msg'] = "Ticket Does not exists!"
		return JsonResponse(data, safe=False)
	current_date = datetime.now()
	update_history = str(tikcet_details.history)+"\r\n user="+ str(request.user.id) +" updated description of task of task from "+str(tikcet_details.description)+" <<==old to new==> "+str(request.POST['ticket_description'])+" "+str(current_date)
	tikcet_details.history = update_history
	tikcet_details.description = request.POST['ticket_description']
	try:
		tikcet_details.save()
		data['status_code'] = 1
	except:
		data['status_msg'] = "Error on saving Ticket!"
		return JsonResponse(data, safe=False)
	return JsonResponse(data, safe=False)

@login_required(login_url='/accounts/login')
def getTicketComments(request):
	data = {}
	data['status_code'] = 0
	data["status_msg"] = ""
	try:
		tikcet_details = issue.objects.get(pk=request.POST['ticket_id'])
	except:
		data['status_msg'] = "Ticket Does not exists!"
		return JsonResponse(data, safe=False)
	list_of_comments = issue_comment.objects.filter(issue=request.POST['ticket_id'], is_delete=0)
	ticket_attachment = issue_file.objects.filter(issue=request.POST['ticket_id'], is_delete=0)
	ticket_attachment_list = {}
	for attachment in ticket_attachment:
		current_attachment = {}
		current_attachment['id'] = attachment.pk
		current_attachment['name'] = attachment.name
		current_attachment['file'] = attachment.issue_file
		ticket_attachment_list[attachment.pk] = current_attachment

	comments = {}
	for comment in list_of_comments:
		current_comment = {}
		current_comment['id'] = comment.pk
		current_comment['comment'] = comment.comment
		current_comment['create_date'] = comment.create_date.strftime("%m/%d/%Y, %H:%M %p")
		comment_owner_instance = details.objects.get(userId=comment.owner)
		current_comment['owner_name'] = comment_owner_instance.first_name+" "+comment_owner_instance.last_name
		try:
			current_comment['owner_name_pic'] = comment_owner_instance.profile_picture.url
		except:
			current_comment['owner_name_pic'] = None
		comment_attachments = issue_comment_file.objects.filter(commentId=comment.pk)
		attachments_list = {}
		if len(comment_attachments) > 0:
			for attachment in comment_attachments:
				current_attachments = {}
				current_attachments['id'] = attachment.pk
				try:
					current_attachments['file'] = attachment.comment_file.url
				except:
					current_attachments['file'] = None
				current_attachments['name'] = attachment.comment_file_name
				attachments_list[attachment.pk] = current_attachments
		current_comment['attachments'] = attachments_list
		comments[comment.pk] = current_comment

	data['issue_attachments'] = ticket_attachment_list
	data['comments'] = comments
	data['comment_count'] = len(list_of_comments)
	data['status_code'] = 1

	return JsonResponse(data, safe=False)

@login_required(login_url='/accounts/login')
def getTicketList(request):
	data = {}
	data['status_code'] = 0
	data["status_msg"] = ""
	user_details = details.objects.get(userId=request.user.id)

	try:
		list_of_task = task.objects.filter(is_delete=0)
		data['status_code'] = 1
	except:
		data['status_msg'] = 'error on grabing tickets!'
		return JsonResponse(data, safe=False)

	tasks = {}
	for task_detail in list_of_task:
		current_task = {}
		current_task['title'] = task_detail.title
		current_task['task_id'] = task_detail.pk
		current_task['description'] = task_detail.description
		current_task['status'] = task_detail.status
		current_task['create_date_formatted'] = task_detail.create_date.strftime("%m/%d/%Y, %H:%M %p")
		try:
			current_task['end_date'] = task_detail.end_date.strftime("%m/%d/%Y, %H:%M %p")
		except:
			current_task['end_date'] = None
		current_task['create_date_since'] = timesince(task_detail.create_date)
		current_task['percentage'] = task_detail.task_percentage
		task_owner_instance = details.objects.get(userId=task_detail.owner)
		current_task['owner_name'] = task_owner_instance.first_name+" "+task_owner_instance.last_name
		try:
			current_task['owner_name_pic'] = task_owner_instance.profile_picture.url
		except:
			current_task['owner_name_pic'] = None
		tasks[task_detail.pk] = current_task
	data['tasks'] = tasks
	return JsonResponse(data, safe=False)

@login_required(login_url='accounts/login')
def getTaskComments(request):
	data = {}
	data['status_code'] = 0
	data["status_msg"] = ""
	try:
		task_details = task.objects.get(pk=request.POST['task_id'])
	except:
		data['status_msg'] = "Task Does not exists!"
		return JsonResponse(data, safe=False)
	list_of_comments = task_comment.objects.filter(task=request.POST['task_id'], is_delete=0)
	list_of_attachments = task_file.objects.filter(task=request.POST['task_id'], is_delete=0)
	task_attachment_list = {}
	attachmentsCount = 1
	for attachment in list_of_attachments:
		current_attachment = {}
		current_attachment['id'] = attachment.pk
		current_attachment['name'] = attachment.name
		try:
			current_attachment['file'] = attachment.issue_file.url
		except:
			current_attachment['file'] = None
		task_attachment_list[attachmentsCount] = current_attachment
		attachmentsCount = attachmentsCount + 1
	comments = {}
	for comment in list_of_comments:
		current_comment = {}
		current_comment['id'] = comment.pk
		current_comment['comment'] = comment.comment
		current_comment['create_date'] = comment.create_date.strftime("%m/%d/%Y, %H:%M %p")
		comment_owner_instance = details.objects.get(userId=comment.owner)
		current_comment['owner_name'] = comment_owner_instance.first_name+" "+comment_owner_instance.last_name
		try:
			current_comment['owner_name_pic'] = comment_owner_instance.profile_picture.url
		except:
			current_comment['owner_name_pic'] = None
		comment_attachments = task_comment_file.objects.filter(comment=comment.pk)
		attachments_list = {}
		if len(comment_attachments) > 0:
			for attachment in comment_attachments:
				current_attachments = {}
				current_attachments['id'] = attachment.pk
				try:
					current_attachments['file'] = attachment.comment_file.url
				except:
					current_attachments['file'] = None
				current_attachments['name'] = attachment.name
				attachments_list[attachment.pk] = current_attachments
				task_attachment_list[attachmentsCount] = current_attachments
				attachmentsCount = attachmentsCount + 1

		current_comment['attachments'] = attachments_list
		comments[comment.pk] = current_comment
	data['task_attachments'] = task_attachment_list
	data['comments'] = comments
	data['comment_count'] = len(list_of_comments)
	data['status_code'] = 1
	return JsonResponse(data, safe=False)

@login_required(login_url='accounts/login')
def removeTaskAttachment(request):
	data = {}
	data['status_code'] = 0
	data["status_msg"] = ""
	try:
		task_attachment = task_file.objects.get(pk=request.POST['task_attachment_id'])
	except:
		data['status_msg'] = "Task Does not exists!"
		return JsonResponse(data, safe=False)
	task_attachment.history = "username id "+str(request.user.id)+" remove attachment!"
	task_attachment.is_delete = 1
	task_attachment.save()
	data['status_code'] = 1
	return JsonResponse(data, safe=False)

@login_required(login_url='accounts/login')
def UpdateTaskStatus(request):
	data = {}
	data['status_code'] = 0
	data["status_msg"] = ""
	try:
		task_detail = task.objects.get(pk=request.POST['task_id'])
	except:
		data['status_msg'] = "Task Does not exists!"
		return JsonResponse(data, safe=False)

	task_detail.status = request.POST['task_status']
	task_detail.save()
	data['status_code'] = 1
	return JsonResponse(data, safe=False)