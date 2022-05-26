from django.urls import path
from polls import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path('aboutus/', views.about, name='about'),
  path('contactus/', views.contact, name='contact'),
  path('ourservices/', views.service, name='service'),
  path('projects/', views.project, name='project'),
  path('career/', views.career, name='career'),
  path('', views.index, name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
