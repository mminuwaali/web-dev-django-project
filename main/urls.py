from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('quote', views.quote_view, name='quote'),
    path('members', views.member_view, name='member'),
    path('service', views.service_view, name='service'),
    path('pricing', views.pricing_view, name='pricing'),
    path('contact', views.contact_view, name='contact'),
]
