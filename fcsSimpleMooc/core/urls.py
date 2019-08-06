from django.contrib import admin
from fcsSimpleMooc.core import views
from django.urls import path, include

admin.autodiscover()
# 'fcsSimpleMooc.core.views.home'
app_name = 'core'

urlpatterns = [path('', views.home, name='home'), path('contact/', views.contact, name='contact')]


# from django.conf.urls import patterns, include, url
# 
# urlpatterns = patterns('simplemooc.core.views',
#     url(r'^$', 'home', name='home'),
#     url(r'^contato/$', 'contact', name='contact'),
# )