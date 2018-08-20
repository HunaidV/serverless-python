"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView 
from django.contrib.auth import views as auth_views
from django.conf import settings
from base.views import *
from accounts.views import *

# from base.views import AssignmentListView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
   	url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    #url(r'^blog/', include('blogging.urls', namespace="blog")), 
    url(r'^accounts/', include('accounts.urls', namespace="accounts")), 
    url(r'^samples/', include('samples.urls', namespace="samples")),
    url(r'^contactus/', include('contactus.urls', namespace="contact")),
    url(r'^services/', include('services.urls', namespace="services")),
    url(r'^neworder/', include('ordernow.urls', namespace="neworder")),
    url(r'^careers/', include('careers.urls', namespace="careers")),
    # url(r'^signup/$', signup, name='signup'),
    # url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #         activate, name='activate'),
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout,{'next_page': '/'}, name='logout'),
    
    #url(r'^order/send/$', frontmail ),
    url(r'^order/thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
    url(r'^order/$', frontmail, name='order'),
    
    url(r'^thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
    url(r'^aboutus/$', TemplateView.as_view(template_name='about.html'), name='aboutus'),
    
    #url(r'^test/$', TemplateView.as_view(template_name='test.html'), name='test'),
    
    url(r'^companypolicy/$', TemplateView.as_view(template_name='privacy.html'), name='companypolicy'),
    
    #url(r'^services/$', TemplateView.as_view(template_name='services.html'), name='services'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
 