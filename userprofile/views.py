from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic

from django.contrib.auth import get_user_model
from dz_practical.models import Posts, Comments

User = get_user_model()


def public_profile(request, pk):
    author = get_object_or_404(User, pk=pk)
    post = author.posts_set.filter(is_publish=True)
    return render(request, 'userprofile/author_profile.html', {'author': author, 'post': post})


@login_required
def my_profile(request):
    a = request.user.id
    author = get_object_or_404(User, pk=a)
    post = author.posts_set.filter(is_publish=True)
    return render(request, 'userprofile/my_profile.html', {'author': author, 'post': post})


class UpdateProfile(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ["username", "email"]
    template_name = 'userprofile/update_profile.html'
    success_url = reverse_lazy("post")
    success_message = "Profile updated"

    def get_object(self, queryset=None):
        user = self.request.user
        return user


