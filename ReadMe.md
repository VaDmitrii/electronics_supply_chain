# Electronics supply chain

### Users can create their products and supply chains.

## How to run the app

Create virtual environment:
```
python3 -m venv venv
```
```
venv/Scripts/activate (Windows)
source venv/bin/activate (MacOS)
```
### Install requirements:
```
pip install -r requirements.txt
```
### Preparing django project:

* Run docker desktop on you PC

* Run in terminal: ```docker-compose up -d```

* Create tables in DB: ```python3 manage.py migrate```

## API's documentation

* 'api/schema/swagger-ui/' - API documentaion

## Endpoints use order (Postman)

* 'api/core/signup/' - create new User in PostgreSQL database by providing 'username', 'password'(JSON)
* 'api/token/' - retrieve JWT 'access' and 'refresh' tokens by providing 'username' and 'password' of user created on previous step
* Now you can send CRUD requests to all endpoints of API. More information you can see in API's documentation on 'api/schema/swagger-ui/' endpoint 
