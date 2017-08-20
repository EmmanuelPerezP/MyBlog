from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("ema", "emmanuelperezp@gmail.com",
                                          os.environ.get('DJANGO_USER_PASSWORD', "123"))
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
