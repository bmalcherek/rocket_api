import hashlib

from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.base import Model


def get_hash(content) -> str:
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


class RocketModel(models.Model):
    model = models.TextField(unique=True, primary_key=True)
    name = models.TextField()
    reusable = models.BooleanField()
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self) -> str:
        return self.name

    def hash(self) -> str:
        return get_hash(str(self.date_modified))


class Booster(models.Model):
    model = models.ForeignKey(RocketModel, on_delete=models.PROTECT)
    code = models.TextField(unique=True, primary_key=True)
    launches_count = models.IntegerField(default=0)
    expended = models.BooleanField(default=False)
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self) -> str:
        return self.code

    def hash(self) -> str:
        return get_hash(str(self.date_modified))


class LaunchPlatform(models.Model):
    code = models.TextField(unique=True, primary_key=True)
    location = models.TextField()
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self) -> str:
        return self.code

    def hash(self) -> str:
        return get_hash(str(self.date_modified))


class Payload(models.Model):
    weight = models.IntegerField(validators=[MinValueValidator(0.0)])
    name = models.TextField()
    delivered = models.BooleanField(default=False)
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self) -> str:
        return self.name

    def hash(self) -> str:
        return get_hash(str(self.date_modified))


class Launch(models.Model):
    booster = models.ForeignKey(Booster, on_delete=models.PROTECT)
    payload = models.ForeignKey(Payload, on_delete=models.PROTECT)
    launch_platform = models.ForeignKey(
        LaunchPlatform, on_delete=models.PROTECT)
    start_time = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def hash(self) -> str:
        return get_hash(str(self.date_modified))


class Token(models.Model):
    token = models.TextField(primary_key=True)


class Decomission(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    model = models.ForeignKey(RocketModel, on_delete=models.CASCADE)
