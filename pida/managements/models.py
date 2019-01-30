from django.db import models


class Notice(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    written_time = models.DateTimeField(auto_now_add=True)


class Faq(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    written_time = models.DateTimeField(auto_now_add=True)
