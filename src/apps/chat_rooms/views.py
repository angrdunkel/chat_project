from django.shortcuts import render
from .forms import RoomForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
from django.views.generic import CreateView, TemplateView
from userprofiles.mixins import CreateViewMixin, TemplateViewMixin
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.urls import reverse

class CreateChatRoomView(CreateView, CreateViewMixin):
    form_class = RoomForm
    success_url = 'room_created'
    template_name = 'chat_rooms/new_room.html'
    template_name_ajax = 'chat_rooms/ajax/new_room_ajax.html'

    def get_template_names(self):
        if self.is_ajax():
            return [self.template_name_ajax]
        return [self.template_name]
    
    def form_valid(self, form):
         new_room = form.save(commit=False)
         new_room.room_creator = self.request.user
         new_room.save()

         return HttpResponseRedirect(reverse('room_created'))


class RoomCreatedView(TemplateView, TemplateViewMixin):
    success_url = None
    template_name = 'chat_rooms/room_created.html'
    template_name_ajax = 'chat_rooms/ajax/room_created_ajax.html'
    
    def get_template_names(self):
        if self.is_ajax():
            return [self.template_name_ajax]
        return [self.template_name]
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        return ctx