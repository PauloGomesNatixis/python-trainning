from django.shortcuts import render

from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
#from rest_framework.permissions import 

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def query_set(self):
        return Task.objects.filter(user=self.request.user)
    

# Create your views here.

# api_app/views.py
#from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


from .models import Task2
from .serializers import Task2Serializer
class Task2ViewSet(viewsets.ModelViewSet):
    queryset = Task2.objects.all()
    serializer_class = Task2Serializer


