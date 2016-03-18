from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'login/$', views.log_in, name='login'),
    url(r'logout/$', views.log_out, name='logout'),
    url(r'edit/(?P<pk>\d+)/$', views.post_edit, name='post_edit'),
    url(r'delete/(?P<pk>\d+)/$', views.post_delete, name='post_delete'),
    url(r'new/', views.post_new, name='post_new'),
]
