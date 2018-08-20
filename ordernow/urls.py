
from django.conf.urls import url
from .views import OrderCreateView
from django.views.generic import TemplateView
# from base.views import AssignmentListView
urlpatterns = [
    
   	url(r'^$', OrderCreateView.as_view(), name='create'),
  	url(r'^thankyou/$', TemplateView.as_view(template_name="thankyou2.html"), name='thankyou'),
    ]
    
 