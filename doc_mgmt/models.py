from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return 'User {}'.format(self.name)


class Document(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ManyToManyField(User)

    def __str__(self):
        return 'Document {} by {}'.format(self.title, self.author.name)

