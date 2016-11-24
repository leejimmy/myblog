"""myblog URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views
from django.conf.urls.static import static
from myblog import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',blog_views.get_blogs,name="get_blogs"),
    url(r'^blog/(?P<pk>\d+)/$',blog_views.get_detail,name='blog_get_detail'),
    url(r'^photos/$',blog_views.get_photos,name='get_photos'),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )