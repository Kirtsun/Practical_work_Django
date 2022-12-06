from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from django.contrib.auth import get_user_model
from .forms import PostsForm, CommentsForm
from .models import Posts
from .tasks import send_mail

User = get_user_model()


@login_required
def post_new(request):
    if request.method == 'Post':
        form = PostsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            send_mail.delay(subject='You have a new Post', text=form.cleaned_data['text'],
                            admin_email='admin@gmail.com')
            return redirect('index')
    else:
        form = PostsForm()
    return render(request, 'dz_practical/new_post.html', {'form': form})


class UserPostUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Posts
    fields = ['title', 'text', 'is_publish']
    template_name = 'dz_practical/update_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Posts.objects.filter(owner=self.request.user)
        return posts


def create_comments(request):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.published_date = timezone.now()
            comm.save()
            send_mail.delay(subject='You have a new Comment', text=form.cleaned_data['text'],
                            admin_email='admin@gmail.com')

            return redirect('index')
    else:
        form = CommentsForm()
    return render(request, 'templates/create_comments.html', {'form': form})
