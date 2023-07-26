"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

#import the index from core/view
# from core.views import index, contact this import is not any more becase it is in core/urls.py

#THis is a way to configurate django to show the image
from django.conf import settings
from django.conf.urls.static import static
##

urlpatterns = [ 
    # with include 'core.urls' the app will go first to core/urls.py before pass to  path('items/', include('item.urls'))
    path('', include('core.urls')),   
    path('items/', include('item.urls')), # include = import the urls file inside item poll
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #to render the image

