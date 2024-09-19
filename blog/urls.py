from django.urls import path
from blog.views import blog_home
from blog.views import blog_single


app_name='blog'
urlpatterns = [
    path('',blog_home,name='blog_home'),
    path('/single',blog_single,name='blog_single'),
    # path('/blog-home.html',blog_home,name='blog_home'),
    # path('/blog-single.html',blog_single,name='blog_single'),
]
