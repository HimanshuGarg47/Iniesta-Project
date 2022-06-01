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
def home(request):
    return render(request, 'staff/dashboard.html' , {"active": True,})


def projects(request):
    projects = Project.objects.filter(team__isnull = False)
    # not assigned projects 
    na_projects = Project.objects.filter(team__isnull = True)
    # print(dir(projects))
    # print(type(projects))
    context = {
        "activate" : True,
        "projects":projects,
        "na_projects":na_projects,
    }
    return render(request , 'staff/project.html' , context)

def team(request):
    projects = Project.objects.filter(team__isnull = False)
    # print(dir(projects))
    # print(type(projects))
    context = {
        "activate" : True,
        "projects":projects,
    }
    return render(request, 'staff/team.html', context)


def employee_detail(request, id):
    employee = Employee.objects.get(id = id)
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





def home_admin(request):
    return render(request, "admin.html")


def home_emp(request):
    return render(request, "employee.html")


def home_intern(request):
    return render(request, "intern.html")


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
# class Employee_DetailView(DetailView):
#     model = Employee
#     template_name_ = 'staff/employee_detail.html'
#     context_object_name = "employee"
#     fields = '__all__'
    
    
#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         context['employee'] = Employee.objects.filter(id=self.kwargs.get('pk'))
#         return context
        
        
    
def team_detail(request , id):
    return render(request, 'staff/team_detail.html' , {})


def index(request):
    employee = Employee.objects.all()
    print(employee)
    return render(request, 'admin.html', {'user': employee})


def intern(request):
    inters = Intern.objects.all()
    print(inters)
    return render(request, 'intern_admin.html', {'user': inters})


def ourproject(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        assign = request.POST.get('assign')
        projectour = Project(name=name, detail=description, assign_date =assign, due_date = datetime.today())
        projectour.save()

    projects = Project.objects.all()
    return render(request, 'projects.html', {'our': projects})


@login_required(login_url='/login/')
def profilePage(request):
    internship = Intern.objects.get(user=request.user)
    return render(request, "intern.html", {"User": internship})


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

    return render(request, "update_profile.html", {"User": user})
# class DetailProfile(View):
#     def is_stored_post(self, request, post_id):
#         stored_posts = request.session.get("stored_posts")
#         if stored_posts is not None:
#           is_saved_for_later = post_id in stored_posts
#         else:
#           is_saved_for_later = False

#         return is_saved_for_later

#     def get(self, request):
#         profile = Employee.objects.all()[0]
        
#         context = {
#             "post": profile.first,
#             "post_tags": post.tags.all(),
#             "comment_form": CommentForm(),
#             "comments": post.comments.all().order_by("-id"),
#             "saved_for_later": self.is_stored_post(request, post.id)
#         }
#         return render(request, "staff/employee_form.html", context)

    # def post(self, request, slug):
    #     comment_form = CommentForm(request.POST)
    #     post = Post.objects.get(slug=slug)

    #     if comment_form.is_valid():
    #         comment = comment_form.save(commit=False)
    #         comment.post = post
    #         comment.save()

    #         return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

    #     context = {
    #         "post": post,
    #         "post_tags": post.tags.all(),
    #         "comment_form": comment_form,
    #         "comments": post.comments.all().order_by("-id"),
    #         "saved_for_later": self.is_stored_post(request, post.id)
    #     }
    #     return render(request, "blog/post-detail.html", context)

