from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Todo(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    reg_dt = models.DateTimeField(auto_now_add=True)
