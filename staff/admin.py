from django.contrib import admin
from .models import Address, Employee , Project , Team  , Task , Department , Submission
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

# class UserAdmin(BaseUserAdmin):
#     pass


admin.site.register(Address)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Department)
admin.site.register(Submission)
admin.site.register(Task)
