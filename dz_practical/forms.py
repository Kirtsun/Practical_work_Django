from django import forms
from django.contrib.auth import get_user_model
from .models import Posts, Comments
from datetime import timedelta

from django.core.exceptions import ValidationError
from django.utils import timezone

User = get_user_model()


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'text', 'is_publish')


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'text',)


class Mail(forms.Form):
    mail = forms.EmailField(label='You email')
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": "10"}))

