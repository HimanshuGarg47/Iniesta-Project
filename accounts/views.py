from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.views.generic import *
from .forms import *
from datetime import datetime
from .models import *
# Create your views here.

def signUp(request):
    return render(request, "front_signUp.html")


class AdminSignUpView(CreateView):
    model = CustomUser
    form_class = AdminSignUpForm
    template_name = "registration/signup_form.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/account/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        new_user = authenticate(self.request, username=username, password=password)
        login(self.request, new_user)
        return redirect("/account/")
    
class EmployeeSignUpView(CreateView):
    model = CustomUser
    form_class = EmployeeSignUpForm
    template_name = 'registration/signup_form.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/")
    
class InternSignUpView(CreateView):
    model = CustomUser
    form_class = InternSignUpForm
    template_name = 'registration/signup_form.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/account/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/account/")
