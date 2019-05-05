"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.views.generic import RedirectView
# from django.contrib import admin

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

# admin.autodiscover()

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'', include('catalog.urls')),
    # url(r'^$', include('catalog.urls')),
    # url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-countries/$', RedirectView.as_view(url='https://restcountries.eu/rest/v2/all'),name='api-countries'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


