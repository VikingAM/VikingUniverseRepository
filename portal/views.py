from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from accounts.models import details, address_info, user_validation, industry_type, password_manager, password_category, invoice
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
			file_name = "profile_picture_"+str(request.user.id)+"_"+str(random_number)+""+str(file_extension)
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