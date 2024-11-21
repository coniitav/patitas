from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "providers": [
            {
                "first_name": "Pepito",
                "last_name": "Perez",
                "foto": "https://whoofpoint.com/media/images/card_id/profile_73870520.png"
            },
            {
                "first_name": "Juan",
                "last_name": "Ramirez"
            },
            {
                "first_name": "María",
                "last_name": "Suarez"
            },
            {
                "first_name": "Vanessa",
                "last_name": "Rojas"
            },
            {
                "first_name": "Michael",
                "last_name": "Torres"
            },
            {
                "first_name": "Ramiro",
                "last_name": "González"
            },
            {
                "first_name": "Eduardo",
                "last_name": "Rojas"
            },
        ]
    }
    return render(request, "homepage/index.html", context)

from django.shortcuts import redirect
def feedback_create(request):
    if request.method == "POST":
        data = request.POST.copy()
        print("++", data)

        return redirect("/feedback/gracias")
    
    return redirect("/")

def feedback_gracias(request):
    return render(request, "homepage/feedback_gracias.html")