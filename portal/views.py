from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import details, address_info, user_validation, industry_type, password_manager


# Create your views here.
@login_required(login_url='/accounts/login')
def portalDashboard(request):
	return render(request, 'portal_dashboard.html')

@login_required(login_url='/accounts/login')
def portalSettingPage(request):
	profile_details = details.objects.get(userId=request.user.id)
	profile_address = address_info.objects.get(userId=request.user.id)
	profile_passwords = password_manager.objects.filter(userId=request.user.id, status=1)
	list_of_industry_type = industry_type.objects.all()
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
		profile_details.save()

		profile_address.street = request.POST['street']
		profile_address.state = request.POST['state']
		profile_address.country = request.POST['country']
		profile_address.city = request.POST['city']
		profile_address.zip_code = request.POST['zip_code']
		profile_address.save()
	return render(request, 'setting_page.html', {"profile_details": profile_details, "profile_passwords":profile_passwords, "industry_type_list":list_of_industry_type, "profile_address":profile_address, "site_url": settings.SITE_URL})

@login_required(login_url='/accounts/login')
def ticketingPage(request):
	return render(request, 'ticketing_page.html')

@login_required(login_url='/accounts/login')
def edit_profile(request):
	if request.method == 'POST':
		print("post")
	return 0