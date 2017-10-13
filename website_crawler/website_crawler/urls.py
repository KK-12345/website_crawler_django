"""website_crawler URL Configuration

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
from django.contrib.auth import views as dauth_views
from website_crawler.authentication import views as wauth_views
from website_crawler.webcrawler import views as webc_views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login', dauth_views.login, {'template_name': 'cover.html' }, name='login'),
    url(r'^logout', dauth_views.logout, {'next_page': '/'}, name='logout'),
    url('^signup$', wauth_views.signup, name='signup'),
    url('^$', webc_views.home, name='home'),
]
