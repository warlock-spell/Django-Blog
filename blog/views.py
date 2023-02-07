from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag
from django.views.generic import ListView
from .forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

class LandingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]


class AllPostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]


class PostDetailView(View):
    model = Post
    template_name = "blog/load-post.html"

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, self.template_name,
                      {
                          "post": post,
                          "post_tags": post.tags.all(),
                          "comment_form": CommentForm(),
                          # remove the comments key, if you only want submissions
                          "comments": post.comments.all().order_by("-id"),
                      })

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            # commit=False means that we don't want to save the model, yet
            # it will create a model instance but not hit it to the database
            comment = comment_form.save(commit=False)
            # since the post field is not in the form, we need to set it manually
            # linking comment to the post
            comment.post = post
            # hit the edited object to the database
            comment.save()
            return HttpResponseRedirect(reverse("load-post", args=[slug]))

        # if form is invalid, re-render the page with the form data
        context = {
            # comment_form from above is pre-filled with user data
            "comment_form": comment_form,
            "post": post,
            "post_tags": post.tags.all(),
            # remove the comments key, if you only want submissions
            "comments": post.comments.all().order_by("-id"),
        }
        return render(request, self.template_name, context=context)
