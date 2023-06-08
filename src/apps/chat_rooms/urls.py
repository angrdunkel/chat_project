from django.urls import include, path, re_path
from . import views


urlpatterns = [
    path(
        'room-created/',
        views.RoomCreatedView.as_view(),
        name='room_created'
    ), 
    path(
        'room-create/',
        views.CreateChatRoomView.as_view(),
        name='room_create'
    ),
]
