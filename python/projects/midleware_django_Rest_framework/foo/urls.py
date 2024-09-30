from django.urls import path
from foo import views

urlpatterns = [
    path('', views.index, name = 'index')
]