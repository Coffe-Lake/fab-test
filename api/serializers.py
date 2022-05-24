from rest_framework import serializers
from .models import Client, Message, Mailing


class ClientSerializer(serializers.ModelSerializer):
    """
    Сериализация для клиентов
    """

    class Meta:
        model = Client
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):
    """
    Сериализация рассылки
    """

    class Meta:
        model = Mailing
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    """
    Сериализация сообщения
    """

    class Meta:
        model = Message
        fields = '__all__'
