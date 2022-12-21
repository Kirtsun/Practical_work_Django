from celery import shared_task

from django.core.mail import send_mail as mail_


@shared_task()
def send_mail(subject, text, to_email):
    mail_(subject, text, 'company_mail@gmail.com', [to_email], fail_silently=False)
