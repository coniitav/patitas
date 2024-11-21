from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sign_up(request):
    return render(request, "homepage/account/sign_up.html")

from django.shortcuts import redirect
def sign_up_create(request):
    if request.method == "POST":
        data = request.POST.copy()
        print("++", data)

        return redirect("/sign_up/gracias")
    
    return redirect("/")

def sign_up_gracias(request):
    return render(request, "homepage/account/sign_up_gracias.html")