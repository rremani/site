from __future__ import unicode_literals

from django.db import models


class HypoUser(models.Model):
    username = models.CharField(max_length=25, null=False, blank=False, unique=True)
    password = models.CharField(max_length=25, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
