#from django.contrib import admin

# Register your models here.
# tickets/admin.py
from django.contrib import admin
from .models import Ticket

admin.site.register(Ticket)
