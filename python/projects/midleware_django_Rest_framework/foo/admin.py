from django.contrib import admin

# Register your models here.
from foo.models import Message

class MessagesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessagesAdmin)