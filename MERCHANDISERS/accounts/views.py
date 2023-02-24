from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile


# Create your views here.


def login_register_user(request : HttpRequest):

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
            new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])
            new_user.save()
        
            # user_profile = Profile(user=new_user, profile_image = request.FILES["profile_image"])
            # user_profile.save()

            #if register successful redirect to sign in page
            return redirect("accounts:login_register_user")


    return render(request, "accounts/login_register.html")



# def login_user(request : HttpRequest):

    # loggin_msg = None
    
    # if request.method == "POST":
    #     #authenticate user credentials
    #     user = authenticate(request, username= request.POST["username"], password = request.POST["password"] )

    #     if user is not None:
    #         #login user
    #         login(request, user)
    #         return redirect("main:index_page")
    #     else:
    #         loggin_msg = "Please Use correct Credentials"

    # return render(request, "accounts/login.html", {"msg" : loggin_msg})



def logout_user(request : HttpRequest):

    logout(request)

    return redirect("main:index_page")

