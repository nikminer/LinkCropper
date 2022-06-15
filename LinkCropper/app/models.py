from django.db import models
from django.contrib.auth.models import User

# Счётчик папок
class CounterFolder(models.Model):
    folder = models.TextField(primary_key=True)
    count =  models.PositiveIntegerField(default=0)


# Идентификатор ссылки
class ReddirectId(models.Model):
    folder = models.TextField()
    linkid = models.PositiveIntegerField()


class ReddirectAnonymous(models.Model):
    id = models.ForeignKey(ReddirectId, primary_key=True, on_delete=models.CASCADE, unique=True)
    url = models.URLField()

class ReddirectUser(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
