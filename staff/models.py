# from statistics import mode
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from .managers import CustomUserManager
# from localflavor.gr.forms import 
# Create your models here.
# from multiselectfield import MultiSelectField

# class Department(models.Model):
#     name = models.CharField(max_length=30)
#     employees = models.ManyToManyField('Employee' , blank=True, null=True)
    
    
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
    email = models.EmailField(unique=True)
    username = None
    employee_id = models.IntegerField(unique=True, default=0)
    image = models.ImageField(upload_to="profile", null=True)
    # name = models.CharField(max_length=255)
    # is_staff = models.BooleanField(default=True)
    # is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    date_joined = models.DateTimeField(default=timezone.now)
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)  # you can set it unique = True
    department = models.IntegerField(choices=department_choices, default=0)
    credit_score = models.IntegerField(validators=[MinValueValidator(0),
                                  MaxValueValidator(100)] , default=0)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    objects = CustomUserManager()
    # address = None
    # def __init__(self , *args, **kwargs):
    #     self.address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)
    #     super().__init__(*args, **kwargs)
        
        
    def __str__(self):
        return str(self.email) 
        
    
class Task(models.Model):
    name  = models.CharField(max_length=50, null = True)
    detail = models.TextField(max_length=400)
    assign_date =models.DateField(null = True)
    due_date = models.DateField(null = True)
    employee_assigned = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
    
class Team(models.Model):
    
    employees = models.ManyToManyField(Employee)
    
    def __init__(self, *args, **kwargs):
        self.project = models.ManyToManyField(Project)
        super().__init__(*args, **kwargs)
        
    def __str__(self):
        return str(self.id)
    
    
        
        

class Project(models.Model):
    name  = models.CharField(max_length=50, null = True)
    detail = models.TextField(max_length=400)
    assign_date =models.DateField(null = True)
    due_date = models.DateField(null = True)
    team = models.ForeignKey(Team , blank= True , null = True , on_delete=models.SET_NULL)
    
    
    def __str__(self):
        return self.name
