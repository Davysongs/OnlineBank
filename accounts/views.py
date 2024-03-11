from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from login_required import login_not_required
from accounts.forms import SignUpForm
from .forms import UserForm
from base.middlewares import CustomException
from accounts.models import Account
from django.http import JsonResponse
from django.views.decorators.http import require_POST


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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            condition = True
            return render(request, "register.html", {'condition': condition})

    
    if request.method == "GET":
        form = SignUpForm()
        return render(request, "register.html", {"form" : form})


#Logout
def logout_user(request):
    logout(request)
    return redirect('home')



def profile(request):
    user = request.user
    try:
        details = Account.objects.get(user=user)
    except Account.DoesNotExist:
        # Handle the scenario where the user's account does not exist
        # For example, redirect the user to a page to create their account
        return redirect('create_account')

    if request.method == "GET":
        form = UserForm(instance=details)  # Populate form with existing data
        if details.pin:
            return render(request, 'update.html', {'details': details, 'form': form})
        else:
            return render(request, 'update.html', {'form': form})

    elif request.method == 'POST':
        if request.is_ajax():
            nickname = request.POST.get('nickname')
            image = request.FILES.get('image')
            user = request.user
            
            try:
                # Get or create the Account object for the user
                account = Account.objects.get_or_create(user=user)
                
                # Update the Account object with the received data
                account.nickname = nickname
                account.image = image
                account.save()
                
                # Return a success response
                return JsonResponse({'message': 'Data saved successfully'}, status=200)
            except Exception as e:
                # Return an error response if an exception occurs
                return JsonResponse({'error': str(e)}, status=500)
            
        else:
            form = UserForm(request.POST, request.FILES, instance=details)
            if form.is_valid():
                form.save()
                # Add a success message to provide feedback to the user
                messages.success(request, 'Profile updated successfully.')
                return redirect('dashboard')
            else:
                # Form is not valid, handle the error scenario by rendering the form with errors
                return render(request, 'update.html', {'details': details, 'form': form})




