import os
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from flask import Flask, jsonify, json, request, current_app
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from payment.models import products, sessions
from accounts.models import credit_score



stripe.api_key = settings.STRIPE_SECRET_KEY
app = Flask(__name__,
            static_url_path='',
            static_folder='stripe_project')
YOUR_DOMAIN = settings.SITE_URL

@csrf_exempt
def paymentCheckout(request):


	if request.method == 'POST':
		product_details = products.objects.get(pk=request.POST['product_id'])
		try:
			# checkout_session = stripe.checkout.Session.create(line_items=[{'price': product_details.stripeId, 'quantity': 1,},],mode='subscription',success_url=settings.SITE_URL +'/success?session_id={CHECKOUT_SESSION_ID}',cancel_url=settings.SITE_URL + '/cancel',)
			checkout_session = stripe.checkout.Session.create(line_items=[{'price': product_details.stripeId, 'quantity': 1,},],mode='subscription',success_url=YOUR_DOMAIN +'/payments/success?session_id={CHECKOUT_SESSION_ID}&prod_id='+str(product_details.pk),cancel_url=YOUR_DOMAIN + '/payments/cancel',)
			print(checkout_session)
			return redirect(checkout_session.url)
		except Exception as e:
			return "Server error", 500
	else:
		return render(request, 'success.html')

@login_required(login_url='/accounts/login')
def paymentSuccess(request):
	print(request.GET['session_id'])
	product_instance = products.objects.get(pk=request.GET['prod_id'])
	new_session = sessions()
	new_session.sessionId = request.GET['session_id']
	new_session.productId = product_instance
	new_session.userId = request.user
	new_session.save()

	new_credit = credit_score()
	new_credit.amount = product_instance.price
	new_credit.paid = 1
	new_credit.status = 1
	new_credit.userId = request.user
	new_credit.credit = product_instance.credits
	new_credit.sessionId = new_session
	new_credit.save()


	return render(request, 'success.html', {})

@login_required(login_url='/accounts/login')
def paymentCancel(request):
	return render(request, 'cancel.html', {})