from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile


# Create your views here.


def login_register_user(request : HttpRequest):
    signup_msg = None

    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            # sign in logic goes here
            user = authenticate(request, username= request.POST["username"], password = request.POST["password"] )
            if user is not None:
            #login user
                login(request, user)
                return redirect("main:index_page")
            else:
                loggin_msg = "Please Use correct Credentials"

            return redirect("accounts:login_register_user")

            
        elif request.POST.get('submit') == 'sign_up':
            # sign up logic goes here
            try :
                new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])
                new_user.save()   
        
                user_profile = Profile(user = new_user)
                if request.FILES.get('profile_image', False):
                    user_profile.profile_image = request.FILES["profile_image"]
                    user_profile.about = request.POST["about"]
                user_profile.save()

                #if register successful redirect to sign in page
                return redirect("accounts:login_register_user")

            except :
                signup_msg = "Username taken, Please use another one"


    return render(request, "accounts/login_register.html", {"signup_msg" : signup_msg})






def logout_user(request : HttpRequest):

    logout(request)

    return redirect("main:index_page")

