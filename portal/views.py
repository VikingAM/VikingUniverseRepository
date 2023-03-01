from django.shortcuts import render

# Create your views here.
def portalDashboard(request):
	return render(request, 'portal_dashboard.html')