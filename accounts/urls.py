from django.urls import path
from django.contrib.auth import views as auth_views

# from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # path("login/", auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("signup/", signUp, name="signup"),
    path("signup/admin/", AdminSignUpView.as_view(), name="adminsignup"),
    path("signup/employee/", EmployeeSignUpView.as_view(), name="empsignup"),
    path("signup/intern/", InternSignUpView.as_view(), name="internsignup"),
    # path("login/", auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login",),

    
]