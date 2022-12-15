import random
from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from dz_practical.models import Comments, Posts

from faker import Faker

import pytz


User = get_user_model()
fake = Faker()


class Command(BaseCommand):
    helps = "Create Post"

    def add_arguments(self, parser):
        parser.add_argument('some_id', nargs='?', type=int, choices=range(1, 501), help='Enter a number from 1 to 500')

    def handle(self, *args, **kwargs):
        objs_comm = []
        total = kwargs['some_id']
        q = [True, False]
        w = Posts.objects.values_list('id', flat=True)
        if w:
            for i in range(total):
                k_comm = Comments(
                    name=fake.company(),
                    text=fake.text(),
                    published_date=fake.date_time_between_dates(
                        datetime_start=datetime(2020, 1, 1), datetime_end=datetime(2022, 12, 31), tzinfo=pytz.UTC),
                    is_publish=random.choice(q),
                    post_id=random.choice(w),
                )
                objs_comm.append(k_comm)
            Comments.objects.bulk_create(objs_comm)
            self.stdout.write('Creation was successful!')
        else:
            self.stdout.write('First create post')
