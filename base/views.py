from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from transactions.models import Trans

# Create your views here.
def homepage(request):
    return render(request, "index.html")

# @login_required(login_url="login")
def dashboard(request):
    if request.method == "GET":
        try:
            user_no = request.user.account_no
            details = Account.objects.get(account_no = user_no)
            return render(request, "dashboard.html", {'context':details})
        except:
            #User have not finished account creation then redirect to account registration
            return render(request,"profile.html" )

    return render(request, "dashboard.html")

