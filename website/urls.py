from django.urls import path
from . import views
from .views import contact_form, success

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', contact_form, name='contact_form'),
    path('success/', success, name='success'),
]
