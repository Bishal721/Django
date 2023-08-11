from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def UserData(request):
    if request.method == "POST":
        Username = request.POST.get("username")
        Email = request.POST.get("email")
        FirstName = request.POST.get("firstname")
        LastName = request.POST.get("lastname")
        Password = request.POST.get("password")
        ConfirmPassword = request.POST.get("confirmpassword")
        if Password == ConfirmPassword:
            user = User.objects.create_user(
                username=Username,
                email=Email,
                first_name=FirstName,
                last_name=LastName,
                password=Password
            )
            user.save()
            return redirect("crud:home")
        else:
            print("Passowrd validation failed")
    return render(request,"users/Register.html")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("crud:home")
        else:
            return redirect("users:Login")
    return render(request,"users/Login.html")

@login_required
def logoutUser(request):
    logout(request)
    return redirect("crud:home")