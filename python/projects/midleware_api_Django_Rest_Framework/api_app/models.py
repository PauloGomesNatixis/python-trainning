from django.db import models
from sqlalchemy import Boolean

class Message(models.Model):
    message = models.CharField(max_length=100)

# Create your models here.


# api_app/models.py
#from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title



##################
class Task2(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    modified = models.CharField(max_length=1000)
    complete = models.CharField(boolean=False)
    
    


