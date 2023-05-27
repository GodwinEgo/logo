from django.db import models

class Logo(models.Model):
    name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='logos/')


class Review(models.Model):
    logo = models.ForeignKey(Logo, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)