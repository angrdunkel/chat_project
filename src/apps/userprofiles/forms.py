from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class RememberLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False, widget=forms.CheckboxInput()
    )

class BaseRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, 
        help_text=''
    )
    first_name = forms.CharField(
        max_length=30, 
        required=False, 
        help_text=''
    )
    last_name = forms.CharField(
        max_length=30, 
        required=False, 
        help_text=''
    )

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',           
            'password1', 
            'password2', 
        ]

class UserRegistrationForm(BaseRegistrationForm):
    pass