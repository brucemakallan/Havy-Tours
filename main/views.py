from django.shortcuts import render
from django.views import generic

from main.models import Download, Carousel, Testimonial, Package, PackageTerm, PackagePrice


def index(request):
    carousel_items = Carousel.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'main/index.html', dict(
        carousel_items=carousel_items,
        testimonials=testimonials
    ))


def about(request):
    return render(request, 'main/about.html')


def booking(request):
    return render(request, 'main/booking.html')


def shop(request):
    return render(request, 'main/shop.html')


def contact(request):
    return render(request, 'main/contact.html')


class DownloadsListView(generic.ListView):
    model = Download
    context_object_name = 'download_entries'
    template_name = 'main/downloads.html'


def gallery(request):
    return render(request, 'main/gallery.html')


def packages(request):
    all_packages = Package.objects.all()
    all_package_terms = PackageTerm.objects.all()
    all_package_prices = PackagePrice.objects.all()
    return render(request, 'main/packages.html', dict(
        all_packages=all_packages,
        all_package_terms=all_package_terms,
        all_package_prices=all_package_prices
    ))


def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

