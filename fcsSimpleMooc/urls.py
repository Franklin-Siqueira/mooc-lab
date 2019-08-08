"""fcsSimpleMooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/

Examples:

    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
"""
from django.contrib import admin
from fcsSimpleMooc.core import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

# 'fcsSimpleMooc.core.views.home'
# path('root_for_app', include('app_path', namespace = 'defined_name_space'))
urlpatterns = [path('admin/', admin.site.urls), 
               path('', include('fcsSimpleMooc.core.urls', namespace='core')), 
               path('courses/', include('fcsSimpleMooc.courses.urls', namespace='courses')),
               path('forum/', include('fcsSimpleMooc.forum.urls', namespace='forum')),
               path('accounts/', include('fcsSimpleMooc.accounts.urls', namespace='accounts'))]

# if in development environment, add paramenters
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#     path('', views.home, name='home'),
#     path('contact/', views.contact, name='contact')
# ]