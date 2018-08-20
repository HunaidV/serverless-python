from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import ServiceModel

class ServiceListView(ListView):
	queryset = ServiceModel.objects.all()


class ServiceDetailView(DetailView):
	queryset = ServiceModel.objects.all()


