from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic

from django.contrib.auth import get_user_model
from django.views.decorators.cache import cache_page

from .forms import PostsForm, CommentsForm, Mail
from .models import Posts, Comments
from .tasks import send_mail

User = get_user_model()


@login_required(login_url='/register/login/')
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
        posts = Posts.objects.filter(author=self.request.user)
        return posts

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.id})


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
            return redirect('post_detail', pk=pk)
    else:
        form = CommentsForm()
    return render(request, 'dz_practical/create_comments.html', {'form': form, 'pk': pk})


@method_decorator(cache_page(10), name='dispatch')
class PostList(generic.ListView):
    model = Posts
    paginate_by = 5
    template_name = 'dz_practical/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        cont = Count('comments', filter=Q(comments__is_publish=True))
        posts = Posts.objects.filter(is_publish=True).annotate(cont=cont)
        return posts


def author_post(request, pk):
    author = get_object_or_404(User, pk=pk)
    page_obj = author.posts_set.filter(is_publish=True).annotate(cont=Count('comments',
                                                                        filter=Q(comments__is_publish=True)))
    paginator = Paginator(page_obj, 5)
    page_obj = request.GET.get('page')
    page_obj = paginator.get_page(page_obj)
    return render(request, 'dz_practical/author_post.html', {'page_obj': page_obj, 'author': author})


def detail_post(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    comm = post.comments_set.filter(is_publish=True)
    paginator = Paginator(comm, 5)
    page_number = request.GET.get('page')
    comm = paginator.get_page(page_number)
    return render(request, 'dz_practical/post_detail.html', {'post': post, 'comm': comm})


class MyBlanks(LoginRequiredMixin, generic.ListView):
    model = Posts
    template_name = 'dz_practical/my_blanks.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        posts = Posts.objects.filter(author=self.request.user, is_publish=False)
        return posts

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.id})


@login_required()
def contact_form(request):
    if request.method == "POST":
        form = Mail(request.POST)
        if form.is_valid():
            to_mail = form.cleaned_data['mail']
            text = form.cleaned_data['text']
            subject = 'Author need your help'
            send_mail.delay(subject, text, to_mail)
            return redirect('post')
    else:
        form = Mail()
    return render(request, 'dz_practical/contact_form.html', {'form': form})

