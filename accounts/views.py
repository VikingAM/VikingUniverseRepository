from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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
			return render(request, 'account_index.html')
		else:
			return render(request, 'login.html')
	else:
		return render(request, 'login.html')

def accountLogout(request):
	logout(request)
	return redirect('/')

def accountCreate(request):
	if request.method == 'POST':
		return render(request, 'account_creation.html')
	else:
		return render(request, 'account_creation.html')