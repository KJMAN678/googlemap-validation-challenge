from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from sample.models import SampleModel


class Command(BaseCommand):
    help = "Sample command"

    def add_arguments(self, parser):
        parser.add_argument("range_num", nargs=1, type=int)

    def handle(self, *args, **options):
        fake = Faker("ja_JP")

        if not options["range_num"]:
            raise CommandError("整数の引数を指定してください。")

        for range_num in options["range_num"]:
            for _ in range(range_num):
                SampleModel.objects.create(name=fake.name(), description=fake.text())

            self.stdout.write(
                self.style.SUCCESS(
                    f"{range_num} 件の SampleModel のデータを作成しました。"
                )
            )
