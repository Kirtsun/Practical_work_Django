from django.shortcuts import redirect, render
from django.utils import timezone

from dz_practical.forms import PostsForm


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
    return render(request, 'new_post.html', {'form': form})
