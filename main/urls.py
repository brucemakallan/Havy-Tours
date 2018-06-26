from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('shop', views.shop, name='shop'),
    path('contact', views.contact, name='contact'),
    path('downloads', views.DownloadsListView.as_view(), name='downloads'),
    path('gallery', views.gallery, name='gallery'),
    path('packages', views.packages, name='packages'),
    path('sendmail', views.sendmail, name='sendmail')
]
