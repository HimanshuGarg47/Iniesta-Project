from django.contrib import admin
from .models import Address, Employee
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserAdmin(BaseUserAdmin):
    pass


admin.site.register(Address)
admin.site.register(Employee, UserAdmin)
