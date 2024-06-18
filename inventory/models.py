from backend.global_model import *


class Supplier(GeneralFieldModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    phone_number = models.CharField(null=True, max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)


class InventoryItem(GeneralFieldModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    suppliers = models.ManyToManyField(Supplier, related_name='items')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)

    @property
    def get_suppliers(self):
        return self.suppliers.filter(active=True)

    @property
    def suppliers_count(self):
        return self.get_suppliers.count()
