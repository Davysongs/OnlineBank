from django.shortcuts import render,redirect
from accounts.models import Account
from login_required import login_not_required

# Create your views here.
@login_not_required
def homepage(request):
    return render(request, "index.html")

def dashboard(request):
    if request.method == "GET":
        user = request.user
        details = Account.objects.get(user = user)
        return render(request, "dashboard.html", {'context':details})
    elif request.method=="POST":
        pass
    

#    return '{:,}'.format(number)
#     return string.replace(',', '')


