from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *
# from base.views import AssignmentListView
urlpatterns = [
    url(r'^$', BlogListView.as_view(), name="list"),
    url(r'(?P<slug>[\w-]+)/$', BlogDetailView.as_view(), name="detail"),    
   	
    ]
    

