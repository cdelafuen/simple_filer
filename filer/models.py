from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class FileLog(models.Model):

    start_datetime = models.DateTimeField(auto_now_add=True)
    finish_datetime = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User)
