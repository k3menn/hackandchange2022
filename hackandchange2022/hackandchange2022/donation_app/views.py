from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import UserRegistrationForm
from .forms import *
from .models import *


class General:
    def base(request):
        ctx = {
        "data" : "DATA FROM THE SERVER"
        }
        return render(request,"donation_app/base.html" , ctx)

class Authorization:
    def aut(request):
        return render(request,"donation_app/register_buttons.html")

class Registration:
    def Register(request):
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
               
                new_user = user_form.save(commit=False)
                
                new_user.set_password(user_form.cleaned_data['password'])
                
                new_user.save()
                return render(request, "donation_app/register_done.html", {'new_user': new_user})
        else:
            user_form = UserRegistrationForm()
        return render(request, "donation_app/register.html", {'user_form': user_form})

