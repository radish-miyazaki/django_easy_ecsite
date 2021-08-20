from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm, UserLoginForm


class HomeView(TemplateView):
    template_name = 'home.html'


class RegisterUserView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm


class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm

    def form_valid(self, form):
        remember = form.cleaned_data.get('remember')
        if remember:
            self.request.session.set_expiry(1200000)
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    pass


# @method_decorator(login_required, name='dispatch') # Decoratorを用いて、View全体に適用
# Mixinを指定して、View全体に適用
class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user.html'

    # @method_decorator(login_required) # request時に実行されるdispatchに適用
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
