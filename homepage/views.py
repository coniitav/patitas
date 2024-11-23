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
                "last_name": "Ramirez",
                "foto": "https://whoofpoint.com/media/images/card_id/profile_40442120.png"
            },
            {
                "first_name": "María",
                "last_name": "Suarez",
                "foto": "https://whoofpoint.com/media/images/card_id/profile__z9pMJfk.png"
            },
            {
                "first_name": "Vanessa",
                "last_name": "Rojas",
                "foto": "https://whoofpoint.com/media/images/card_id/profile__Bxs38Zm.png"
            },
            {
                "first_name": "Michael",
                "last_name": "Torres",
                "foto": "https://whoofpoint.com/media/images/card_id/profile__Hbemmoz.png"
            },
            {
                "first_name": "Ramiro",
                "last_name": "González",
                "foto": "https://whoofpoint.com/media/images/card_id/profile_75449101.png"
            },
            {
                "first_name": "Eduardo",
                "last_name": "Rojas",
                "foto": "https://whoofpoint.com/media/images/card_id/profile_74944414_nzUOEwk.png"
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