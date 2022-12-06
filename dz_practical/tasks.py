from celery import shared_task

from django.core.mail import send_mail as mail_


@shared_task()
def send_mail(subject, text, admin_email):
    mail_(subject, text, 'company_mail@gmail.com', [admin_email], fail_silently=False)
