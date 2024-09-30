from email import message
from django.shortcuts import render,HttpResponse

# Create your views here.
from foo.models import Message

def index(request):
    messages = Message.objects.all()
    return render(request, 'foo/message.html',{'messages': messages})

