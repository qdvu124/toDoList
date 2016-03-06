from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/edit$',views.post_edit, name='post_edit'),
    ]
