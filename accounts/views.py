from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from login_required import login_not_required
from accounts.forms import SignUpForm
from .forms import UserForm
from django.http import HttpResponseRedirect
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
    try:
        details = Account.objects.get(user=user)
    except Account.DoesNotExist:
        raise CustomException("Your account is not configured properly")

    if request.method == "GET":
        form = UserForm()  # Create a form instance
        if details.pin:  # Check if the user has a PIN
            return render(request, 'profile.html', {'details': details, 'form': form})
        else:
            return render(request, 'update.html', {'form': form})

    elif request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=details)  # Populate form with existing data
        if form.is_valid():
            form.save()  # Save the form data
            return redirect('dashboard')
        else:
            # Form is not valid, handle the error scenario here
            # You might want to render the profile page again with the form and error messages
            # For example
            return render(request, 'update.html', {'details': details, 'form': form})

