from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register_user(request : HttpRequest):

    # if request.method == "POST":
    #     new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
    #     new_user.save()

    #     #if register successful redirect to sign in page
    #     return redirect("accounts:login_user")


    return render(request, "accounts/register.html")



def login_user(request : HttpRequest):

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

    return render(request, "accounts/login.html", {"msg" : loggin_msg})



def logout_user(request : HttpRequest):

    # logout(request)

    return redirect("main:index_page")

