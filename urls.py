"""celery_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from services import entry
from views.home import index
urlpatterns = [
    url(r'^$', index , name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^celery/', entry.hello),
    url(r'^add2/', entry.add2, name='add2'),
    url(r'^api/',include('api.urls')),
    url(r'^deploy/', include('views.urls')),
]
