'''

URLs for the forum's related instances

. 'index', views.index, name = 'index'
. '<tag>/tag/', views.index, name = "index_tagged"
. '/replies/<pk>/correct/', views.reply_correct, name = "reply_correct"
. '/replies/<pk>/incorrect/', views.reply_incorrect, name = "reply_incorrect"
. '<shortcut>/', views.thread, name = "thread"

'''
from django.contrib import admin
from fcsSimpleMooc.forum import views
from django.urls import path, include, re_path
#
#  Code from course's material
#
# urlpatterns = patterns('simplemooc.forum.views',
#     url(r'^$', 'index', name='index'),
#     url(r'^tag/(?P<tag>[\w_-]+)/$', 'index', name='index_tagged'),
#     url(r'^respostas/(?P<pk>\d+)/correta/$', 'reply_correct', name='reply_correct'),
#     url(r'^respostas/(?P<pk>\d+)/incorreta/$', 'reply_incorrect', name='reply_incorrect'),
#     url(r'^(?P<slug>[\w_-]+)/$', 'thread', name='thread'),
# )

admin.autodiscover()

app_name = 'forum'

urlpatterns = [path('index', views.index, name = 'index'), 
               path('tag/<tag>/', views.index, name = "index_tagged"),
               path('replies/<pk>/correct/', views.reply_correct, name = "reply_correct"),
               path('replies/<pk>/incorrect/', views.reply_incorrect, name = "reply_incorrect"),
               path('<shortcut>/', views.thread, name = "thread"),]

# urlpatterns = [path('index', views.index, name = 'index'), 
#                path('<shortcut>', views.details, name = "details"),
#                path('<shortcut>/enrollment/', views.enrollment, name = "enrollment"),
#                path('<shortcut>/undo_enrollment/', views.undo_enrollment, name = "undo_enrollment"),
#                path('<shortcut>/announcements/', views.announcements, name = "announcements"),
#                path('<shortcut>/announcements/<pk>', views.show_announcement, name = "show_announcement"),
#                path('<shortcut>/lessons/', views.lessons, name = "lessons"),
#                path('<shortcut>/lessons/<pk>', views.lesson, name = "lesson"),
#                path('<shortcut>/material/<pk>', views.material, name = "material"),]