# @Project:     my_site
# @Filename:    forms.py
# @Author:      Daksh
# @Time:        07-02-2023 03:44 pm

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {"user_name": "Your Name", "user_email": "Your Email", "text": "Your Comment"}
