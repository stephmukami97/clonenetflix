from django.urls import path
from . import views


urlpatterns = [
    path('home',views.home,name="home"),
    path('display/<str:pk>',views.display,name="display"),
    path('',views.index,name="index"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]
