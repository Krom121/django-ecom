from django.db import models


class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.name