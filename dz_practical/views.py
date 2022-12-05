from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from django.contrib.auth import get_user_model
from dz_practical.forms import PostsForm
from dz_practical.models import Posts

User = get_user_model()


def post_new(request):
    if request.method == 'Post':
        form = PostsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostsForm()
    return render(request, 'dz_practical/new_post.html', {'form': form})


class UserPostUpdate(generic.UpdateView):
    model = Posts
    fields = ['title', 'text', 'is_publish']
    template_name = 'dz_practical/update_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Posts.objects.filter(owner=self.request.user)
        return posts
