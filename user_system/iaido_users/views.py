from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            # Handle invalid login credentials
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        print(113)
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('iaido')

@login_required
def index(request):
    """ Instead of the login_required decorator one could also use
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")"""
    return HttpResponse("Hello, world. You're at the polls index.")
