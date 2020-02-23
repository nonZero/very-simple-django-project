from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from demoapp.models import Post


class Command(BaseCommand):
    help = "Create some silly posts"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, *args, **options):
        foo = Faker()
        for i in range(n):
            Post.objects.create(
                title=foo.text(55).title(),
                published_at=foo.date_time_this_decade(tzinfo=timezone.get_default_timezone()),
                content=foo.text(2500),
            )
