from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model, login as auth_login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import RememberLoginForm

User = get_user_model()

#def logout_view(request):
#    logout(request)
#    messages.success(request, 'You are logged out.')
 #   return HttpResponseRedirect(reverse('home_page'))

class SignInViev(LoginView, LoginViewMixin):
    redirect_authenticated_user = True
    form_class = RememberLoginForm
    template_name = 'registration/login.html'
    
    def get_template_names(self):
        if self.is_ajax():
            return [self.template_name_ajax]
        return [self.template_name]

    def get_success_url(self):
        print(self.is_step2verification())
        return super().get_success_url()

    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        print(f'Error {self.request}')
        print(self.request.POST.get('username'))
        return self.render_to_response(self.get_context_data(form=form))
    
    def form_valid(self, form):
        auth_login(self.request, form.get_user())
                
        if self.is_ajax():
            if self.request.user.is_client:
                return JsonResponse({
                    "status": "ok",
                    "redirect_url": self.get_success_url(),
                })
        
        return HttpResponseRedirect(self.get_success_url()) 