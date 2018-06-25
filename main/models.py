from django.db import models


class Download(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    file_type = models.CharField(max_length=10)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Carousel(models.Model):
    url = models.CharField(max_length=1000)

    def __str__(self):
        return "url: {}".format(self.url)


RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    rating = models.IntegerField(default=4, choices=RATING_CHOICES)

    def __str__(self):
        return self.name
