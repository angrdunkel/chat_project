from django.urls import include, path, re_path

from . import views

urlpatterns = [      
    path(
        '',
        views.SignInViev.as_view(),
        name='login'
    ),
    path(
        'user-registration/',
        views.UserRegistrationView.as_view(),
        name='user_registration'
    ),
]