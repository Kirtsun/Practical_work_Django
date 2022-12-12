from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count, Q
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
    author = get_object_or_404(User, pk=request.user.id)
    page_obj = author.posts_set.filter(is_publish=True)
    paginator = Paginator(page_obj, 5)
    page_obj = request.GET.get('page')
    page_obj = paginator.get_page(page_obj)
    return render(request, 'userprofile/my_profile.html', {'author': author, 'page_obj': page_obj})


class UpdateProfile(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ["username", "email"]
    template_name = 'userprofile/update_profile.html'
    success_url = reverse_lazy("userprofile:my_profile")
    success_message = "Profile updated"

    def get_object(self, queryset=None):
        user = self.request.user
        return user


