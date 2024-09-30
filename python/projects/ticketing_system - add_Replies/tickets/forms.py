# tickets/forms.py
from django import forms
from .models import Ticket, Reply

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['message']
