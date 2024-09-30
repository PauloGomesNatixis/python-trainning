# tickets/views.py
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, Reply
from .forms import TicketForm, ReplyForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.db.models import Q


#@login_required
def ticket_list(request):
    query = request.GET.get('q')
    
    if isinstance(request.user, AnonymousUser):
        return redirect('login')  # Redirect to login if not logged in
    
#    tickets = Ticket.objects.all()
#    return render(request, 'ticket_list.html', {'tickets': tickets})

    if request.user.is_staff:  # Check if the user is admin (staff or superuser)
        tickets = Ticket.objects.all()  # Admin users can see all tickets
    else:
        tickets = Ticket.objects.filter(user=request.user)  # Regular users see only their tickets

    if query:
        tickets = tickets.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'ticket_list.html', {'tickets': tickets})


# def create_ticket(request):
#     if request.method == 'POST':
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('ticket_list')
#     else:
#         form = TicketForm()
#     return render(request, 'create_ticket.html', {'form': form})


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # Associate the ticket with the current user
            ticket.save()
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



@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    
    # Check if the user is an admin
    if not request.user.is_staff:
        return redirect('ticket_list')  # Redirect non-admins to ticket list
    
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')  # Redirect to the ticket list after saving
    else:
        form = TicketForm(instance=ticket)  # Use the current ticket instance

    return render(request, 'edit_ticket.html', {'form': form, 'ticket': ticket})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after sign up
            return redirect('ticket_list')  # Redirect to the ticket list or any other page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



# @login_required
# def logout(reqest):
#     logout(request)
#     return reqest
# @login_required
# def logout_view(request):
#     auth_logout(request)  # This logs out the user
#     return render(request, 'registration/logout.html')  # Render the logout template

@login_required
def logout_view(request):
    auth_logout(request)  # This logs out the user
    return redirect('ticket_list')  # Redirect to the home page