from django.db import models


class Review(models.Model):
    logo = models.ImageField(upload_to='logos/')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review #{self.id}"
