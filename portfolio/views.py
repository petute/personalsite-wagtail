from django.shortcuts import render
from django.views.generic import DetailView

from .models import _S_Projects_Project_ImageBlock

# Create your views here.

class Project_ImageDetailView(DetailView):
    model = _S_Projects_Project_ImageBlock
    template_name = 'portfolio/blocks/_S_Projects_Project_Image.html'