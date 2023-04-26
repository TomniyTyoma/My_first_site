from django.db import models

class Feedback(models.Model):
    email = models.CharField(max_length=250)
    text = models.TextField()