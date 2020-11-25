from django import forms
from django.forms import ModelForm

from model_hris.post.models import (
    Post,
    Comment
)

class PostForm(forms.ModelForm):
    description = forms.CharField(
                            label="",
                            widget=forms.Textarea(
                                attrs=
                                    {'rows': 3,'style' : "white-space: pre-wrap",'placeholder': "What's on your mind?"},
                                ),
                            )
    class Meta:
        model = Post
        fields = [
            'description',
        ]


class CommentForm(forms.ModelForm):
    description = forms.CharField(label="")
    class Meta:
        model = Comment
        fields = [
            'description',
        ]
