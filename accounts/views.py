from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from login_required import login_not_required
from base.forms import SignUpForm


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
    #store temporary data input
    #show link has been sent to your email
    #execute email verifivation 
    #take the user to the login view after email verification is complete
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        context = {"form" : form}
        if form.is_valid():
            form.save()
            # Set a flag to indicate successful registration
            condition = True
            return render(request, "register.html", {'condition': condition})
        return render(request, "register.html", context)
    elif request.method == "GET":
        context = {"form" : form}
        return render(request, "register.html", context)
    


    return render(request, "register.html")

#Logout
def logout_user(request):
    logout(request)
    return redirect('home')
