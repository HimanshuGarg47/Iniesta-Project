# from statistics import mode
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
# from localflavor.gr.forms import 
# Create your models here.
# from multiselectfield import MultiSelectField


from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# Create your models here.
class Address(models.Model):
    address_line1 = models.CharField(_("address"), max_length=128)
    address_line2 = models.CharField(_("address2"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Zanesville")
    state = models.CharField(max_length=100, null=True)
    country = models.CharField("Country", max_length=50, null=True) 
    zip_code = models.CharField(_("zip code"), max_length=5, default="43701")
    
    
class Employee(AbstractUser):
    department_choices = (
        (0, "Trainee"),
        (1,"Full Stack Developer"),
        (2 , "Frontend Developer"),
        (3, "Backend Developer"),
        (4, "Graphic Designer"),
        (5, "Digital Marketer"),
        (6, "Data Scientist")
    )
    username = models.CharField(max_length=20, unique=True)
    employee_id = models.AutoField(primary_key=True , default=0)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="profile", null=True)
    # name = models.CharField(max_length=255)
    # is_staff = models.BooleanField(default=True)
    # is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    date_joined = models.DateTimeField(default=timezone.now)
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)  # you can set it unique = True
    address = models.OneToOneField(Address , on_delete=models.SET_NULL , null=True)
    department = models.IntegerField(choices=department_choices, default=0)
    credit_score = models.IntegerField(validators=[MinValueValidator(0),
                                  MaxValueValidator(100)] , default=0)
    


    

