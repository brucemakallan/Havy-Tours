from django.shortcuts import render
from django.views import generic

from main.models import Download, Carousel


class IndexListView(generic.ListView):
    model = Carousel
    context_object_name = 'carousel_items'
    template_name = 'main/index.html'


def about(request):
    return render(request, 'main/about.html')


def booking(request):
    return render(request, 'main/booking.html')


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

