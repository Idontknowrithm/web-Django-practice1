from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm
from .forms import LoginForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'
    
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'
    
    # make session
    def form_valid(self, form):
        self.request.session['user'] = form.user_id
        
        return super().form_valid(form)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')