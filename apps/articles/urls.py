from django.urls import path
from .views import index_view,blog_single,blog_view

urlpatterns=[
    path('',index_view,name='index'),
    path('detail/<int:pk>/',blog_single,name='detail'),

    path('blog/',blog_view,name='blog_list')
]