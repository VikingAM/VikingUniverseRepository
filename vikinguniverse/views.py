from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404


def landingpage(request):
	return render(request, 'landing_page.html')

def pricingPage(request):
	return render(request, 'pricing.html')

def FAQs(request):
	return render(request, 'FAQs.html')

def LandingServicesPage(request):
	return render(request, 'services.html')

def ServicesDesignArt(request):
	return render(request, 'services/design_arts.html')

def ServicesDigitalMarketing(request):
	return render(request, 'services/digital_marketing.html')

def ServicesWritingTranslation(request):
	return render(request, 'services/writing_translation.html')

def ServicesDevelopmentIT(request):
	return render(request, 'services/development_IT.html')

def ServicesBusinessAssistance(request):
	return render(request, 'services/business_assistance.html')

def ServicesFinancialDataAnalytics(request):
	return render(request, 'services/financial_data.html')

def aboutPage(request):
	return render(request, 'about.html')