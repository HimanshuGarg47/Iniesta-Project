from django.http import HttpResponse
from django.shortcuts import render
from  django.views.generic.edit import CreateView
from .models import Employee
# Create your views here.
def home(request):
    return render(request, 'staff/dashboard.html' , {})


def projects(request):
    return render(request , 'staff/project.html' , {})

def team(request):
    return render(request, 'staff/team.html', {})

class createProfile(CreateView):
    model = Employee
    # template_name_ = 'staff/profile.html'
    fields = '__all__'
    
    
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

