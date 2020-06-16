from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=64)
  author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
  body = models.TextField(default = "hey this is a joke!")
  def __str__(self):
    return self.title