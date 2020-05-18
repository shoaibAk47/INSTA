from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
# Create your models here.
class Entity(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='entities'
    )
    sdfasfasd
    image=models.URLField()
    tags = ArrayField(models.CharField(max_length=200), blank=True)
    height=models.IntegerField()
    width=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

