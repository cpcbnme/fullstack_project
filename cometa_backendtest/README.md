# Backend powered by Django

Beers and cheers. A simple backend practice using orders and stock with some drinks. It has a simple API to manage orders and stock about beers.

## Setup

1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. Run the migrations
5. Run the server

```bash
git clone
cd cometa_backendtest
python3 -m venv venv
pip install -r requirements.txt
make migrate
make runserver
```

## API

You can access the API by accessing to the following endpoints. The API has two main endpoints:

1. Orders: `/orders/`
2. Stock: `/stock/`

### Orders

#### GET `/orders/`

#### POST `/orders/` with the following payload

```json
{
	"items": [
		{
			"name": "Heineken",
			"quantity": 2
		},
		{
			"name": "Club Colombia",
			"quantity": 1
		}
	]
}
```

### Stock

By default, the stock has seeded with some beers. You can access the stock by the following endpoint.

> > Note: To see the stock, you need to run `make fillstock`.

#### GET `/stock/`
