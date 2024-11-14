from django.db import models

class Folder(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=30)

class Reminder(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    hour = models.DateTimeField(auto_now_add=True)

