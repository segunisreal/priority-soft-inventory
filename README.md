# Store Management API

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`
5. To populate database with fake data for testing, run: `python manage.py populate_db`
6. To create a super admin account to access the admin panel, run: `python manage.py createsuperuser` and fill out the prompts.

## Swagger Doc Link
- {{base_url}}/doc/ <br><br>If you are running the app on port 8000 on localhost, then URL will be: http://localhost:8000/doc/

## API Endpoints

### Suppliers

- `GET /inventory/suppliers/` - List all suppliers
- `POST /inventory/suppliers/` - Create a new supplier
- `GET /inventory/suppliers/<id>/` - Retrieve a supplier
- `PUT /inventory/suppliers/<id>/` - Update a supplier
- `DELETE /inventory/suppliers/<id>/` - Delete a supplier
- `GET /inventory/suppliers/<id>/items` - Get all items of a supplier

### Inventory Items

- `GET /inventory/items/` - List all items
- `POST /inventory/items/` - Create a new item
- `GET /inventory/items/<id>/` - Retrieve an item
- `PUT /inventory/items/<id>/` - Update an item
- `DELETE /inventory/items/<id>/` - Delete an item
- `GET /inventory/items/<id>/suppliers` - Get all suppliers of an item
