from django.contrib import admin

# Register your models here.
from .models import Mailing, Client, Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'begin_mailing', 'text', 'end_mailing')
    search_fields = ('begin_mailing',)
    list_filter = ('text',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'phone', 'code', 'tag')
    search_fields = ('phone',)
    list_filter = ('tag',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_message', 'status', 'message')
    search_fields = ('date_message',)
    list_filter = ('status',)
