from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    time = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
