
from django.conf.urls import url
from .views import Career
from django.views.generic import TemplateView
# from base.views import AssignmentListView
urlpatterns = [
    
    url(r'^$', Career.as_view(), name='create'),
  	url(r'^thankyou/$', TemplateView.as_view(template_name="thanks.html"), name='thankyou'),
    ]
    
 