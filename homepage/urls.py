from django.urls import path
from . import views, views_account
urlpatterns = [
    path("", views.index, name="index"),
    path("feedback/create", views.feedback_create, name="feedback_create"),
    path("feedback/gracias", views.feedback_gracias, name="feedback_gracias"),
    path("sign_up", views_account.sign_up, name="sign_up"),
    path("sign_up/create", views_account.sign_up_create, name="sign_up_create"),
    path("sign_up/gracias", views_account.sign_up_gracias, name="sign_up_gracias"),
    path("sign_in", views_account.sign_in, name="sign_in"),
    path("sign_in/members", views_account.sign_in_members, name="sign_in_members"),
    path("sign_in/login", views_account.sign_in_login, name="sign_in_login"),
]