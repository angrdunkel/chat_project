from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model, login as auth_login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib import messages
from .forms import RememberLoginForm, UserRegistrationForm
from .mixins import LoginViewMixin, CreateViewMixin

User = get_user_model()

def logout_view(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return HttpResponseRedirect(reverse('home_page'))

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


class BaseRegistrationView(CreateView, CreateViewMixin):
    form_class = UserRegistrationForm
    success_url = 'registration_complite'
    template_name = 'registration/registration.html'
    username_prefix = ''
    user_type = 0

    def get_template_names(self):
        if self.is_ajax():
            return [self.template_name_ajax]
        return [self.template_name]
    
    def create_inactive_user(self, form):
        new_user = form.save(commit=False)
        new_user.is_active = False
        new_user.type = self.user_type
        username_exists = True
        while username_exists:
            new_username = self.generate_username()
            try:
                old_user = User.objects.get(username=new_username)
            except:
                username_exists = False
                new_user.username = new_username
        new_user.save()

        self.after_user_save(new_user, form)

        #self.send_activation_email(new_user)

        return new_user

    def form_valid(self, form):
        new_user = self.register(form)
        
        if self.is_ajax():
           return JsonResponse({
                        "status": "ok",
                        "url": reverse('registration_complite'),
                  })
            
        return HttpResponseRedirect(reverse('registration_complite'))

    def register(self, form):
        new_user = self.create_inactive_user(form)
        signals.user_registered.send(
            sender=self.__class__,
            user=new_user,
            request=self.request
        )
        return new_user
    
    def after_user_save(self, user, form):
        pass

class UserRegistrationView(BaseRegistrationView):
    username_prefix = 'USR'
    user_type = 2