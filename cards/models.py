from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Card(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.title