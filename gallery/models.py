from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery:image_detail', kwargs={'pk': self.pk})

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'image') # A user can like an image only once

    def __str__(self):
        return f'{self.user.username} likes {self.image.title}'


class Comment(models.Model):
    image = models.ForeignKey(Image, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.image.title}'