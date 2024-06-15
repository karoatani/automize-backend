# OverView

This is the backend which Automize uses to manage all backend related tasks. Languages, libraries and Framework  used at the backend are:
- Python
- Django
- Django Rest Framework
- Rest Framework Simplejwt
- Postgresql


## Getting started
To get started making request to the backend, you need to make sure python3 is installed, if you do not have python3 installed on your system, download and install python3 [here](https://www.python.org/downloads/)


## Setting up environment

To get the backend server up and running, th first step is to clone the automize repo

```
git clone https://github.com/Ayothegod/automize-backend.git
```

### Navigate to the backend directory
```
cd backend
```

### Install pipenv

```
pip install pipenv
```

### Install necessary dependencies
```
pipenv install -r requirements.txt
pipenv shell
```

### Run Database Migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```


### Create an admin superuser
```
python manage.py createsuperuser
```


### Run the backend Server
```
python manage.py runserver
```
Yaaaay You've made it, The backend server should now be running on http://127.0.0.1:8000/


## Endpoints

### LOGIN
#### HTTP Methods : [POST]

#### Sample Request
**Body**:  
- **username** : The username of the user
- **password** : The password of the user

```javascript
const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

const raw = JSON.stringify({
  "username": "admin",
  "password": "password"
});

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("http://127.0.0.1:8000/api/v1/accounts/login/", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
```

#### Sample Response
**Body**:  
- **refresh** : A short lived token used to obtain another access token
- **access** : Token used to authenticate the user   

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTcyMjE0MywiaWF0IjoxNzE3OTk0MTQzLCJqdGkiOiJmNzBmNTY5ODhjNmE0ZTBlYjdjNDYwMzhhODRlMjgzMCIsInVzZXJfaWQiOjJ9.rhbAsueu1xswtBdDqR6flHhneHllDr9_CE0ybXXRUeU",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MDI0MTQzLCJpYXQiOjE3MTc5OTQxNDMsImp0aSI6ImZiYTA4ZWI3OWFhNjQxZTU4ODViZDQwZjlkZmVlMjQ5IiwidXNlcl9pZCI6Mn0.gOyWAN0aog4LhHV7DfzpbwNGU0efxVoARIfrPXCQjUc"
}
```
**Status_code** : 200 OK

### REGISTER
#### HTTP Methods : [POST]

#### Sample Request
**Body**:  
- **first_name** : The first name of the user
- **last_name** : The last name of the user
- **username** : The username of the user
- **email** : The email of the user
- **password** : The password of the user

```javascript
const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

const raw = JSON.stringify({
  "first_name": "Ayo",
  "last_name": "King",
  "username": "Ayo.god2sdq2352433",
  "email": "test2129q4s5d23@gmail.com",
  "password": "Ayo1234@admin"
});

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("http://127.0.0.1:8000/api/v1/accounts/register/", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));

```

#### Sample Response
**Body**:  
- **first_name** : The first name of the user
- **last_name** : The last name of the user
- **username** : The username of the user
- **email** : The email of the user
- **password** : The hashed version of the user password   

```json
{
    "first_name": "Ayo",
    "last_name": "King",
    "username": "Ayo.god22",
    "email": "test12@gmail.com",
    "password": "pbkdf2_sha256$720000$mh9xG3GGfeDsX2u9eS7S5E$HxBVrnnwRz1wMnNgVzqmdR1C8FIfIIXFg/oPpngRPZU="
}
```
**Status_code** : 201 Created

### REFRESH
#### HTTP Methods : [POST]

#### Sample Request
**Body**:  
- **refresh** : A short lived token used to obtain another access token

```javascript
const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

const raw = JSON.stringify({
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTc4ODQyNCwiaWF0IjoxNzE4MDYwNDI0LCJqdGkiOiIzYWI5YWNjZjJkNjU0NWJhOTdiZTUzOGQ4YzMzZDk5NyIsInVzZXJfaWQiOjJ9.4Bq3SjFP-QEZ4K_94NXsGn11hpLoCaHEDBejNLIzd7Q"
});

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("http://127.0.0.1:8000/api/v1/accounts/login/token/refresh/", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
```

#### Sample Response
**Body**:  
- **access** : Token used to authenticate the user   

```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MDkwNDQ0LCJpYXQiOjE3MTgwNjA0MjQsImp0aSI6IjI2NWMzZGI5MWUyOTQ3ODg4M2UwODYxNzVmZDFmOTJjIiwidXNlcl9pZCI6Mn0.SfQmyPdf_kDI1A3bzCzbm8YG_GpO-4tZXFZ59dvUSIs"
}
```
**Status_code** : 200 OK


### ADD DEBT
#### HTTP Methods : [POST]

#### Sample Request
**Body**:
- **person**:
    -  **first_name**: The debtor or creditor first name
    -   **last_name**: The debtor or creditor last name
    -   **phone_number**: The debtor or creditor phone number
    
- **type**: Specifies whether the debt is a debit or credit
- **amount**: The Amount owed
- **currency**: The currency which the debt will be paid in 
- **due_date**: The duraion of the debt
- **interest_rate**: The interest rate (optional)
 - **payment_frequency**: How often the debt will be paid 
- **payment_method**: The method of payment  

```javascript
const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4NDcwMzMxLCJpYXQiOjE3MTg0NDAzMzEsImp0aSI6IjZjYjcxY2JlM2IyZDQ3OTY4M2E5NmJhODQ5OGMwNzk4IiwidXNlcl9pZCI6MX0.WxaiuUB2AfNapGealoxeLtUGqIdiKThRQhq7wKD-PjQ");

const raw = JSON.stringify({
  "person": {
    "first_name": "Favour",
    "last_name": "Jones",
    "phone_number": "+2349015867277"
  },
  "type": "CR",
  "amount": 100,
  "currency": "100",
  "due_date": "2024-06-15T08:24:59Z",
  "interest_rate": 10,
  "payment_frequency": "MONTHLY",
  "payment_method": "BANK TRANSFER"
});

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("http://127.0.0.1:8000/api/v1/accounts/add-debt/", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
```

#### Sample Response
**Body**: 
```json
{
    "id": 7,
    "user_id": 1,
    "type": "CR",
    "person_id": 7,
    "amount": 100.0,
    "currency": "100",
    "due_date": "2024-06-15T08:24:59Z",
    "interest_rate": 10.0,
    "date_created": "2024-06-15T08:50:00.232947Z",
    "last_updated": "2024-06-15T08:50:00.232947Z",
    "payment_frequency": "MONTHLY",
    "payment_method": "BANK TRANSFER",
    "is_paid": false,
    "is_bad_debt": false
}
```
**Status_code** : 201 CREATED





### LIST ALL DEBT
#### HTTP Methods : [GET]

#### Sample Request

```javascript
const myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4NDcwMzMxLCJpYXQiOjE3MTg0NDAzMzEsImp0aSI6IjZjYjcxY2JlM2IyZDQ3OTY4M2E5NmJhODQ5OGMwNzk4IiwidXNlcl9pZCI6MX0.WxaiuUB2AfNapGealoxeLtUGqIdiKThRQhq7wKD-PjQ");

const raw = "";

const requestOptions = {
  method: "GET",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("http://127.0.0.1:8000/api/v1/accounts/list-debts/", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
```

#### Sample Response
**Body**: 
```json
[
    {
        "id": 1,
        "user": {
            "id": 1,
            "first_name": "",
            "last_name": "",
            "username": "admin",
            "email": "oyinbunuaatani@gmail.com"
        },
        "person": {
            "first_name": "Atani",
            "last_name": "Jones",
            "phone_number": "+2349015867277"
        },
        "type": "DR",
        "amount": 100.0,
        "currency": "NGN",
        "due_date": "2024-06-15T08:24:59Z",
        "interest_rate": 10.0,
        "payment_frequency": "MONTHLY",
        "payment_method": "BANK TRANSFER"
    },
    {
        "id": 2,
        "user": {
            "id": 1,
            "first_name": "",
            "last_name": "",
            "username": "admin",
            "email": "oyinbunuaatani@gmail.com"
        },
        "person": {
            "first_name": "Atani",
            "last_name": "Jones",
            "phone_number": "+2349015867277"
        },
        "type": "DR",
        "amount": 100.0,
        "currency": "NGN",
        "due_date": "2024-06-15T08:24:59Z",
        "interest_rate": 10.0,
        "payment_frequency": "MONTHLY",
        "payment_method": "BANK TRANSFER"
    },
    {
        "id": 8,
        "user": {
            "id": 1,
            "first_name": "",
            "last_name": "",
            "username": "admin",
            "email": "oyinbunuaatani@gmail.com"
        },
        "person": {
            "first_name": "Favour",
            "last_name": "Jones",
            "phone_number": "+2349015867277"
        },
        "type": "CR",
        "amount": 100.0,
        "currency": "NGN",
        "due_date": "2024-06-15T08:24:59Z",
        "interest_rate": 10.0,
        "payment_frequency": "MONTHLY",
        "payment_method": "BANK TRANSFER"
    }
]
```
**Status_code** : 200 OK

### UPDATE DEBT
#### HTTP Methods : [PUT]

#### Sample Request
**Body**:
- **person**:
    -  **first_name**: The debtor or creditor first name
    -   **last_name**: The debtor or creditor last name
    -   **phone_number**: The debtor or creditor phone number
    
- **type**: Specifies whether the debt is a debit or credit
- **amount**: The Amount owed
- **currency**: The currency which the debt will be paid in 
- **due_date**: The duraion of the debt
- **interest_rate**: The interest rate (optional)
- **payment_frequency**: How often the debt will be paid 
- **payment_method**: The method of payment  
- **is_paid** : Boolean field to denote a paid debt
- **is_bad_debt** : Boolean field to mark a debt as bad debt

```javascript
const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4NDcwMzMxLCJpYXQiOjE3MTg0NDAzMzEsImp0aSI6IjZjYjcxY2JlM2IyZDQ3OTY4M2E5NmJhODQ5OGMwNzk4IiwidXNlcl9pZCI6MX0.WxaiuUB2AfNapGealoxeLtUGqIdiKThRQhq7wKD-PjQ");

const raw = JSON.stringify({
  "person": {
    "first_name": "Atani",
    "last_name": "Jones",
    "phone_number": "+2349015867277"
  },
  "type": "DR",
  "amount": 100,
  "currency": "50",
  "due_date": "2024-06-15T08:24:59Z",
  "interest_rate": 10,
  "payment_frequency": "MONTHLY",
  "payment_method": "BANK TRANSFER",
  "is_paid": true,
  "is_bad_debt": true
});

const requestOptions = {
  method: "PUT",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("http://127.0.0.1:8000/api/v1/accounts/update-debt/2/", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
```

#### Sample Response
**Body**: 
```json
{
    "id": 7,
    "user_id": 1,
    "type": "CR",
    "person_id": 7,
    "amount": 100.0,
    "currency": "100",
    "due_date": "2024-06-15T08:24:59Z",
    "interest_rate": 10.0,
    "date_created": "2024-06-15T08:50:00.232947Z",
    "last_updated": "2024-06-15T08:50:00.232947Z",
    "payment_frequency": "MONTHLY",
    "payment_method": "BANK TRANSFER",
    "is_paid": false,
    "is_bad_debt": false
}
```
**Status_code** : 200 OK

### DEBT DETAILS
#### HTTP Methods : [GET]

#### Sample Request

```javascript
const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4NDcwMzMxLCJpYXQiOjE3MTg0NDAzMzEsImp0aSI6IjZjYjcxY2JlM2IyZDQ3OTY4M2E5NmJhODQ5OGMwNzk4IiwidXNlcl9pZCI6MX0.WxaiuUB2AfNapGealoxeLtUGqIdiKThRQhq7wKD-PjQ");

const raw = JSON.stringify({
  "person": {
    "first_name": "Atani",
    "last_name": "Jones",
    "phone_number": "+2349015867277"
  },
  "type": "DR",
  "amount": 100,
  "currency": "50",
  "due_date": "2024-06-15T08:24:59Z",
  "interest_rate": 10,
  "payment_frequency": "MONTHLY",
  "payment_method": "BANK TRANSFER",
  "is_paid": true,
  "is_bad_debt": true
});

const requestOptions = {
  method: "GET",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("http://127.0.0.1:8000/api/v1/accounts/debt-details/1/", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
```
#### Sample Response
**Body**: 
```json
{
    "id": 1,
    "user": {
        "id": 1,
        "first_name": "",
        "last_name": "",
        "username": "admin",
        "email": "oyinbunuaatani@gmail.com"
    },
    "person": {
        "first_name": "Atani",
        "last_name": "Jones",
        "phone_number": "+2349015867277"
    },
    "type": "DR",
    "amount": 100.0,
    "currency": "50",
    "due_date": "2024-06-15T08:24:59Z",
    "interest_rate": 10.0,
    "payment_frequency": "MONTHLY",
    "payment_method": "BANK TRANSFER"
}
```
**Status_code** : 200 OK


### DELETE DEBT
#### HTTP Methods : [PUT]

#### Sample Request
**Body**:
- **is_deleted** : Used to delete a particular debt
```javascript
const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Authorization", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4NDcwMzMxLCJpYXQiOjE3MTg0NDAzMzEsImp0aSI6IjZjYjcxY2JlM2IyZDQ3OTY4M2E5NmJhODQ5OGMwNzk4IiwidXNlcl9pZCI6MX0.WxaiuUB2AfNapGealoxeLtUGqIdiKThRQhq7wKD-PjQ");

const raw = JSON.stringify({
  "is_deleted": true
});

const requestOptions = {
  method: "PUT",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("http://127.0.0.1:8000/api/v1/accounts/delete-debt/1/", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
```

#### Sample Response
**Body**: 
```json
{
    "is_deleted": false
}
```
**Status_code** : 200 OK
