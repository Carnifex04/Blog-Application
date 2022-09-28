from django.db import models


# Create your models here.

class Post(models.Model):
    posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, default='')
    title = models.CharField(max_length=150, blank=True, default='')
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['posted']

    def __str__(self):
        return self.title
