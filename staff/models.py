# from statistics import mode
# from pyexpat import model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
# from localflavor.gr.forms import
# Create your models here.
# from multiselectfield import MultiSelectField


class Submission(models.Model):
    sub_name = models.CharField(max_length=200)
    sub_file = models.FileField(upload_to='statistics')
    sub_date = models.DateTimeField(
        'date submitted', blank=True, null=True, default=timezone.now)
    project = models.ForeignKey(
        'Project', blank=True, on_delete=models.CASCADE)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.sub_name


class Task(models.Model):
    name = models.CharField(max_length=50, null=True)
    detail = models.TextField(max_length=400)
    assign_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    employee_assigned = models.ForeignKey(
        'accounts.Employee', related_name='task_assigned' , null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Team(models.Model):
    project = models.ForeignKey(
        'Project', related_name='project_team' , blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " assigned " + str(self.project.name)


class Project(models.Model):
    name = models.CharField(max_length=50, null=True)
    detail = models.TextField(max_length=400)
    assign_date = models.DateField(null=True)
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.name
