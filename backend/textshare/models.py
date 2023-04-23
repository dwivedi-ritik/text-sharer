from django.db import models

# Create your models here.


class Textshare(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"{id}"

    class Meta:
        ordering = ['created_at']
