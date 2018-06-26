from django.contrib import admin

from main.models import Download, Carousel, Testimonial, Package, PackagePrice, PackageTerm

admin.site.register(Download)
admin.site.register(Carousel)
admin.site.register(Testimonial)
admin.site.register(Package)
admin.site.register(PackageTerm)
admin.site.register(PackagePrice)
