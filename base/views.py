from django.shortcuts import render,redirect
from accounts.models import Account
from login_required import login_not_required
from django.contrib.auth.hashers import make_password
from .forms import UserForm
from django.db import transaction
from .middlewares import CustomException

# Create your views here.
@login_not_required
def homepage(request):
    return render(request, "index.html")

def dashboard(request):
    if request.method == "GET":
        try:
            user = request.user
            details = Account.objects.get(user = user)
            return render(request, "dashboard.html", {'context':details})
        except:
            #User have not finished account creation then redirect to account registration
            return redirect('profile')
    elif request.method=="POST":
        pass
    
def profile(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, "test.html", {"form": form})

    if request.method == 'POST':
        user = request.user
        try:
            account = Account.objects.get(user=user)
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                with transaction.atomic():
                    new_account = form.save(commit=False)
                    new_account.save(force_insert=True)
                return redirect('dashboard')
        except Account.DoesNotExist:
            raise CustomException("You already have an account")

