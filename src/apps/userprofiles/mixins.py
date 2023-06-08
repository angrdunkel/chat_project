from django.contrib.auth import get_user_model
from random import choice
from chat_rooms.models import Room

User = get_user_model()

class AjaxMixin:
    def is_ajax(self):
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return True
        return False
    
class AjaxTemplateMixin(object):
    
    def get_template_names(self, AjaxMixin):
        if self.request.is_ajax():            
            return [self.template_name_ajax]        
        return [self.template_name]

class TemplateViewMixin(AjaxMixin, AjaxTemplateMixin):
    pass

class LoginViewMixin(TemplateViewMixin):
    pass

class CreateViewMixin(TemplateViewMixin):
    
    def generate_username(self, size=8):
        allowed_chars = '0123456789'
        code = ''.join([choice(allowed_chars) for i in range(size)])
        return "".join([self.username_prefix, '-', code[0:4], '-', code[4:8]])
    
class ProfileViewMixins(TemplateViewMixin):
    
    def get_user_rooms(self):       
        return Room.objects.all().filter(room_creator=self.request.user)
