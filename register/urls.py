from django.contrib.auth import views as viewss
from django.urls import path, reverse_lazy

from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/", viewss.LoginView.as_view(next_page='/dz_practical/'), name="login"),
    path("logout/", viewss.LogoutView.as_view(), name="logout"),

    path("password_change/", viewss.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", viewss.PasswordChangeDoneView.as_view(), name="password_change_done"),

    path("password_reset/", viewss.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')),
         name="password_reset"),
    path("password_reset/done/", viewss.PasswordResetDoneView.as_view(), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", viewss.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", viewss.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("registration/", views.registers, name='registration')
]
