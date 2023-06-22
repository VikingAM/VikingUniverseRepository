from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime
from tickets.models import issue, issue_type, task_cetegory_theme, task_category, task, task_comment
from accounts.models import details

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
	open_tickets = task.objects.filter(status="Open", owner=request.user, is_delete=0)
	return render(request, 'task_dashboard.html', {"profile_details":profile_details, "open_tickets":open_tickets})

@login_required(login_url='/accounts/login')
def taskSubmit(request):
	profile_details = details.objects.get(userId=request.user.id)
	category_theme = task_cetegory_theme.objects.filter(is_delete=0)
	return render(request, 'submit_task_page.html', {"profile_details":profile_details, "category_themes": category_theme})

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
	if task_details.status == "Open":
		return render(request, 'task_open.html', {"profile_details":profile_details, "task_detail":task_details})
	elif task_details.status == "In Progress":
		comments = task_comment.objects.filter(task=task_details)
		return render(request, 'task_in_progress.html', {"profile_details":profile_details, "task_detail":task_details, "comments":comments})
	elif task_details.status == "Complete":
		comments = task_comment.objects.filter(task=task_details)
		return render(request, 'task_in_progress.html', {"profile_details":profile_details, "task_detail":task_details, "comments":comments})
	else:
		return render(request, 'task_open.html', {"profile_details":profile_details, "task_detail":task_details})

@login_required(login_url='/accounts/login')
def editTask(request):
	data = {}
	data['status_code'] = 0
	try:
		task_details = task.objects.get(pk=request.POST['task_id'])
	except:
		data['error_msg'] = "Task does not exists!"
		return JsonResponse(data, safe=False)

	task_details.title = request.POST['task_title']
	task_details.description = request.POST['description']

	try:
		task_details.save()
		data['status_code'] = 1
	except:
		data['error_msg'] = "Error on saving the task!"
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
	except:
		data['error_msg'] = "Ticket does exists!"
		return JsonResponse(data, safe=False)

	data['issue_name'] = issue_details.title
	data['issue_id'] = issue_details.pk
	data['issue_status'] = issue_details.ticket_status
	data['issue_description'] = issue_details.description
	data['create_date'] = issue_details.create_date
	data['owner_name'] = issueOwnder.first_name+" "+issueOwnder.last_name



	return JsonResponse(data, safe=False)