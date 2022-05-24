from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ClientSerializer, MessageSerializer, MailingSerializer
from .models import Client, Message, Mailing


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()
