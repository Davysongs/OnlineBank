from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from login_required import login_not_required
from accounts.forms import SignUpForm
from .forms import UserForm
from django.db import transaction
from base.middlewares import CustomException
from accounts.models import Account


# Create your views here.
#login 
@login_not_required
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email= email, password= password)
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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        context = {"form" : form}
        if form.is_valid():
            form.save()
            condition = True
            return render(request, "register.html", {'condition': condition})

    
    if request.method == "GET":
        form = SignUpForm()
        return render(request, "register.html", {"form" : form})


#Logout
def logout_user(request):
    logout(request)
    return redirect('home')


def profile(request):
    user = request.user

    if request.method == "GET":
        try:
            account_details = Account.objects.get(user=user)
            form = UserForm(instance=account_details)  # Populate the form with existing data
        except Account.DoesNotExist:
            form = UserForm()
        return render(request, "profile.html", {"form": form})

    if request.method == 'POST':
        try:
            account_details = Account.objects.get(user=user)
            form = UserForm(request.POST, request.FILES, instance=account_details)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        except Account.DoesNotExist:
            raise CustomException("You already have an account")

