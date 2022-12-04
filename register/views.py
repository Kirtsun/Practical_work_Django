from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegisterForm


class RegisterFormView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        # form.cleaned_data.get("password1")

        # username = self.request.POST['username']
        # password = self.request.POST['password1']

        user = authenticate(self, username=user.username, password=user._password)
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)
