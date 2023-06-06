from django.db import models

from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.conf import settings
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import MyUserManager

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        (1, 'Administrator'),
        (2, 'user'),
    )
    id = models.AutoField(
        primary_key=True, 
        unique=True
    )
    username = models.CharField(
        max_length=50, 
        unique=True,
    )
    
    email = models.EmailField(
        max_length=100, 
        unique=True
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(
        _('First Name'),
        max_length=128,
        blank=True,
        default=''
    )
    last_name = models.CharField(
        _('Last Name'),
        max_length=128,
        blank=True,
        default=''
    )
    middle_name = models.CharField(
        _('Middle name'), max_length=50,
        blank=True, null=True
    )
    type = models.PositiveIntegerField(
        _('Type'), help_text=_('User type'),
        choices=USER_TYPES,
        default=1
    )
    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now,
        null=True, blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return self.email