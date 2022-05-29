from django.http import HttpResponse
from django.shortcuts import render
from  django.views.generic.edit import CreateView
from .models import Employee , Team , Project 
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
    context = {
        "employee":employee
    }
    
    return render(request , 'staff/employee_detail.html', context)
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

