from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from accounts.models import details, address_info, user_validation, password_reset_code, password_manager, password_category, credit_score, invoice
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
	from_email = 'no-reply@vikinguniverse.com'
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
			otp_random = random.randint(1000, 9999)
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
			subject = 'Viking Universe password reset OTP'
			html_message = render_to_string('mail_password_reset_otp.html', {'UserFullname': fullname, 'OTP': otp_random, "site_url": settings.SITE_URL})
			plain_message = strip_tags(html_message)
			from_email = 'no-reply@vikinguniverse.com'
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

	verification_id = request.POST['verification_id'];

	verification_details = user_validation.objects.get(pk=verification_id)
	UserDetails = details.objects.get(userId=verification_details.userId)
	verification_link = verification_details.code
	fullname = UserDetails.last_name+", "+UserDetails.first_name
	client_email = UserDetails.email

	try:
		send_email(fullname, verification_link, client_email)
		data['success'] = 1
	except:
		data['success'] = 0
	
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

@login_required(login_url='accounts/login')
def creditScoreDashboard(request):
	profile_details = details.objects.get(userId=request.user.id)
	userId = request.user.id
	Available_credit = 0
	total_credits_used = 0

	credit_list = credit_score.objects.filter(userId=userId).order_by('-create_date')
	Available_credit = sum(credit_list.values_list('credit', flat=True))

	history_list = []
	for credit_detail in credit_list:
		detail = {}
		detail['credit'] = credit_detail.credit
		detail['create_date'] = credit_detail.create_date
		detail['title'] = str(credit_detail.credit)+" Credit Added!"
		detail['desc'] = "Credit Added to account!"
		detail['type'] = "0"
		history_list.append(detail)

	return render(request, "credit_score_dashboard.html", {"AVC": Available_credit, "TCU": total_credits_used, "history_list":history_list, "profile_details":profile_details })

@login_required(login_url='accounts/login')
def creditScoreAdd(request):
	data = {}
	data['status_code'] = 0

	if request.method == 'POST':
		custom_amount = request.POST['custom_amount']
		credit = request.POST['credits']
		userId = request.POST['userId']
		try:
			userInstance = User.objects.get(pk=userId)
		except:
			data['status_code'] = 0
			data['status_msg'] = "UserId Error!"
			return JsonResponse(data, safe=False)

		new_credit_score = credit_score()
		new_credit_score.amount = custom_amount
		new_credit_score.credit = credit
		new_credit_score.userId = userInstance
		new_credit_score.paid = 1 #set to 1 for now

		new_invoice = invoice()
		new_invoice.userId = userInstance
		new_invoice.payment_method = "Card"
		new_invoice.product_name = "Custom Credit"
		new_invoice.product_description = "Custom "+custom_amount+" Credit"
		new_invoice.amount = custom_amount
		new_invoice.quantity = 1
		try:
			new_credit_score.save()
			new_invoice.save()
			data['status_code'] = 1
			data['status_msg'] = "Success!"
		except:
			data['status_code'] = 0
			data['status_msg'] = "Error on saving credit Score!"
		return JsonResponse(data, safe=False)
	else:
		return JsonResponse(data, safe=False)
	
	


@login_required(login_url='accounts/login')
def invoiceDetailsGetById(request):
	data = {}
	data['status_code'] = 0
	if request.method == 'POST':
		invoiceId = request.POST['invoiceId']
		invoiceDetails = invoice.objects.get(pk=invoiceId)
		address_details = address_info.objects.get(userId=invoiceDetails.userId.pk)
		complete_address = str(address_details.street)+" "+str(address_details.city)+" "+str(address_details.state)+" "+str(address_details.country)
		data['purchase_date'] = invoiceDetails.create_date.strftime("%B %d, %Y")
		data['payment_method'] = invoiceDetails.payment_method
		data['customer_number'] = invoiceDetails.userId.pk
		data['customer_address'] = complete_address
		data['product_name'] = invoiceDetails.product_name
		data['product_qty'] = invoiceDetails.quantity
		data['product_desc'] = invoiceDetails.product_description
		data['product_tax'] = 0
		data['product_total'] = invoiceDetails.amount
		data['status_code'] = 1


	return JsonResponse(data, safe=False)
