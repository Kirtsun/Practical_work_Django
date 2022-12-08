from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegisterForm


class RegisterFormView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy("post")

    def form_valid(self, form):
        user = form.save()
        user = authenticate(self.request, username=user.username, password=form.cleaned_data.get("password1"))
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)
