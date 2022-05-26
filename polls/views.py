from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# import sqlite3 as db
# import mysql.connector as sql

#con = db.connect('data.db',check_same_thread=False)
#con=sql.connect(host='y20db.c7qkhc6tkh0v.ap-south-1.rds.amazonaws.com',user='admin',password='postgres',database='mydb');
#cur=con.cursor()

def index(request):
    context = {}
    return render(request, 'polls/index.html', context)


def about(request):
    context = {}
    return render(request, 'polls/about.html', context)


def contact(request):
    context = {}
    return render(request, 'polls/contactUs.html', context)


def service(request):
    context = {}
    return render(request, 'polls/ourservices.html', context)


def project(request):
    context = {}
    return render(request, 'polls/project.html', context)


def career(request):
    context = {}
    return render(request, 'polls/career.html', context)
