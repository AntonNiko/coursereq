from django import forms
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from decimal import Decimal
import random, re

# Create your views here.
def index(request):
    context = {}
    return render(request, "course_manager/index.html", context)
