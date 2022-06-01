from pyexpat import model
from django.db import models
# from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from .managers import CustomAccountManager
from staff.models import *



class Address(models.Model):
    address_line1 = models.CharField(_("address"), max_length=128)
    address_line2 = models.CharField(_("address2"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Zanesville")
    state = models.CharField(max_length=100, null=True)
    country = models.CharField("Country", max_length=50, null=True)
    zip_code = models.CharField(_("zip code"), max_length=7, default="43701")

    def __str__(self):
        return self.address_line1
    # employee = models.OneToOneField(Employee , on_delete=models.CASCADE)
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    is_admin = models.BooleanField("admin", default=False)
    is_employee = models.BooleanField("employee", default=False)
    is_intern = models.BooleanField("intern", default=False)
    mobile_no = models.PositiveIntegerField(
        validators=[
            RegexValidator(
                regex="^[1-9][0-9]{9}$",
                message="Mobile Number must be of ten digit digits",
                code="invalid Mobile Number",
            )
        ]
    )

    objects = CustomAccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "email",
        "mobile_no",
    ]

    def __str__(self):
        return self.username


class Employee(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name='employees', on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to="profile", null=True)

    date_joined = models.DateTimeField(default=timezone.now)
    # (choices=department_choices, default=0)
    department = models.ForeignKey(
        Department, related_name='departments', blank=True, default=None, null=True, on_delete=models.SET_NULL)
    credit_score = models.IntegerField(validators=[MinValueValidator(0),
                                                   MaxValueValidator(100)], default=0)
    address = models.ForeignKey(Address, related_name='addresses' , on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(
        'staff.Team', related_name = 'teams', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username


class Intern(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name = 'interns' , on_delete=models.CASCADE, primary_key=True)

    image = models.ImageField(upload_to="profile", null=True)

    date_joined = models.DateTimeField(default=timezone.now)
    # (choices=department_choices, default=0)
    department = models.ForeignKey(
        Department, blank=True, default=None, null=True, on_delete=models.SET_NULL)
    credit_score = models.IntegerField(validators=[MinValueValidator(0),
                                                   MaxValueValidator(100)], default=0)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(
        'staff.Team', blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.user.username
