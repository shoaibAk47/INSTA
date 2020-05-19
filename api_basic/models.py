from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
# Create your models here.
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
    image=models.URLField()
    #tags = ArrayField(models.CharField(max_length=200), blank=True)
    height=models.IntegerField()
    width=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "USERENTITIES"
        ordering = ['-created_at']


class EntityTags(models.Model):
    title=models.CharField(max_length=200)
    relentity=models.ManyToManyField(Entity, related_name='tags_list', through='Rel')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users_tag'
    )


class Rel(models.Model):
    tags=models.ForeignKey(EntityTags, on_delete=models.CASCADE)
    entity=models.ForeignKey(Entity, on_delete=models.CASCADE)

    