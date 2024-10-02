# tickets/urls.py
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import the auth views
from . import views

from .views import signup  # Import the signup view
from .views import edit_ticket # Import edit ticket 
from .views import ticket_detail
from .views import ticket_list
from .views import create_ticket
from .views import logout_view  # Import your custom logout view
#from .views import 


urlpatterns = [
    path('signup/', signup, name='signup'),  # Add this line for the signup view
    path('login/', auth_views.LoginView.as_view(next_page='/'), name='login'),  # Add this line for the login view
    path('', ticket_list, name='ticket_list'),
    path('create/', create_ticket, name='create_ticket'),
    path('ticket/<int:pk>/', ticket_detail, name='ticket_detail'),
    #path('edit/<int:ticket_id>/', edit_ticket, name='edit_ticket'),  # Add this line for the edit_ticket view
    path('edit/<int:ticket_id>/', edit_ticket, name='edit_ticket'),  # Add this line for the edit_ticket view
    
    #path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), 
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    #path('logout/',views.customlogout, name='logout'),
    path('logout/', logout_view, name='logout'),  # Use your custom logout view
]
