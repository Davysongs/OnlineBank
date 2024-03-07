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
        uid = request.user.email
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
        pin = request.POST.get('pin')

        # Retrieve existing user profile instance
        user_profile = Account.objects.get(email=uid)

        # Update fields with new data
        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.email = email
        user_profile.phone = phone
        user_profile.address = address
        user_profile.city = city
        user_profile.country = country
        user_profile.postcode = postcode
        user_profile.state = state
        user_profile.pin = pin

        # Save the updated user profile instance
        user_profile.save()
