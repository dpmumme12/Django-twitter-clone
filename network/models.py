from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class profile(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="profile_user")
    following = models.ManyToManyField("User",  blank=True, related_name="following_user")
    followers = models.ManyToManyField("User",  blank=True, related_name="follower_user")

    def __str__(self):
        return self.user.username
 

class post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="post_user")
    body = models.TextField(blank=True)
    likes = models.ManyToManyField("User", blank=True, related_name="post_likes")
    date_posted = models.DateTimeField(auto_now_add = True, blank = True)

    def __str__(self):
        return self.user.username