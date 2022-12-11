from django.urls import path
from .views import Watsapp

urlpatterns = [
    path('', Watsapp)
]