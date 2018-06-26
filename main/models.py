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


class Package(models.Model):
    title = models.CharField(max_length=1000)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class PackageTerm(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    term = models.CharField(max_length=1000)

    def __str__(self):
        return "{} : {}".format(self.package.title, self.term)


class PackagePrice(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, null=True, blank=True)
    price = models.CharField(max_length=100)

    def __str__(self):
        return "{} : {} : {}".format(self.package.title, self.price, self.description)
