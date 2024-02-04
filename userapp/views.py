

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('floating_text')
        password = request.POST.get('floating_password')

        print(username, password)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('/contact')
        else:
            messages.error(request, "Wrong username or password")
            print("Error while submitting the contact")
            return render(request, "userapp/_login.html")

    return render(request, "userapp/_login.html")


def signupUser(request):
    if request.method == 'POST':
        email = request.POST.get('floating_email')
        username = request.POST.get('floating_username')
        password = request.POST.get('floating_password')
        confirm_password = request.POST.get('floating_confirm_password')
        if username and password and email and confirm_password:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            user.save()
            return redirect('/user/login')
        else:
            messages.error(request, f"Error while submitting the contact")
            print("Error while submitting the contact")
            return render(request, "/user/login")
    return render(request, "userapp/_signup.html")


def logoutUser(request):
    logout(request)
    return redirect('/user/login')
