
from django.db import models,connection
from django.contrib.auth.models import User

# Create your models here.
class Twitter(models.Model):
    text = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"Tweet by {self.author.username}: {self.text[:50]}..."

class Like(models.Model):
    like = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like' )
    tweet = models.ForeignKey(Twitter, on_delete=models.CASCADE,related_name='like')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"{self.like.username} liked {self.tweet.id}"

class Follow(models.Model):
    other_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    between_users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.other_user.username} follows {self.between_users.username}"