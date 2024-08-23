from django.db import models
from user.models import User
from shortsapi import settings


class Short(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='post')
    caption = models.TextField()
    content = models.FileField(upload_to=settings.UPLOAD_POST_FOLDER,
                               max_length=200,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='likes_user')
    short = models.ForeignKey(Short, on_delete=models.CASCADE,
                             related_name='likes_short')
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comment_user')
    short = models.ForeignKey(Short, on_delete=models.CASCADE,
                             related_name='comment_short')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='share_user')
    short = models.ForeignKey(Short, on_delete=models.CASCADE,
                             related_name='share_short')
    to_user = models.IntegerField(null= False)
    created_at = models.DateTimeField(auto_now_add=True)
