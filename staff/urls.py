from django.urls import path
from staff import views
from staff.views import *
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('profile/<int:id>', views.employee_detail, name='profile'),
    path('team/', views.team, name='team'),
    path('team/<int:id>/', views.team_detail, name='team-detail'),
    path('projects/', views.projects, name='projects'),
    path('project-assign/<int:pk>', views.project_assign, name='project-assign'),
    path("", home, name="home"),
    path("home-admin/", home_admin, name="home_admin"),
    path("home-emp/", home_emp, name="home_emp"),
    path("home-intern/", home_intern, name="home_intern"),
    
    # login
    path("login/", auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login",),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('index/', index, name="index"),
    path('intern-admin/', intern, name="intern_admin"),
    path('ourproject/', ourproject, name="ourproject"),
    path('profilepage/', profilePage, name="profilepage"),
    path('updateprofile', updateprofile, name="updateprofile"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
