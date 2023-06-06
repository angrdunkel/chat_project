from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _

class Rooms(models.Model):
    room_creator = models.ForeignKey(
       settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        related_name='room_creator',
        on_delete=models.CASCADE,
    )
    name  = models.CharField(
        _('Room name'), 
        max_length=50,
        blank=True, 
        null=True
    )
    created_at = models.DateTimeField(
        _('Created at'), 
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class UserRooms(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        Rooms,
        verbose_name=_("Chat Room"),
        related_name='room',
        on_delete=models.CASCADE,
    ) 
    created_at = models.DateTimeField(
        _('Created at'), 
        auto_now_add=True
    )  
    def __str__(self):
        return self.room

class Message(models.Model):
    room = models.ForeignKey(
        Rooms,
        verbose_name=_("Chat Room"),
        related_name='room_message',
        on_delete=models.CASCADE,
    )
    message = models.TextField(
        _("Text"),
        default=""
    )  
    created_at = models.DateTimeField(
        _('Created at'), 
        auto_now_add=True
    ) 
    user_message = models.ForeignKey(
       settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        related_name='user_message',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user_message