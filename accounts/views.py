from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from accounts.models import details, address_info, user_validation
import uuid, datetime

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
			return redirect('LandingPage')
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
				except:
					data['error_msg'] = "An Error occur on creating a User."
					return render(request, 'register.html', data)

				try:
					newUserAddressInfo = address_info()
					newUserAddressInfo.userId = newUser
					newUserAddressInfo.save()

					validationCode = user_validation();
					validationCode.userId = newUser
					validationCode.verification_code = uuid.uuid4().hex
					validationCode.save()
				except:
					data['error_msg'] = "An Error occur on creating a profile."
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

def email_verfication_template(request):
	return render(request, 'mail_verification.html')

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
	print(UserDetails)
	fullname = UserDetails.last_name+", "+UserDetails.first_name
	return render(request, 'register_verification.html', {"fullname":fullname, "code":verification_id})

def resendVerification(request):
	data = {}
	data['success'] = 1
	return JsonResponse(data, safe=False)
