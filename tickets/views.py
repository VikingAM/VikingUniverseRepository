from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.http import JsonResponse
from tickets.models import issue, issue_type
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

	new_issue.title = request.POST['title']
	new_issue.description = request.POST['description']
	new_issue.issue_type = issue_type_instance
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
	list_of_issue_ticket = issue.objects.all();
	profile_details = details.objects.get(userId=request.user.id)
	return render(request, 'ticketing_page.html', {"issue_types":issue_types, "issue_tickets": list_of_issue_ticket, "profile_details": profile_details})