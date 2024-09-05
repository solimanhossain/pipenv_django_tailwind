from django.urls import path
from theme import views

urlpatterns = [
    path('', views.base, name='base'),
]