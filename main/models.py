from django.db import models


class Download(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    file_type = models.CharField(max_length=10)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
