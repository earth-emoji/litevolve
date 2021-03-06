import json
import random
from django.shortcuts import render, redirect

# Create your views here.
def home(request, template_name='pages/home.html', data={}):
    if request.user.is_authenticated:
        return redirect('profile:index', request.user.profile.slug)
    return render(request, template_name, data)
