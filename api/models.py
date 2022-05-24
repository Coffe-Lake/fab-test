from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class Mailing(models.Model):
    begin_mailing = models.DateTimeField(verbose_name='Начало рассылки')
    end_mailing = models.DateTimeField(verbose_name='Конец рассылки')
    text = models.TextField(verbose_name='Текст сообщения')
    mobile_code = models.CharField(verbose_name='Код оператора', max_length=50, blank=True)
    tag = models.CharField(verbose_name='Теги для поиска', max_length=15)

    @property
    def to_send(self):
        now = timezone.now()
        if self.begin_mailing <= now <= self.end_mailing:
            return True

    @property
    def send_messages(self):
        return len(self.messages.filter(status='send'))

    @property
    def messages_delivered(self):
        return len(self.messages.filter(status='delivery'))

    @property
    def failed_send_messages(self):
        return len(self.messages.filter(status='fail'))

    def __str__(self):
        return f'Новая рассылка {self.id} от {self.begin_mailing}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Client(models.Model):
    phone = models.CharField(
        max_length=11,
        unique=True,
        verbose_name='Мобильный телефон',
        validators=[
            RegexValidator(
                regex=r'7[0-9]{10}',
                message='Формат ввода телефона 7XXXXXXXXXX (X - цифра от 0 до 9)'
            )
        ]
    )
    code = models.CharField(verbose_name='Код оператора', max_length=3)
    tag = models.CharField(verbose_name='Теги для поиска', max_length=50, blank=True)
    time_zone = models.CharField(verbose_name='Часовой пояс', max_length=15)

    def __str__(self):
        return f'Номер {self.phone}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    SENT = 'send'
    DELIVERING = 'delivery'
    FAILED = 'fail'

    MESSAGE_STATUS_CHOICES = [
        (SENT, "Отправка"),
        (DELIVERING, "Доставляется"),
        (FAILED, "Неуспешно"),
    ]

    date_message = models.DateTimeField(verbose_name="Дата отправки", auto_now_add=True)
    status = models.CharField(verbose_name='Статус отправки', max_length=10, choices=MESSAGE_STATUS_CHOICES)
    message = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    @property
    def __str__(self):
        return f'Сообщение {self.id} для {self.client}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
