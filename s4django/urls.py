"""s4django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# The admin now has a sidebar on larger screens for easier navigation. It is enabled by default but can be disabled by using a custom AdminSite and setting AdminSite.enable_nav_sidebar to False.
admin.autodiscover()
admin.site.enable_nav_sidebar = False
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('polls.urls')),
    path('employee/', include(('staff.urls', 'staff') , namespace='staff')),
    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
