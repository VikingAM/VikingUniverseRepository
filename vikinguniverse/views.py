from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404


def landingpage(request):
	return render(request, 'landing_page.html')

def pricingPage(request):
	return render(request, 'pricing.html')

def FAQs(request):
	return render(request, 'FAQs.html')

def LandingServicesPage(request):
	return render(request, 'services.html')