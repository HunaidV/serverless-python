from django.conf.urls import url


from .views import ServiceListView, ServiceDetailView
# from base.views import AssignmentListView
urlpatterns = [
    url(r'^$', ServiceListView.as_view(), name="list"),
    url(r'(?P<slug>[\w-]+)/$', ServiceDetailView.as_view(), name="detail"),   
    
    
    ]
    

