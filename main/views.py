from django.shortcuts import render
from django.views import generic

from main.models import Download, Carousel, Testimonial


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
    return render(request, 'main/packages.html')

