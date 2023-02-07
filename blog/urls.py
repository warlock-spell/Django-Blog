# @Project:     my_site
# @Filename:    urls.py
# @Author:      Daksh
# @Time:        24-01-2023 12:28 am

from django.urls import path
from . import views

urlpatterns = [
    path("", views.LandingPageView.as_view(), name="landing-page"),
    path("posts", views.AllPostsView.as_view(), name="posts"),
    # slug is a unique identifier for a post
    # use slug for SEO friendly URLs
    # slug is a string that can contain letters, numbers, underscores, and hyphens
    # e.g. my-first-post
    # slug-transformer assures that given string is a valid slug
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="load-post")
]
