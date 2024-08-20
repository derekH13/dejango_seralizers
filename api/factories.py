import factory

from api.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    description = factory.Faker("pystr")
    price = factory.Faker("pyint")

    class Meta:
        model = Product