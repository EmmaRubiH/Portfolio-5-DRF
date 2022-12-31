from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Popular(models.Model):
    """
    Comment model, related to User and Post
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="popular", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["owner", "post"]

    def __str__(self):
        return f"{self.owner} {self.post}"