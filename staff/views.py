from django.http import HttpResponse
from django.shortcuts import render
from  django.views.generic.edit import CreateView
from .models import Employee
# Create your views here.
def home(request):
    return render(request, 'staff/dashboard.html' , {})


class createProfile(CreateView):
    model = Employee
    # template_name_ = 'staff/profile.html'
    # fields = '__all__'

