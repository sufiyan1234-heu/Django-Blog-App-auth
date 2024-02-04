import traceback
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User


from home.models import Contact3

from django.contrib import messages
# Create your views here.


def index(request):

    return render(request, "home/index.html")


def about(request):
    return render(request, "home/_about.html")


def contact(request):
    if request.user.is_anonymous:
        return redirect('/user/login')
    try:
        if request.method == "POST":
            company = request.POST.get("floating_company")
            email = request.POST.get("floating_email")
            phone = request.POST.get("floating_phone")
            desc = request.POST.get("message")

            contact = Contact3(company=company, email=email,
                               phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, "Successfully created contact")

        return render(request, "home/_contact.html")
    except Exception as e:
        messages.error(
            request, f"Error while submitting the contact: {str(e)}")
        print("Error while submitting the contact", traceback.format_exc())
        return render(request, "home/_contact.html")


def services(request):
    return render(request, "home/_services.html")
