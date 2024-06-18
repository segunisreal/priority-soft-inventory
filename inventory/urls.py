from django.urls import path
from .views import *

urlpatterns = [
    path('suppliers/', SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('suppliers/<int:pk>/items', SupplierItemsView.as_view(), name='supplier-detail'),

    path('items/', InventoryItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', InventoryItemDetailView.as_view(), name='item-detail'),
    path('items/<int:pk>/suppliers', ItemSuppliersListCreateView.as_view(), name='item-suppliers'),
]
