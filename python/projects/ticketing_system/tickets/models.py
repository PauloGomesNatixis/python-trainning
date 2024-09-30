from django.db import models

# Create your models here.
from django.contrib.auth.models import User  # Import the User model


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('suspend', 'Suspend'),
        ('in_pogress', 'In progress'),
        ('closed', 'Closed'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')  # Add ForeignKey for user
    # Make user field nullable for now
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets', null=True, blank=True)

    def __str__(self):
        return self.title



class Reply(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='replies', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply to {self.ticket.title}"