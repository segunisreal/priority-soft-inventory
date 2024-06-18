from django.core.management.base import BaseCommand
from inventory.models import *
from faker import Faker


class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create fake suppliers and inventory items
        for _ in range(15):
            Supplier.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
            )

        # Create fake items
        for _ in range(10):
            price = str(fake.pricetag()).replace('$', '').replace(',', '')
            InventoryItem.objects.create(
                name=fake.word(),
                description=fake.text(),
                price=price,
            )

        # Add suppliers to items
        for item in InventoryItem.objects.all():
            suppliers = Supplier.objects.all().order_by('?')[:5]
            item.suppliers.add(*suppliers)
            item.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database test data'))
