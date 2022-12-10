from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from django.contrib.auth import get_user_model
from dz_practical.models import Posts, Comments

User = get_user_model()


def public_profile(request, pk):
    author = get_object_or_404(User, pk=pk)
    post = author.posts_set.filter(is_publish=True)
    return render(request, 'userprofile/author_profile.html', {'author': author, 'post': post})


def my_profile(request):
    a = request.user.id
    author = get_object_or_404(User, pk=a)
    post = author.posts_set.filter(is_publish=True)
    return render(request, 'userprofile/my_profile.html', {'author': author, 'post': post})
