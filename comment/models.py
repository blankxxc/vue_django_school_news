from django.db import models
from django.contrib.auth.models import User
from new.models import news
from django.urls import reverse


# 新闻的评论
class Comment(models.Model):
    new = models.ForeignKey(
        news,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.content[:20]
