from django.shortcuts import render

from django.views.generic import CreateView
from .forms import CareerForm
from django.urls import reverse_lazy


class Career(CreateView):
	form_class = CareerForm
	template_name = "career.html"
	success_url = reverse_lazy('careers:thankyou')



