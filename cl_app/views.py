from django.shortcuts import render
from cl_app.models import Listing, Profile
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# Create your views here.

class IndexView(ListView):
    template_name = "index.html"
    model = Listing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            pass
        else:
            context["login_form"] = AuthenticationForm()
        return context

class RegisterView(CreateView):
    # template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/'
    model = User
    # fields = ["username", "email", "password", "password"]
