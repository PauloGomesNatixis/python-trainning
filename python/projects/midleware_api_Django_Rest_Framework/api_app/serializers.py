from email.policy import default
from unittest import result
from urllib import request
from rest_framework import serializers
from sqlalchemy import PrimaryKeyConstraint


from .models import Message
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message']


from .models import Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed']
        
        
from .models import Task2
class Task2Serializer(serializers.ModelSerializer):
    #user=PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())
    class Meta:
        model = Task
        fields = ['title', 'description', 'modified', 'completed', 'user']
        
    def create(self, validated_data):
        reques= self.context.get('request')
        assert request
        result = Task(
            user=request.user,
            **validated_data,
        )
        return super().create(validated_data)()    