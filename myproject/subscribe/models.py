from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    name = models.TextField(max_length=30)
    email = models.TextField(max_length=30)
    nationality= models.TextField(max_length=25)

