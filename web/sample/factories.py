from django.contrib.auth.models import User
from factory import Faker, django

from sample.models import SampleModel


class SampleModelFactory(django.DjangoModelFactory):
    class Meta:  # pyrefly: ignore
        model = SampleModel

    name = Faker("name")
    description = Faker("text")


class UserFactory(django.DjangoModelFactory):
    class Meta:  # pyrefly: ignore
        model = User

    username = Faker("user_name")
    email = Faker("email")
    password = Faker("password")
