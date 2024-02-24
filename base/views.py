from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, "index.html")
# @login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html")
