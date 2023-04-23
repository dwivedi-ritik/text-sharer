from django.db import models
from django.contrib import auth
from django.db import models
from django.contrib import auth

# Create your models here.


class Textshareauth(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    body = models.TextField(max_length=5000)
    created_by = models.ForeignKey(
        auth.get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "{}-{}".format(self.id, self.title)
