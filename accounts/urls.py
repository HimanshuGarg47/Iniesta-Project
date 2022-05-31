from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("signup/", signUp, name="signup"),
    path("signup/admin/", AdminSignUpView.as_view(), name="adminsignup"),
    path("signup/employee/", EmployeeSignUpView.as_view(), name="empsignup"),
    path("signup/intern/", InternSignUpView.as_view(), name="internsignup"),
    
]