# SocialNetworkAPI

Simple API where master can get requests from people wanting to repair their phones, when the master starts repairing, the cutomer can't change their request. 

When the work is done master sends an invoice with the price, as soon as the customer pays it, master can't change the invoice anymore.

```
api/v1/docs - swagger
api/v1/register - for registration
api/v1/login - for login
api/v1/request - for creating request
api/v1/requests - for checking the lit of requests
api/v1/requests/{id} - for updating requests
api/v1/invoice - for creating invoice
api/v1/invoices - for checking the lit of invoices
api/v1/invoices/{id} - for updating invoices
```

### To run on your PC you need to clone the repository

```
git clone https://github.com/KhirilovA/PhoneRepairAPI.git
```

Install requirements

```
poetry install --no-dev
```

Configure your .env and .env.docker files as it is shown in 

```
.env.example
.env.docker.example
```

Run migrations

```
python manage.py migrate
```


And run the server or start the container

```
python manage.py runserver
docker-compose up
```
