import factory
from faker import Faker

from .models import Material

faker = Faker()


class FakeMaterial(factory.django.DjangoModelFactory):
    name = faker.word()
    density = faker.random_number(digits=4)

    class Meta:
        model = Material
