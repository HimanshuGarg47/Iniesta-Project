from django.urls import path
from staff import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path('', views.home, name="home"),
  path('profile/<int:id>', views.employee_detail, name='profile'),
  path('team/', views.team, name='team'), 
  path('team/<int:id>/', views.team_detail, name='team-detail'), 
  path('projects/', views.projects, name='projects'),
  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
