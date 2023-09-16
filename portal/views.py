from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.conf import settings
from accounts.models import details, address_info, user_validation, industry_type, password_manager, password_category, invoice
from tickets.models import issue, issue_comment, issue_comment_file, task, task_comment, task_comment_file, task_file, issue_file, issue_responders, task_responders, task_cetegory_theme, task_category, task_sub_category, category_assistance, category_feature
import random, os


# Create your views here.
@login_required(login_url='/accounts/login')
def portalDashboard(request):
	profile_details = details.objects.get(userId=request.user.id)
	return render(request, 'portal_dashboard.html', {"profile_details":profile_details})

@login_required(login_url='/accounts/login')
def portalSettingPage(request):
	profile_details = details.objects.get(userId=request.user.id)
	profile_address = address_info.objects.get(userId=request.user.id)
	profile_passwords = password_manager.objects.filter(userId=request.user.id, status=1)
	list_of_industry_type = industry_type.objects.all()
	list_of_password_category = password_category.objects.all();
	list_of_invoice = invoice.objects.filter(userId=request.user.id, status=1).order_by('-create_date')
	if request.method == 'POST':
		profile_details.first_name = request.POST['first_name']
		profile_details.last_name = request.POST['last_name']
		profile_details.email = request.POST['email']
		profile_details.phone = request.POST['phone_num']
		profile_details.company_name = request.POST['company_name']
		if request.POST['industry_type'] != "0":
			industry_type_selected = industry_type.objects.get(pk=request.POST['industry_type'])
			profile_details.industry_type = industry_type_selected
		else:
			profile_details.industry_type = None
		profile_details.website = request.POST['website']
		request_file = request.FILES['profile_picture'] if 'profile_picture' in request.FILES else None
		if request_file:
			split_tup = os.path.splitext(request_file.name)
			file_extension = split_tup[1]
			random_number = random.randint(0,1000)
			fs = FileSystemStorage()
			file_name = "prof_pic/profile_picture_"+str(request.user.id)+"_"+str(random_number)+""+str(file_extension)
			ProfPic = fs.save(file_name, request_file)
			profile_details.profile_picture = ProfPic

		profile_details.save()

		profile_address.street = request.POST['street']
		profile_address.state = request.POST['state']
		profile_address.country = request.POST['country']
		profile_address.city = request.POST['city']
		profile_address.zip_code = request.POST['zip_code']
		profile_address.save()
	return render(request, 'setting_profile_page.html', {"profile_details": profile_details, "list_of_invoice":list_of_invoice, "profile_passwords":profile_passwords, "industry_type_list":list_of_industry_type, "profile_address":profile_address, "password_category":list_of_password_category, "site_url": settings.SITE_URL})

@login_required(login_url='/accounts/login')
def edit_profile(request):
	if request.method == 'POST':
		print("post")
	return 0

@login_required(login_url='/accounts/login')
def SettingPasswordPage(request):
	profile_details = details.objects.get(userId=request.user.id)

	return render(request, 'setting_password_page.html', {"profile_details": profile_details, "site_url": settings.SITE_URL})

@login_required(login_url='/accounts/login')
def SettingInvoicePage(request):
	profile_details = details.objects.get(userId=request.user.id)
	list_of_invoice = invoice.objects.filter(userId=request.user.id, status=1).order_by('-create_date')
	return render(request, 'setting_invoice_page.html', {"profile_details": profile_details, "list_of_invoice":list_of_invoice})

@login_required(login_url='/accounts/login')
def SettingPasswordManagementPage(request):
	profile_details = details.objects.get(userId=request.user.id)
	list_of_password_category = password_category.objects.all();
	profile_passwords = password_manager.objects.filter(userId=request.user.id, status=1)
	return render(request, 'setting_password_management_page.html', {"profile_details": profile_details, "password_category":list_of_password_category, "profile_passwords":profile_passwords})

@login_required(login_url='/accounts/login')
def SettingFaqsPage(request):
	profile_details = details.objects.get(userId=request.user.id)
	return render(request, 'setting_faqs_page.html', {"profile_details": profile_details})


# admin side
@login_required(login_url='/accounts/login')
def portalAdminDashboard(request):
	returnVal = {}
	profile_details = details.objects.get(userId=request.user.id)
	open_tasks = task.objects.filter(is_delete=0, status="OPEN")
	in_progress_tasks = task.objects.filter(is_delete=0, status="IN PROGRESS")
	approval_tasks = task.objects.filter(is_delete=0, status="FOR APPROVAL")
	all_tickets = issue.objects.filter(is_delete=0).exclude(ticket_status="CLOSED")
	all_task = task.objects.filter(is_delete=0).exclude(status="CLOSED")
	returnVal['profile_details'] = profile_details
	returnVal['open_task'] = open_tasks
	returnVal['in_progress_tasks'] = in_progress_tasks
	returnVal['approval_tasks'] = approval_tasks
	returnVal['all_tickets'] = all_tickets
	returnVal['all_task'] = all_task
	return render(request, 'admin_templates/admin_dashboard.html', returnVal)

@login_required(login_url='/accounts/login')
def portalAdminTicketDashboard(request):
	returnVal = {}
	profile_details = details.objects.get(userId=request.user.id)
	open_ticket = issue.objects.filter(is_delete=0, ticket_status="OPEN")
	in_progress_ticket = issue.objects.filter(is_delete=0, ticket_status="IN PROGRESS")
	to_be_tested_ticket = issue.objects.filter(is_delete=0, ticket_status="TO BE TESTED")
	all_tickets = issue.objects.filter(is_delete=0).exclude(ticket_status="CLOSED")
	high_tickets = issue.objects.filter(is_delete=0, severity="HIGH").exclude(ticket_status="CLOSED")
	returnVal['sidebar'] = "ticket"
	returnVal['profile_details'] = profile_details
	returnVal['open_ticket'] = open_ticket
	returnVal['in_progress_ticket'] = in_progress_ticket
	returnVal['to_be_tested_ticket'] = to_be_tested_ticket
	returnVal['all_tickets'] = all_tickets
	return render(request, 'admin_templates/tickets/ticket_dashboard.html', returnVal)

@login_required(login_url='/accounts/login')
def portalAdminTicketList(request):
	returnVal = {}
	profile_details = details.objects.get(userId=request.user.id)
	# list_of_tickets = issue.objects.raw("SELECT * FROM tickets_issue a INNER JOIN accounts_details b ON a.`userId_id` = b.`userId_id` WHERE STATUS = 0")
	all_tickets = issue.objects.filter(is_delete=0).exclude(ticket_status="CLOSED")
	returnVal['sidebar'] = "ticket"
	returnVal['profile_details'] = profile_details
	returnVal['all_tickets'] = all_tickets
	return render(request, 'admin_templates/tickets/ticket_list.html', returnVal)

@login_required(login_url='/accounts/login')
def getAdminTicketDetails(request, ticket_id):
	returnVal = {}
	ticket = issue.objects.get(pk=ticket_id)
	profile_details = details.objects.get(userId=request.user.id)
	private_comment = issue_comment.objects.filter(issue=ticket_id, is_delete=0, is_private=1)
	ticket_comment_attachments = issue_comment_file.objects.filter(issue=ticket_id, is_delete=0)
	attachments = issue_file.objects.filter(issue=ticket_id, is_delete=0)
	client_comment = issue_comment.objects.filter(issue=ticket_id, is_delete=0, is_private=0)
	list_responders = details.objects.filter(account_type_id=2)
	ticket_responders = issue_responders.objects.filter(issue=ticket_id)

	if request.method == 'POST':
		userInstance = details.objects.get(userId=request.user.id)
		ticket_comment = issue_comment()
		private_comment = request.POST.get('private_ticket_comment', False)
		if private_comment:
			ticket_comment.comment = request.POST.get('private_ticket_comment', False)
		else:
			ticket_comment.comment = request.POST.get('client_ticket_comment', False)
		ticket_comment.owner = userInstance
		ticket_comment.issue = ticket
		ticket_comment.is_private = request.POST['is_private']
		ticket_comment.save()
		request_file = request.FILES['private_attachments'] if 'private_attachments' in request.FILES else None
		client_request_file = request.FILES['ticket_client_attachments'] if 'ticket_client_attachments' in request.FILES else None
		if request_file:
			for f in request.FILES.getlist('private_attachments'):
				ticket_comment_file = issue_comment_file()
				ticket_comment_file.commentId = ticket_comment
				ticket_comment_file.comment_file_name = f.name
				ticket_comment_file.issue = ticket
				split_tup = os.path.splitext(f.name)
				file_extension = split_tup[1]
				random_number = random.randint(0,1000)
				fs = FileSystemStorage()
				file_name = "tickets_attachments/id_"+str(ticket_id)+"_"+str(random_number)+""+str(file_extension)
				comment_file = fs.save(file_name, f)
				ticket_comment_file.comment_file = comment_file
				ticket_comment_file.save()
		elif client_request_file:
			for f in request.FILES.getlist('ticket_client_attachments'):
				ticket_comment_file = issue_comment_file()
				ticket_comment_file.commentId = ticket_comment
				ticket_comment_file.comment_file_name = f.name
				ticket_comment_file.issue = ticket
				split_tup = os.path.splitext(f.name)
				file_extension = split_tup[1]
				random_number = random.randint(0,1000)
				fs = FileSystemStorage()
				file_name = "tickets_attachments/id_"+str(ticket_id)+"_"+str(random_number)+""+str(file_extension)
				comment_file = fs.save(file_name, f)
				ticket_comment_file.comment_file = comment_file
				ticket_comment_file.save()
		return redirect ('getAdminTicketDetails', ticket_id)

	returnVal['sidebar'] = "ticket"
	returnVal['profile_details'] = profile_details
	returnVal['ticket'] = ticket
	returnVal['private_comment'] = private_comment
	returnVal['ticket_comment_attachments'] = ticket_comment_attachments
	returnVal['attachments'] = attachments
	returnVal['client_comment'] = client_comment
	returnVal['list_responders'] = list_responders
	returnVal['ticket_responders'] = ticket_responders
	return render(request, 'admin_templates/tickets/ticket_detailed.html', returnVal)


@login_required(login_url='/accounts/login')
def portalAdminTaskDashboard(request):
	returnVal = {}
	profile_details = details.objects.get(userId=request.user.id)
	open_tasks = task.objects.filter(is_delete=0, status="OPEN")
	in_progress_tasks = task.objects.filter(is_delete=0, status="IN PROGRESS")
	approval_tasks = task.objects.filter(is_delete=0, status="FOR APPROVAL")
	all_task = task.objects.filter(is_delete=0).exclude(status="CLOSED")
	returnVal['profile_details'] = profile_details
	returnVal['open_task'] = open_tasks
	returnVal['in_progress_tasks'] = in_progress_tasks
	returnVal['approval_tasks'] = approval_tasks
	returnVal['all_task'] = all_task
	return render(request, 'admin_templates/task/task_dashboard.html', returnVal)

@login_required(login_url='/accounts/login')
def portalAdminTaskList(request):
	profile_details = details.objects.get(userId=request.user.id)
	task_list = task.objects.filter(is_delete=0)
	return render(request, 'admin_templates/task/task_list.html', {"profile_details": profile_details, "task_list":task_list, "base_url":settings.SITE_URL})

@login_required(login_url='/accounts/login')
def portalAdmintaskDetails(request, task_id):
	returnVal = {}
	profile_details = details.objects.get(userId=request.user.id)
	task_details = task.objects.get(pk=task_id)
	task_owner = details.objects.get(pk=task_details.owner.pk)
	comment_list = task_comment.objects.filter(task=task_id, is_private=0)
	comment_is_private = task_comment.objects.filter(task=task_id, is_private=1)
	comment_attachments = task_comment_file.objects.filter(task=task_id)
	task_attachment = task_file.objects.filter(task=task_id)
	list_responders = details.objects.filter(account_type_id=2)
	task_responder = task_responders.objects.filter(task=task_id)

	if request.method == 'POST':
		userInstance = details.objects.get(userId=request.user.id)
		task_new_comment = task_comment()
		task_comment_form_field = request.POST.get('task_comment', False);
		task_client_comment = request.POST.get('task_client_comment', False)
		if task_comment_form_field:
			task_new_comment.comment = request.POST.get('task_comment', False)
		elif task_client_comment:
			task_new_comment.comment = request.POST.get('task_client_comment', False)
		else:
			task_new_comment.comment = ""
		
		task_new_comment.owner_accountDetails = userInstance
		task_new_comment.task = task_details
		task_new_comment.is_private = request.POST['is_private']
		task_new_comment.save()



		request_file = request.FILES['task_attachments'] if 'task_attachments' in request.FILES else None
		request_client_file = request.FILES['task_client_attachments'] if 'task_client_attachments' in request.FILES else None
		if request_file:
			for f in request.FILES.getlist('task_attachments'):
				task_new_comment_file = task_comment_file()
				task_new_comment_file.comment = task_new_comment
				task_new_comment_file.name = f.name
				split_tup = os.path.splitext(f.name)
				file_extension = split_tup[1]
				random_number = random.randint(0,1000)
				fs = FileSystemStorage()
				file_name = "tasks_attachments/id_"+str(task_id)+"_"+str(random_number)+""+str(file_extension)
				comment_file = fs.save(file_name, f)
				task_new_comment_file.comment_file = comment_file
				task_new_comment_file.task = task_details
				task_new_comment_file.save()
		elif request_client_file:
			for f in request.FILES.getlist('task_client_attachments'):
				task_new_comment_file = task_comment_file()
				task_new_comment_file.comment = task_new_comment
				task_new_comment_file.name = f.name
				split_tup = os.path.splitext(f.name)
				file_extension = split_tup[1]
				random_number = random.randint(0,1000)
				fs = FileSystemStorage()
				file_name = "tasks_attachments/id_"+str(task_id)+"_"+str(random_number)+""+str(file_extension)
				comment_file = fs.save(file_name, f)
				task_new_comment_file.comment_file = comment_file
				task_new_comment_file.task = task_details
				task_new_comment_file.save()
		return redirect ('portalAdmintaskDetails', task_id)
		
	returnVal['profile_details'] = profile_details
	returnVal['detail'] = task_details
	returnVal['task_attachments'] = task_attachment
	returnVal['task_owner'] = task_owner
	returnVal['sidebar'] = "task"
	returnVal['comment_attachments'] = comment_attachments
	returnVal['client_comments'] = comment_list
	returnVal['comment_is_private'] = comment_is_private
	returnVal['list_responders'] = list_responders
	returnVal['task_responder'] = task_responder

	return render(request, 'admin_templates/task/task_detailed.html', returnVal)

@login_required(login_url='/accounts/login')
def portalAdminServicesDashboard(request):
	returnVal = {}
	profile_details = details.objects.get(userId=request.user.id)
	returnVal['just_loop'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	returnVal['sidebar'] = "services"
	returnVal['profile_details'] = profile_details
	return render(request, 'admin_templates/services/admin_services_dashboard.html', returnVal)

@login_required(login_url='/accounts/login')
def portalAdminServicesList(request):
	returnVal = {}
	profile_details = details.objects.get(userId=request.user.id)
	category_theme = task_cetegory_theme.objects.filter(is_delete=0)
	category = task_category.objects.filter(is_delete=0)
	sub_category = task_sub_category.objects.filter(is_delete=0)
	returnVal['sidebar'] = "services"
	returnVal['profile_details'] = profile_details
	returnVal['category_theme'] = category_theme
	returnVal['categories'] = category
	returnVal['sub_categories'] = sub_category
	return render(request, 'admin_templates/services/admin_services_list.html', returnVal)

@login_required(login_url='/accounts/login')
def portalAdminServiceThemeDetail(request, category_theme_id):
	returnVal = {}
	profile_details = details.objects.get(userId=request.user.id)
	category_theme = task_cetegory_theme.objects.get(pk=category_theme_id)
	category = task_category.objects.filter(is_delete=0, theme=category_theme_id, status=1)
	category_theme_assistance = category_assistance.objects.filter(is_delete=0, category_theme=category_theme_id)
	returnVal['sidebar'] = "services"
	returnVal['profile_details'] = profile_details
	returnVal['category_theme'] = category_theme
	returnVal['categories'] = category
	returnVal['category_theme_assistance'] = category_theme_assistance
	return render(request, 'admin_templates/services/admin_services_theme_detailed.html', returnVal)

@login_required(login_url='accounts/login')
def portalAdminServiceCategoryDetail(request, category_id):
	returnVal = {}
	profile_details = details.objects.get(userId=request.user.id)
	category = task_category.objects.get(pk=category_id)
	category_features = category_feature.objects.filter(category=category_id)
	sub_category = task_sub_category.objects.filter(category=category_id)
	returnVal['sidebar'] = "services"
	returnVal['profile_details'] = profile_details
	returnVal['category'] = category
	returnVal['category_features'] = category_features
	returnVal['sub_categories'] = sub_category
	return render(request, 'admin_templates/services/admin_services_category_detailed.html', returnVal)
