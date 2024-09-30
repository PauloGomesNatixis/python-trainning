# from django.urls import path

# from .views import homePageView

# urlpatterns = [
#     path('',homePageView, name = 'home')
# ]


# tickets/urls.py
from django.urls import path
from . import views

urlpatterns = [
#    path('',homePageView, name = 'home'),
    path('', views.ticket_list, name='ticket_list'),
    path('create/', views.create_ticket, name='create_ticket'),
]
