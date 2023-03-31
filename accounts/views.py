from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from accounts.models import details, address_info, user_validation, password_reset_code, password_manager, password_category
import uuid, datetime, random

# Create your views here.
def accountIndex(request):
	return render(request, 'account_index.html')

def accountLogin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			print(request.GET.get('next'))
			if request.GET.get('next') != None:
				return redirect(request.GET.get('next'),  '/portal')
			return redirect('portalDashboard')
		else:
			return render(request, 'login.html' , {"error_msg": "username and password does not match!", "username":username})
	else:
		return render(request, 'login.html', {"error_msg": "", "username": ""})

def accountLogout(request):
	logout(request)
	return redirect('LandingPage')

def accountCreate(request):
	data = {}
	if request.method == 'POST':
		data['error_msg'] = ""
		data['company_name'] = request.POST['company_name']
		data['first_name'] = request.POST['first_name']
		data['last_name'] = request.POST['last_name']
		data['email'] = request.POST['email']
		data['phone_num'] = request.POST['phone_num']
		data['password'] = request.POST['password']
		data['username'] = request.POST['username']
		CheckUserByUsername = User.objects.filter(username=data['username'])
		Existing = 0
		if len(CheckUserByUsername) == 0:
			CheckUserByEmail = User.objects.filter(email=data['email'])
			if len(CheckUserByEmail) == 0:
				try:
					newUser = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'])
					newUserDetails = details()
					newUserDetails.userId = newUser
					newUserDetails.last_name = data['last_name']
					newUserDetails.first_name = data['first_name']
					newUserDetails.email = data['email']
					newUserDetails.phone = data['phone_num']
					newUserDetails.company_name = data['company_name']
					newUserDetails.save()

					newUserAddressInfo = address_info()
					newUserAddressInfo.userId = newUser
					newUserAddressInfo.save()

					validationCode = user_validation();
					validationCode.userId = newUser
					validationCode.verification_code = uuid.uuid4().hex
					validationCode.save()
				except:
					data['error_msg'] = "An Error occur on creating a User."
					return render(request, 'register.html', data)
				
				fullname = data['last_name']+", "+data['first_name']
				verification_link = validationCode.verification_code
				send_email(fullname, verification_link, newUserDetails.email)
				return redirect('accountVerificationPage', validationCode.verification_code)				
				# return render(request, 'register.html', data)
			else:
				data['error_msg'] = "Email already been use!"
				return render(request, 'register.html', data)
		else:
			data['error_msg'] = "Username already been use!"
			return render(request, 'register.html', data)
	else:
		data['error_msg'] = ""
		data['company_name'] = ""
		data['first_name'] = ""
		data['last_name'] = ""
		data['email'] = ""
		data['phone_num'] = ""
		data['password'] = ""
		data['username'] = ""
		return render(request, 'register.html', data)

def send_email(fullname, verification_link, client_email):
	data = {}
	subject = 'Viking Universer Email Verification'
	html_message = render_to_string('mail_verification.html', {'UserFullname': fullname, 'verification_link': verification_link, "site_url": settings.SITE_URL})
	plain_message = strip_tags(html_message)
	from_email = 'william.crumb@vikingassetmanagement.com'
	msg = EmailMultiAlternatives(subject, plain_message, from_email, [client_email])
	msg.attach_alternative(html_message, "text/html")

	try:
		msg.send()
	except BadHeaderError:
		print("error on sending email.")
	return True

def passwordResetOtp(request):
	data = {}
	data['status'] = "OTP email failed"
	if request.method == 'POST':
		Userinstance = User.objects.get(pk=request.POST['userId'])
		user = authenticate(request, username=Userinstance.username, password=request.POST['current_password'])
		if user is not None:
			UserDetails = details.objects.get(userId=request.POST['userId'])
			otp_random = random.randint(100000, 999999)
			list_of_password_otp = password_reset_code.objects.filter(userId=request.POST['userId'], status=0)
			if len(list_of_password_otp) > 0:
				for password_otp in list_of_password_otp:
					password_otp.status = 1
					password_otp.save()
			reset_password = password_reset_code()
			reset_password.code = otp_random
			reset_password.userId = Userinstance
			reset_password.save()
			client_email = UserDetails.email

			fullname = UserDetails.last_name+", "+UserDetails.first_name
			subject = 'Viking Universer password reset OTP'
			html_message = render_to_string('mail_password_reset_otp.html', {'UserFullname': fullname, 'OTP': otp_random, "site_url": settings.SITE_URL})
			plain_message = strip_tags(html_message)
			from_email = 'william.crumb@vikingassetmanagement.com'
			msg = EmailMultiAlternatives(subject, plain_message, from_email, [client_email])
			msg.attach_alternative(html_message, "text/html")

			try:
				msg.send()
				data['status'] = "OTP sent"
			except BadHeaderError:
				data['status'] = "error on sending email."
		else:
			data['status'] = "error on current password!"	
		
	return JsonResponse(data, safe=False)

def accountVerfiy(request, verification_id):
	verification_details = user_validation.objects.get(verification_code=verification_id)
	if verification_details.status == 0:
		UserDatails = details.objects.get(userId=verification_details.userId)
		UserDatails.status = "verified"
		UserDatails.update_date = datetime.datetime.now()
		UserDatails.save()
		verification_details.status = 1
		verification_details.update_date = datetime.datetime.now()
		verification_details.save()
		return render(request, 'register_welcome.html')
	else:
		return redirect('portalDashboard')

def accountVerificationPage(request, verification_id):
	verification_details = user_validation.objects.get(verification_code=verification_id)
	UserDetails = details.objects.get(userId=verification_details.userId)
	fullname = UserDetails.last_name+", "+UserDetails.first_name
	return render(request, 'register_verification.html', {"fullname":fullname, "code":verification_id, "verification_id":verification_details.pk})

def resendVerification(request):
	data = {}
	data['success'] = 1
	return JsonResponse(data, safe=False)

@login_required(login_url='accounts/login')
def changePassword(request):
	data = {}
	otp_details = password_reset_code.objects.get(code=request.POST['otp'])
	if otp_details.userId.pk == int(request.POST['userId']):
		if otp_details.status == 0:
			try:
				u = User.objects.get(pk=request.POST['userId'])
				u.set_password(request.POST['new_password'])
				u.save()
				data['success'] = "Password Updated!"
				otp_details.status = 1
				otp_details.save()
			except:
				data['error_msg'] = "unable to update password"
		else:
			data["error_msg"] = "OTP is not anymore valid!"
	else:
		data["error_msg"] = "OTP does not match!"
	return JsonResponse(data, safe=False)

@login_required(login_url='accounts/login')
def profileNewPassword(request):
	data = {}
	Userinstance = User.objects.get(pk=request.POST['userId'])
	passowrd_name = request.POST['password_name']
	username = request.POST['username']
	password = request.POST['password']
	url = request.POST['url']
	description = request.POST['description']
	data['status'] = 0
	# include encrypt and decrypt soon.
	try:
		new_passowrd = password_manager()
		new_passowrd.userId = Userinstance
		if request.POST['category'] != 0:
			new_passowrd.categoryId = request.POST['category']
		new_passowrd.name = passowrd_name
		new_passowrd.username = username
		new_passowrd.password = password
		new_passowrd.url = url
		new_passowrd.description = description
		new_passowrd.save()
		data['success_msg'] = "successfully added!"
		data['status'] = 1
	except:
		data["error_msg"] = "Error on saving the new password!"

	return JsonResponse(data, safe=False)

@login_required(login_url='accounts/login')
def ProfileNewPasswordGetById(request):
	data = {}
	data['status'] = 0
	try:
		password_manager_details = password_manager.objects.get(pk=request.POST['password_management_id'])
	except:
		data['error_msg'] = "Error on fetching data!"
		return JsonResponse(data, safe=False)

	data['name'] = password_manager_details.name
	data['username'] = password_manager_details.username
	data['password'] = password_manager_details.password
	data['url'] = password_manager_details.url
	data['description'] = password_manager_details.description
	if password_manager_details.category != None:
		data['category'] = password_manager_details.category.id
	else:
		data['category'] = 0
	data['status'] = 1
	return JsonResponse(data, safe=False)

@login_required(login_url='accounts/login')
def ProfileUpdatePassword(request):
	data = {}
	data['status_code'] = 0
	try:
		password_manager_details = password_manager.objects.get(pk=request.POST['password_management_id'])
	except:
		data['status_msg'] = "Error on data does not match!"
		return JsonResponse(data, safe=False)

	try:
		password_category_instance = password_category.objects.get(pk=request.POST['category'])
	except:
		password_category_instance = None

	password_manager_details.name = request.POST['name']
	password_manager_details.username = request.POST['username']
	password_manager_details.password = request.POST['password']
	password_manager_details.url = request.POST['url']
	password_manager_details.description = request.POST['description']
	password_manager_details.category = password_category_instance

	try:
		password_manager_details.save()
		data['status_code'] = 1
		data['status_msg'] = "Update successfully!"
	except:
		data['status_msg'] = "Error on updating data!"
		return JsonResponse(data, safe=False)

	return JsonResponse(data, safe=False)