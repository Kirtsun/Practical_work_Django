from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm


def registers(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_user = authenticate(request, username=new_user.username,
                                    password=user_form.cleaned_data.get("password"))
            login(request, new_user)
            return redirect('post')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})
