from django.shortcuts import render
from accounts.models import Account
from transactions.models import Trans
from login_required import login_not_required

# Create your views here.
@login_not_required
def homepage(request):
    return render(request, "index.html")

@login_not_required
def dashboard(request):
    if request.method == "GET":
        try:
            user_no = request.user.account_no
            details = Account.objects.get(account_no = user_no)
            return render(request, "dashboard.html", {'context':details})
        except:
            #User have not finished account creation then redirect to account registration
            return render(request,"dashboard.html" )
    return render(request, "dashboard.html")

