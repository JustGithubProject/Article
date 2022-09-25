from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("news/", news),
    path("novosti/", news_number_2)
]