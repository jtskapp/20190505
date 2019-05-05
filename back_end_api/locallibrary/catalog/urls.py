from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^countries/$', views.country, name='countries'),
    url(r'book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^api/$', views.BookListAPIView.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.BookListDetailAPIView.as_view()),

    url(r'^api/test$', views.EndPointTestListAPIView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
