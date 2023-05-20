from django.shortcuts import render
from django.views.generic import TemplateView,ListView
# Create your views here.
from app.models import *
class home(TemplateView):
    template_name='app/home.html'


class School_List(ListView):
    model=School
    context_object_name='schools'
    template_name='app/School_List.html'