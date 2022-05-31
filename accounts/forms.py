from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import CustomUser, Employee, Intern


class AdminSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "mobile_no"
        )

    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()

    def __init__(self, *args, **kwargs):
        super(AdminSignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None


class EmployeeSignUpForm(UserCreationForm):
    # department = forms.ModelMultipleChoiceField(
    #     queryset=Department.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "mobile_no",
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        emp = Employee.objects.create(user=user)
        # emp.department.add(*self.cleaned_data.get('department'))
        return user


class InternSignUpForm(UserCreationForm):
    # departments = forms.ModelMultipleChoiceField(
    #     queryset=Department.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "mobile_no",
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_intern = True
        user.save()
        intern = Intern.objects.create(user=user)
        # intern.departments.add(*self.cleaned_data.get('departments'))
        return user
