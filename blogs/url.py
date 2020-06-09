from django.contrib import admin
from django.urls import path,include

from .views import *


urlpatterns=[

    path("",IndexView.as_view(),name="index"),
    path("detail/<int:pk>/<slug:slug>",PostDetail.as_view(),name="detail"),
    path("category/<int:pk>/<slug:slug>",CategoryDetail.as_view(),name="category_detail"),
    path("create_post/",CreatePostView.as_view(),name="create_post"),
    path("post_update/<int:pk>/<slug:slug>",UpdatePostView.as_view(),name="post_update"),
    path("post_delete/<int:pk>/<slug:slug>",DeletePostView.as_view(),name="post_delete"),
    path("search/",SearchView.as_view(),name="search"),
    path("categories/",Categories.as_view(),name="categories")
]