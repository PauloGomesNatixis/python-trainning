# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.

# def homePageView(request):
#     return HttpResponse('hello world')

# tickets/views.py
from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'pages/ticket_list.html', {'tickets': tickets})

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'pages/create_ticket.html', {'form': form})
