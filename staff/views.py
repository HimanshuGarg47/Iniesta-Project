from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from  django.views.generic.edit import CreateView
from django.contrib.auth import *
from django.views.generic import *
from .forms import *
from datetime import datetime
from accounts.models import *

from .models import  Team , Project 
# from django.views.generic.detail import DetailView

# Create your views here.
# def home(request):
#     return render(request, 'staff/dashboard.html' , {"active": True,})


def home(request):
    if request.user.is_authenticated:

        if request.user.is_superuser:
            return redirect("/admin/")
        elif request.user.is_admin:
            return redirect("index/")
        elif request.user.is_employee:
            return redirect("employee/")
        elif request.user.is_intern:
            return redirect("profilepage/")

    else:
        return render(request, "polls/index.html")
    
    
def projects(request):
    projects = Project.objects.filter(project_team__isnull = False)
    # not assigned projects 
    na_projects = Project.objects.filter(project_team__isnull = True)
    # print(dir(projects))
    # print(type(projects))
    context = {
        "activate" : True,
        "projects":projects,
        "na_projects":na_projects,
    }
    return render(request , 'staff/project.html' , context)

def team(request):
    projects = Project.objects.filter(project_team__isnull = False)
    # print(dir(projects))
    # print(type(projects))
    context = {
        "activate" : True,
        "projects":projects,
    }
    return render(request, 'staff/team.html', context)

def team_detail(request , id):
    return render(request, 'staff/team_detail.html' , {})


def employee_detail(request, id):
    employee = Employee.objects.get(user__id = id)
    print(employee.image.url)
    context = {
        "employee":employee
    }
    
    return render(request , 'staff/employee_detail.html', context)

def project_assign(request , pk):  # pk => project id
    ems = Employee.objects.all().filter(team__isnull = True)
    print(ems)
    context = {
        "project_id":pk,
        "ems":ems,            # ems=>employees 
        
    }
    return render(request, 'staff/project-assign.html', context)


def home_emp(request):
    return render(request, "staff/dashboard.html")


# end of employee views




# admin view
def home_admin(request):
    return render(request, "staff/admin.html")

def index(request):
    employee = Employee.objects.all()
    print(employee)
    return render(request, 'staff/admin.html', {'user': employee})




# intern view
def home_intern(request):
    return render(request, "staff/intern.html")

@login_required(login_url='/login/')
def profilePage(request):
    internship = Intern.objects.get(user=request.user)
    return render(request, "staff/intern.html", {"User": internship})

# class Employee_DetailView(DetailView):
#     model = Employee
#     template_name_ = 'staff/employee_detail.html'
#     context_object_name = "employee"
#     fields = '__all__'
    
    
#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         context['employee'] = Employee.objects.filter(id=self.kwargs.get('pk'))
#         return context
        
        
    






def intern(request):
    inters = Intern.objects.all()
    print(inters)
    return render(request, 'staff/intern_admin.html', {'user': inters})


def ourproject(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        assign = request.POST.get('assign')
        projectour = Project(name=name, detail=description, assign_date =assign, due_date = datetime.today())
        projectour.save()

    projects = Project.objects.all()
    return render(request, 'staff/projects.html', {'our': projects})




@login_required(login_url='/login/')
def updateprofile(request):
    user = CustomUser.objects.get(username=request.user)
    print(user)
    if (user.is_superuser):
        return redirect("/admin/")
    else:
        user_intern = Intern.objects.get(user=request.user)
        print(user_intern)

        if request.method == "POST":
            user_intern.user.username = request.POST.get('username')
            user_intern.user.email = request.POST.get('email')
            user_intern.user.mobile_no = request.POST.get('phone')
            user_intern.addressline = request.POST.get('addressline')
            user_intern.pin = request.POST.get('pin')
            user_intern.city = request.POST.get('city')
            user_intern.state = request.POST.get('state')
            if (request.FILES.get('pic')):
                user_intern.pic = request.FILES.get('pic')
            user_intern.save()
            return redirect("profilepage/")

    return render(request, "staff/update_profile.html", {"User": user})
