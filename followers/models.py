from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    owner = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)


class Meta:
    unique_together = ['owner', 'followed']


def __str__(self):
    return f'{self.owner} {self.followed}'
