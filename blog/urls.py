from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^$', views.encourage, name='encourage'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^mobile/post/$', views.post_mobile_list, name='post_mobile_list'),
    url(r'^mobile/post/(?P<pk>[0-9]+)/edit/$', views.post_mobile_edit, name='post_mobile_edit'),
    url(r'^mobile/post/add/$', views.post_mobile_add, name='post_mobile_add'),
]
