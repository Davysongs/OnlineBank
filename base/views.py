from django.shortcuts import render,redirect
from accounts.models import Account
from transactions.models import Trans
from login_required import login_not_required


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
    
def profile(request):
    if request.method == "GET":
        return render(request, "profile.html")
    if request.method == 'POST':
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
        pin = request.POST.get('pin')

        # Create and save UserProfile instance
        user_profile = Account(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            country=country,
            postcode=postcode,
            state=state,
            pin=pin
        )
        user_profile.save()


