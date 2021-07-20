from django.db import models
from Account.models import UserTable as User
# Create your models here.


class Text(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    coverImage = models.FileField(blank=True, null=True,)
    bookFile = models.FileField(blank=True, null=True,)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Prayer(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    coverImage = models.FileField(blank=True, null=True,)
    bookFile = models.FileField(blank=True, null=True,)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Knowledge(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    coverImage = models.FileField(blank=True, null=True,)
    bookFile = models.FileField(blank=True, null=True,)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Healing(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    coverImage = models.FileField(blank=True, null=True, )
    bookFile = models.FileField(blank=True, null=True, )
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Marriage(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    coverImage = models.FileField(blank=True, null=True, )
    bookFile = models.FileField(blank=True, null=True, )
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Novels(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    coverImage = models.FileField(blank=True, null=True, )
    bookFile = models.FileField(blank=True, null=True, )
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title