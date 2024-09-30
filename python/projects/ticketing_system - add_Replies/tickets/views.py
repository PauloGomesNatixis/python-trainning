# tickets/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, Reply
from .forms import TicketForm, ReplyForm

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    replies = ticket.replies.all()

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.ticket = ticket
            reply.save()
            return redirect('ticket_detail', pk=ticket.pk)
    else:
        form = ReplyForm()

    return render(request, 'ticket_detail.html', {
        'ticket': ticket,
        'replies': replies,
        'form': form
    })
