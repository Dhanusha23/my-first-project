
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile



@login_required
def home(request):
    return render(request,'home.html')
'''
def loginview(request):
    if request.method == 'POST':
        # Handle POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            return redirect('home')  # Redirect to the home page or any other page
        else:
            # If authentication fails, show an error message or redirect back to the login page
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})

    else:
        # Handle GET request (display the login form)
        return render(request, 'login.html')
        '''



def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # If authentication is successful, log the user in
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page or any other page
        else:
            # If authentication fails, show an error message or redirect back to the login page
            return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

    

def logout_view(request):
        logout(request)
        return redirect('login')

def sign_up(request):
    if request.method == "POST":
        uform = UserCreationForm(request.POST)
        if uform.is_valid():
            uform.save()
            return redirect('home')  # Redirect to the home page or any other page after successful signup
    else:
        uform = UserCreationForm()

    return render(request, 'signup.html', {'form': uform})

def Resethome(request):
    return render(request,'registration/ResetPassword.html')

def resetpassword(request):
    responseDic={}
    try:
        usern = request.POST['uname']
        recepient = request.POST['email']
        pwd = request.POST['password']

        try:
            user=User.objects.get(username=usern)
            if user is not None:
                user.set_password(pwd)
                user.save()
                responseDic["errmsg"]="Password Reset Successfully"
                return render(request,'registration/ResetPassword.html',responseDic)
        except Exception as e:
                print(e)
                responseDic["errmsg"]="Email does not exist"
                return render(request,"registration/ResetPassword.html",responseDic)

    except Exception as e:
        print(e)
        responseDic["errmsg"]="Failed to reset password"
        return render(request,"registration/ResetPassword.html",responseDic)
    

@login_required
def account(request):
    if request.method == 'POST':
        user = request.user
        if user is not None:
            name = request.POST.get('name')
            address = request.POST.get('address')
            contact_number = request.POST.get('contact_number')
            email = request.POST.get('email')

            user.first_name = name
            user.email=email
            user.save()

            # Check if the user has a profile
            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                # If the profile does not exist, create a new one
                profile = Profile.objects.create(user=user)

            profile.address = address
            profile.contact_number = contact_number
            profile.email = email
            profile.save()

            # Add a success message or redirect to another page if needed.
        else:
            # Handle the case where the user is not authenticated
            return render(request, 'signup.html')

    context = {
        'user': request.user,
    }
    return render(request, 'account.html', context)
     
