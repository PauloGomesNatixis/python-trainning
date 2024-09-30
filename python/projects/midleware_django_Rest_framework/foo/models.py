from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Mesage(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    message = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return f'{self.author}:{self.message}'
    
    class Meta:
        db_table = 'messages'