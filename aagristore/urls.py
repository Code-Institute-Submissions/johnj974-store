"""aagristore URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
# static files
from django.views import static
# imported functions from account app
from accounts.views import index, logout, login, registration, user_profile
# imported urls from products app
from products import urls as urls_products
# import the view function
from products.views import all_machinery, Machinery
# import the media root from settings
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/register/$', registration, name='registration'),
    url(r'^accounts/profile/$', user_profile, name='profile'),
    url(r'^products/', include(urls_products)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    #url(r'^$', all_machinery, name='Macinery'),
]
