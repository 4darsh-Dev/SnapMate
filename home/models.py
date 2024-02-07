from django.db import models

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=100)
    favorite_colors = models.CharField(max_length=100)  # For simplicity, store as comma-separated values
    favorite_songs = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Optional field

    def __str__(self):
        return self.name
    