from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('clients', ClientViewSet)
router.register('message', MessageViewSet)
router.register('mailing', MailingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
