from django.urls import path
from staff import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path('', views.home, name='home'),
  path('profile/' , views.createProfile.as_view() , name = 'profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
