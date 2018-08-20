from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import BLOGMODEL

class BlogListView(ListView):
	queryset = BLOGMODEL.objects.all()
	


class BlogDetailView(DetailView):
	queryset = BLOGMODEL.objects.all()