# multisearch

## Quickstart

Clone the project
```
git clone https://github.com/siderai/multisearch/
cd multisearch
```
Set environmentment variables in .env file. Example:
```
SECRET_KEY=django-insecure-p+4!a_yopj2cp)0hjo8vzu4$gc9ti%pkx2-4msg-*-n$@u3m4-
DEBUG=True
```
Run containers
```
docker-compose up -d --build
docker-compose exec app python3 manage.py migrate
docker-compose exec app python3 manage.py loaddata db.json
docker-compose exec app python3 manage.py runserver
```

For access to api playground open localhost/graphql
