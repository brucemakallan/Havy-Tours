from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def booking(request):
    return render(request, 'main/booking.html')


def contact(request):
    return render(request, 'main/contact.html')


def downloads(request):
    return render(request, 'main/downloads.html')


def gallery(request):
    return render(request, 'main/gallery.html')


def packages(request):
    return render(request, 'main/packages.html')

