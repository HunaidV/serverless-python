from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView, ListView, DetailView
from .forms import OrderForm
from .models import OrderModel




class OrderCreateView(CreateView):
	form_class = OrderForm
	template_name = "ordernew.html"
	success_url = reverse_lazy('neworder:thankyou')





# 
	



