from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^books/(?P<num>\d+)$', views.books),
    url(r'^authors$', views.authors),
    url(r'^addAuthor$', views.addAuthor)
]