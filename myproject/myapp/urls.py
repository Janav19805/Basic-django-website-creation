from django.urls import path
from . import views


urlpatterns = [
    path("home", views.homepage),
    path("about", views.aboutpage),
    path("contact", views.contactpage),
    path("website", views.websitepage),
    path("form", views.formpageview),
    path("process", views.formpageprocess)
]