from django.contrib.auth import get_user_model
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
    
    def get_crypto_file_user(self, user):
        if CryptoUserFile.objects.filter(user=user).exists():
            return CryptoUserFile.objects.get(user=user)
        else:
            print(user)
            create_crypto_user = CryptoUserFile(
                user=user,
            )
            create_crypto_user.save()
            return create_crypto_user