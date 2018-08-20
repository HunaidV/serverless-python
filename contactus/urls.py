from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.views.generic import TemplateView
from .views import contactmail
# from base.views import AssignmentListView
urlpatterns = [
    url(r'^$', contactmail, name="form"),
    url(r'^thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),    
    
    ]
    

