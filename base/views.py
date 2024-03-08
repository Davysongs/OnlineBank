from django.shortcuts import render,redirect
from accounts.models import Account
from login_required import login_not_required
from django.contrib.auth.hashers import make_password
from .forms import UserForm
from django.shortcuts import get_object_or_404
import random
import string



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

def generate_account_number():
    while True:
        account_no = ''.join(random.choices(string.digits, k=10))
        # Check if the generated number already exists in the Account model
        if not Account.objects.filter(account_no=account_no).exists():
            # If the number doesn't exist, return it
            return account_no
    
def profile(request):
    form = UserForm()
    if request.method == "GET":
        context = {"form" : form}
        return render(request, "profile.html",context )
    if request.method == 'POST':
        user = request.user
        instance = get_object_or_404(Account, user= user)
        form =  UserForm(request.POST, request.FILES, instance = instance)
        if form.is_valid():
            picture = form.cleaned_data('image')
            phone = form.cleaned_data('phone')
            address = form.cleaned_data('address')
            city = form.cleaned_data('city')
            country = form.cleaned_data('country')
            postcode = form.cleaned_data('postcode')
            state = form.cleaned_data('state')
            pin = form.cleaned_data('pin1')
            nickname = form.cleaned_data('nickname')
            number =  generate_account_number() 
            
        
            Account.objects.create(
                nickname = nickname,
                user=user,
                pin=make_password(pin),    
                account_no = number,
                phone=phone,
                address=address,
                city=city,
                country=country,
                postcode=postcode,
                state=state,
                balance=0,
                image= picture
                )
            return redirect('dashboard')
    return redirect('dashboard')

