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

        import os
        import resend

        resend.api_key = "re_Kn78HRwU_F7uK8HejaweGxsExXpUxqpnE"

        params: resend.Emails.SendParams = {
            "from": "Bichito <robot@resend.equisd.com>",
            "to": [data["email"]],
            "subject": "Patitas te da la bienvenida",
            "html": "<h2>Ya eres parte de Patitas</h2>"
        }
        return redirect("/sign_up/gracias")
    
    return redirect("/")

def sign_up_gracias(request):
    return render(request, "homepage/account/sign_up_gracias.html")

def sign_in(request):
    return render(request, "homepage/account/sign_in.html")

def sign_in_members(request):
    return render(request, "homepage/account/sign_in_members.html")

def sign_in_login(request):
    if request.method == "POST":
        data = request.POST.copy()
        print("++", data)
        return redirect("/sign_in/members")
    return redirect("/")
