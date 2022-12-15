from django import forms
from django.contrib.auth import get_user_model

from .models import Comments, Posts


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
