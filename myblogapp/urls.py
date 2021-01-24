"""myblogapp URL Configuration

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
from django.conf.urls import include, url
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from posts import views
from django.views.generic import RedirectView

urlpatterns = [
    # サーバーアドレスにbbsと続いている場合bbsのurls.pyを参照する
    url(r'^posts/', include('posts.urls')),
    path('bbs/',include('bbs.urls')),
    path('admin/', admin.site.urls),
    path('',RedirectView.as_view(url='/bbs/')),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)