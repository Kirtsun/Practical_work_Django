from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from django_lifecycle import AFTER_UPDATE, LifecycleModel, hook

from .tasks import send_mail

User = get_user_model()


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    text = models.TextField()
    create_date = models.DateTimeField()
    published_date = models.DateTimeField()
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comments(LifecycleModel):
    name = models.CharField(max_length=50, null=True)
    text = models.TextField()
    published_date = models.DateTimeField()
    is_publish = models.BooleanField(default=False)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    @hook(AFTER_UPDATE, when="is_publish", was=False, is_now=True)
    def on_publish(self):
        send_mail.delay(subject='You have a new Comment', text=' http://127.0.0.1:8000'
                                                               + reverse('post_detail', args=[str(self.post.id)]),
                        to_email=self.post.author.email)

    def __str__(self):
        return self.text
