from django.shortcuts import render
from .models import Post, Author, Tag


# Create your views here.


def landing_page(request):
    # only 3 results are fetched from database
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
    })


def load_post(request, slug):
    selected_post = Post.objects.get(slug=slug)
    return render(request, "blog/load-post.html", {
        "post": selected_post,
    })
