from django.shortcuts import render, redirect
from math import ceil
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from datetime import datetime


def home(request):
    return render(request, 'welcome.html')



