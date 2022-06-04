from ast import Str
from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    picture = models.ImageField(upload_to=' images', null=True, blank=True)
    body = models.TextField()
    liked = models.ManyToManyField(User, default=None, null=True, blank=True)
    # author
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def get_liked(self):
        return self.liked.all()

    @property
    def like_count(self):
        return self.liked.all().counts()

    # get user liked
    def get_user_liked(self):
        pass
