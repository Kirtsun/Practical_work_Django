from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from django.contrib.auth import get_user_model
from .forms import PostsForm, CommentsForm
from .models import Posts, Comments
from .tasks import send_mail

User = get_user_model()


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            post.published_date = timezone.now()
            post.save()
            send_mail.delay(subject='You have a new Post', text=form.cleaned_data['text'],
                            to_email='admin@gmail.com')
            return redirect('post')
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


def create_comments(request, pk):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.published_date = timezone.now()
            comm.post_id = pk
            comm.save()
            send_mail.delay(subject='You have a new Comment', text=form.cleaned_data['text'],
                            to_email='admin@gmail.com')
            post = get_object_or_404(Posts, pk=pk)
            user_email = post.author.email
            send_mail.delay(subject='You have a new Comment', text=form.cleaned_data['text'],
                            to_email=user_email)
            return redirect('post_detail', pk=pk)
    else:
        form = CommentsForm()
    return render(request, 'dz_practical/create_comments.html', {'form': form, 'pk': pk})


class PostList(generic.ListView):
    model = Posts
    queryset = Posts.objects.select_related("author")
    paginate_by = 5
    template_name = 'dz_practical/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Posts.objects.filter(is_publish=True)
        return posts


def author_post(request, pk):
    post = Posts.objects.filter(author_id=pk, is_publish=True)
    return render(request, 'dz_practical/author_post.html', {'post': post})


def detail_post(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    comm = post.comments_set.filter(is_publish=True)
    return render(request, 'dz_practical/post_detail.html', {'post': post, 'comm': comm})




