# views: register, dashboard, edit, edit_password, password_reset_confirm, password_reset
from fcsSimpleMooc.accounts.views import * 
from django.urls import path, include
from django.contrib.auth.views import LoginView
# from django.contrib.auth import logout

from fcsSimpleMooc.core import views

app_name = 'accounts'

urlpatterns = [path('connect/', LoginView.as_view(template_name='accounts/login.html'), name = 'login'), 
               path('register/', register, name='register'),
               path('edit/', edit, name='edit'),
               path('password_reset/', password_reset, name='password_reset'),
               path('edit_password/', edit_password, name='edit_password'),
               path('password_reset_confirm/<key>', password_reset_confirm, name='password_reset_confirm'),
               path('dashboard/', dashboard, name='dashboard'),
               path('logout', logout_request, name='logout'),]

##########                  END                ###########
# {'template_name':'accounts/login.html'},
# re_path(r'^(?P<pk>\d+)/$', views.details, name = 'details'),]

# from https://docs.djangoproject.com/en/2.2/topics/http/urls/#using-regular-expressions
#
# Example (didn't work):
#
# re_path(r'^comments/(?:page-(?P<page_number>\d+)/)?$', comments),  # good
#django.contrib.auth.views.logout
#
# from django.conf.urls import patterns, include, url
# 
# urlpatterns = patterns('simplemooc.core.views',
#     url(r'^$', 'home', name='home'),
#     url(r'^contato/$', 'contact', name='contact'),
# )
 

#     url(r'^sair/$', 'django.contrib.auth.views.logout', 
#         {'next_page': 'core:home'}, name='logout'),

#     url(r'^nova-senha/$', 'simplemooc.accounts.views.password_reset', 
#         name='password_reset'),
#     url(r'^confirmar-nova-senha/(?P<key>\w+)/$', 
#         'simplemooc.accounts.views.password_reset_confirm', 
#         name='password_reset_confirm'),
#     url(r'^editar/$', 'simplemooc.accounts.views.edit', 
#         name='edit'),
#     url(r'^editar-senha/$', 'simplemooc.accounts.views.edit_password', 
#         name='edit_password'),
##########                  END                ###########