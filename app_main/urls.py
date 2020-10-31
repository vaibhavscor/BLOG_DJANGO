from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.home_page,name='home'),
    path('search',views.searchkey,name='search'),
    path('read_blog/<str:slug>', views.blog_read,name='slug'),
]
