from django.urls import path,include
from blog.views import *

urlpatterns = [
    path("",PostListView.as_view(),name='home'),
    
    path("search",search,name='search'),

    path("Blog/<slug:slug>",PostDetailView.as_view(),name='Blog Details'),

    path("Category/<slug:slug>",category_page,name='Category Page'),

    path("Contact Us",ContactUsFormView.as_view(),name='Contact Us'),

    path("create blog",PostCreateView.as_view(),name='Create Blog'),
    
    path("Blog/<slug:slug>/update",PostUpdateView.as_view(),name='Update Blog'),
    path("Blog/<slug:slug>/delete",PostDeleteView.as_view(),name='Delete Blog'),
    
    path('thank_you',thank_you,name='Thank You'),

    path('My Blog/<slug:slug>',MyBlog,name='My Blog'),
    path('My Blog/<slug:slug>/Draft',DraftBlog,name='Draft Blog'),
    path('My Blog/<slug:slug>/Published',PublishedBlog,name='Published Blog'),
]
