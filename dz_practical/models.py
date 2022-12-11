from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField()
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comments(models.Model):
    name = models.CharField(max_length=50, null=True)
    text = models.TextField()
    published_date = models.DateTimeField()
    is_publish = models.BooleanField(default=False)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

