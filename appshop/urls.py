from django.urls import path
from .import views


urlpatterns = [
    path('', views.index),
    path('Blog', views.Blog),
    path('offer', views.Offer),
]
