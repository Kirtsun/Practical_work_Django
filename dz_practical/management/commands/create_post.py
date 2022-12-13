import random
from datetime import datetime
import pytz
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from dz_practical.models import Posts
from faker import Faker


User = get_user_model()
fake = Faker()


class Command(BaseCommand):
    helps = "Create Post"

    def add_arguments(self, parser):
        parser.add_argument('some_id', nargs='?', type=int, choices=range(1, 501), help='Enter a number from 1 to 500')

    def handle(self, *args, **kwargs):
        objs_post = []
        total = kwargs['some_id']
        q = [True, False]
        w = User.objects.values_list('id', flat=True)
        if w:
            for i in range(total):
                k_post = Posts(
                    author_id=random.choice(w),
                    title=fake.company(),
                    text=fake.text(),
                    published_date=fake.date_time_between_dates(
                        datetime_start=datetime(2020, 1, 1), datetime_end=datetime(2022, 12, 31), tzinfo=pytz.UTC),
                    create_date=fake.date_time_between_dates(
                        datetime_start=datetime(2020, 1, 1), datetime_end=datetime(2022, 12, 31), tzinfo=pytz.UTC),
                    is_publish=random.choice(q)
                )
                objs_post.append(k_post)
            Posts.objects.bulk_create(objs_post)
            self.stdout.write('Creation was successful!')
        else:
            self.stdout.write('First create users')
