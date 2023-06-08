from django.contrib.auth import get_user_model
from django import forms

from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']