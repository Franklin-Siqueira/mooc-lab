from django.contrib import admin
from fcsSimpleMooc.courses import views
from django.urls import path, include, re_path

admin.autodiscover()
# 'fcsSimpleMooc.core.views.home'
app_name = 'courses'

urlpatterns = [path('index', views.index, name = 'index'), 
               path('<shortcut>', views.details, name = "details"),
               path('<shortcut>/enrollment/', views.enrollment, name = "enrollment"),
               path('<shortcut>/undo_enrollment/', views.undo_enrollment, name = "undo_enrollment"),
               path('<shortcut>/announcements/', views.announcements, name = "announcements"),
               path('<shortcut>/announcements/<pk>', views.show_announcement, name = "show_announcement"),
               path('<shortcut>/lessons/', views.lessons, name = "lessons"),
               path('<shortcut>/lessons/<pk>', views.lesson, name = "lesson"),
               path('<shortcut>/material/<pk>', views.material, name = "material"),]

#                re_path(r'^(?P<pk>\d+)/$', views.details, name = 'details'),]

# from https://docs.djangoproject.com/en/2.2/topics/http/urls/#using-regular-expressions
#
# Example:
#
# re_path(r'^comments/(?:page-(?P<page_number>\d+)/)?$', comments),  # good
#
#
# from django.conf.urls import patterns, include, url
# 
# urlpatterns = patterns('simplemooc.core.views',
#     url(r'^$', 'home', name='home'),
#     url(r'^contato/$', 'contact', name='contact'),
# )