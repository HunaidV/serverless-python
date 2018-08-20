from django.shortcuts import render
from django.views.generic import ListView ,DetailView
# Create your views here.
from .models import SampleModel
class SampleListView(ListView):
	queryset = SampleModel.objects.all()


class SampleDetailView(DetailView):
	queryset = SampleModel.objects.all()