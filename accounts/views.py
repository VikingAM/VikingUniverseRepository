from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from accounts.models import details, address_info, user_validation
import uuid

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
			if len(CheckUserByEmail == 0):
				try:
					newUser = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'])
					newUserDetails = details()
					newUserDetails.userId = newUser
					newUserDetails.last_name = data['last_name']
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
					fullname = data['last_name']+", "+data['first_name']
					verfication_link = "www.vikinguniverse.com/account/verify/"+validationCode.verification_code
					send_email(fullname, verfication_link)
					redirect('verification', {'hashcode': validationCode.verification_code})
				except:
					data['error_msg'] = "An Error occur on creating a profile."
			else:
				data['error_msg'] = "Email already been use!"
		else:
			data['error_msg'] = "Username already been use!"
		# user = User.objects.create_user(username=username, email=emailForm, password=passwordForm, first_name=firstNameForm, last_name=lastnameForm)
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

def send_email(fullname, verification_link):
	data = {}
	subject = 'Viking Universer Email Verification'
	html_message = render_to_string('mail_template.html', {'UserFullname': fullname, 'verification_link': verification_link})
	plain_message = strip_tags(html_message)
	from_email = 'william.crumb@vikingassetmanagement.com'

	msg = EmailMultiAlternatives(subject, plain_message, from_email, [to])
	msg.attach_alternative(html_content, "text/html")

	try:
		msg.send()
	except BadHeaderError:
		data['status'] = "error!"
	return True

def email_verfication_template(request):
	return render(request, 'mail_verification.html')

def accountVerfiy(request):
	return True

def accountVerificationPage(request, verification_id):
	print(verification_id)
	return render(request, 'register_verification.html')