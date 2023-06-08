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
    path(
        'accounts/profile/',
        views.ProfileView.as_view(),
        name='profile'
    ),
    re_path(
        r'^logout/',
        views.logout_view,
        name='logout'
    ),
    path(
        'registration-complite/',
        views.BaseRegistrationCompleteView.as_view(),
        name='registration_complite'
    ), 
]