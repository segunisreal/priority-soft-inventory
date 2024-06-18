from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import *


class SupplierListCreateView(generics.ListCreateAPIView):
    queryset = Supplier.objects.filter(active=True)
    serializer_class = SupplierSerializer


class ItemSuppliersListCreateView(generics.ListCreateAPIView):
    queryset = Supplier.objects.filter(active=True)
    serializer_class = SupplierSerializer

    def get_queryset(self):
        item_id = self.kwargs.get('pk')
        item = get_object_or_404(InventoryItem, active=True, pk=item_id)
        return item.suppliers.filter(active=True)


class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.filter(active=True)
    serializer_class = SupplierSerializer


class SupplierItemsView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.filter(active=True)
    serializer_class = SupplierInventoryItemSerializerOut

    def get_queryset(self):
        supplier_id = self.kwargs.get('pk')
        supplier = get_object_or_404(Supplier, pk=supplier_id, active=True)
        return supplier.items.filter(active=True)


class InventoryItemListCreateView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.filter(active=True)
    serializer_class = InventoryItemSerializer


class InventoryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.filter(active=True)
    serializer_class = InventoryItemSerializer
