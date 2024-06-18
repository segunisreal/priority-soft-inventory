import base64

from django.test import TestCase
from django.contrib.auth.models import User
from faker import Faker
from rest_framework.test import APITestCase
from .models import *
from rest_framework import status


class PermissionTests(APITestCase):

    def setUp(self):
        self.staff_user = User.objects.create_user(username='staffuser', password='password', is_staff=True)
        self.regular_user = User.objects.create_user(username='regularuser', password='password', is_staff=False)
        self.supplier = Supplier.objects.create(name='Supplier 1', email='sup1@example.com', phone_number='+2348100000000')
        self.item = InventoryItem.objects.create(name='Item 1', description='Description 1', price='9.99')

    def auth_header(self, username, password):
        credentials = f"{username}:{password}"
        credentials_bytes = credentials.encode('utf-8')
        credentials_base64 = base64.b64encode(credentials_bytes).decode('utf-8')
        return f"Basic {credentials_base64}"

    def test_staff_user_can_create_supplier(self):
        url = '/inventory/suppliers/'
        data = {
          "name": "string",
          "email": "user@example.com",
          "phone_number": "string"
        }
        headers = {
            'Authorization': self.auth_header('staffuser', 'password')
        }
        response = self.client.post(url, data, headers=headers, format='json',)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED or status.HTTP_200_OK)

    def test_regular_user_cannot_create_supplier(self):
        url = '/inventory/suppliers/'
        data = {
            "name": "string",
            "email": "user@example.com",
            "phone_number": "string"
        }
        headers = {
            'Authorization': self.auth_header('regularuser', 'password')
        }
        response = self.client.post(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_staff_user_can_update_item(self):
        url = f'/inventory/items/{self.item.id}/'
        data = {'name': 'Updated Item', 'description': 'Updated Description', 'price': '19.99'}
        headers = {
            'Authorization': self.auth_header('staffuser', 'password')
        }
        response = self.client.put(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_regular_user_cannot_update_item(self):
        url = f'/inventory/items/{self.item.id}/'
        data = {'name': 'Updated Item', 'description': 'Updated Description', 'price': '19.99'}
        headers = {
            'Authorization': self.auth_header('regularuser', 'password')
        }
        response = self.client.put(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_staff_user_can_delete_supplier(self):
        url = f'/inventory/suppliers/{self.supplier.id}/'
        headers = {
            'Authorization': self.auth_header('staffuser', 'password')
        }
        response = self.client.delete(url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT or status.HTTP_200_OK)

    def test_regular_user_cannot_delete_supplier(self):
        url = f'/inventory/suppliers/{self.supplier.id}/'
        headers = {
            'Authorization': self.auth_header('regularuser', 'password')
        }
        response = self.client.delete(url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class SuppliersTests(APITestCase):

    def setUp(self):
        fake = Faker()

        # Create fake suppliers and inventory items
        for _ in range(10):
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
            suppliers = Supplier.objects.all().order_by('?')[:3]
            item.suppliers.add(*suppliers)
            item.save()

    def test_get_all_suppliers(self):
        url = f'/inventory/suppliers/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('count', response.json())

    def test_get_single_supplier(self):
        url = f'/inventory/suppliers/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_supplier_items(self):
        url = f'/inventory/suppliers/1/items'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('count', response.json())


class ItemsTests(APITestCase):

    def setUp(self):
        fake = Faker()

        # Create fake suppliers and inventory items
        for _ in range(10):
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
            suppliers = Supplier.objects.all().order_by('?')[:3]
            item.suppliers.add(*suppliers)
            item.save()

    def test_get_all_items(self):
        url = f'/inventory/items/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('count', response.json())

    def test_get_single_supplier(self):
        url = f'/inventory/items/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_supplier_items(self):
        url = f'/inventory/items/1/suppliers'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('count', response.json())


