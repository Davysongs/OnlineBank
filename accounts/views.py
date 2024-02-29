from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from login_required import login_not_required

# Create your views here.
#login 
@login_not_required
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username= username, password= password)
            if user is not None:
                login(request,user)
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
            else:
                messages.info(request,"Username or password is incorrect")
                return render(request, "login.html")
        return render(request, "login.html")

#sign up view
@login_not_required
def register_view(request):
    return render(request, "register.html")

#Logout
def logout_user(request):
    logout(request)
    return redirect('home')