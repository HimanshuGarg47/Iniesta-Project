from django.contrib import admin
from .models import Project , Team  , Task ,Submission

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

# class UserAdmin(BaseUserAdmin):
#     pass


admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Submission)
admin.site.register(Task)
