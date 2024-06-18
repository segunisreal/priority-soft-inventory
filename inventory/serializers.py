from rest_framework import serializers
from .models import Supplier, InventoryItem


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        exclude = ('active',)


class InventoryItemSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)
    suppliers_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = InventoryItem
        exclude = ('active',)


class SupplierInventoryItemSerializerOut(serializers.ModelSerializer):

    class Meta:
        model = InventoryItem
        exclude = ('active', 'suppliers')



