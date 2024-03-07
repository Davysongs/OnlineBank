from django.shortcuts import render,redirect
from accounts.models import Account
from login_required import login_not_required
from django.contrib.auth.hashers import make_password
import random
import string



# Create your views here.
@login_not_required
def homepage(request):
    return render(request, "index.html")

def dashboard(request):
    if request.method == "GET":
        try:
            user_no = request.user.account_no
            details = Account.objects.get(account_no = user_no)
            return render(request, "dashboard.html", {'context':details})
        except:
            #User have not finished account creation then redirect to account registration
            return redirect('profile')
    elif request.method=="POST":
        pass

def generate_account_number():
    while True:
        # Generate a random string of numbers
        account_no = ''.join(random.choices(string.digits, k=10))

        # Check if the generated number already exists in the Account model
        if not Account.objects.filter(account_no=account_no).exists():
            # If the number doesn't exist, return it
            return account_no
    
def profile(request):
    if request.method == "GET":
        return render(request, "profile.html")
    if request.method == 'POST':
        uid=request.user.email
        print(uid)
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        postcode = request.POST.get('postcode')
        state = request.POST.get('state')
        pin = request.POST.get('pin1')
        print(pin, type(pin))
        number =  generate_account_number() 
        user = request.user
            # If the user doesn't have an account, create a new one
        account = Account.objects.create(
            user=user,
            pin=make_password(pin),    
            account_no = number,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            country=country,
            postcode=postcode,
            state=state,
            balance=0,
            )
        return redirect('dashboard')

