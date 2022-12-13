from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from faker import Faker


User = get_user_model()
fake = Faker()


class Command(BaseCommand):
    helps = "Create random user"

    def add_arguments(self, parser):
        parser.add_argument('some_id', nargs='?', type=int, choices=range(1, 501), help='Enter a number from 1 to 500')

    def handle(self, *args, **kwargs):
        objs_user = []
        total = kwargs['some_id']
        for i in range(total):
            k_user = User(
                username=fake.user_name(),
                email=fake.email(),
                password=make_password(fake.password())
            )
            objs_user.append(k_user)
        User.objects.bulk_create(objs_user)
        self.stdout.write('Creation was successful!')
