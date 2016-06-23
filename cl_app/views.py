from django.shortcuts import render
from cl_app.models import Listing, Profile
from django.views.generic.base import TemplateView
from django.views.generic import ListView

# Create your views here.

class IndexView(ListView):
    template_name = "index.html"
    model = Listing
