from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  #home page url
    url(r'^(?P<id>\d+)/$', views.result, name='result'), #result url, uses result's pk as a slug
    url(r'^about/$', views.about, name='about'), #about page url
    url(r'^contact/', views.contact, name='contact'), #contact page url
]