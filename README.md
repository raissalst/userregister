# User Register Application using Flask and JSON

#### The main goal of this task is to practice the use of Flask framework and to write/load data using JSON file type to storage data.

.

### Endpoints:

- /user -> list all users (GET)
- /user/:id -> filter user (GET)
- /user -> register new user (POST)
- /user/:id -> update user's data (PATCH)
- /user/:id -> delete user (DELETE)

### Request body and expected answers:

<h3 align="center">***Get list of users***</h3>

`GET /user`

No request body needed.

In case everything works well, the answer shall be like:

`STATUS 200`

```json
{
  "data": [
    {
      "email": "name@mail.com",
      "id": 1,
      "name": "Name"
    },
    {
      "email": "name@mail.com",
      "id": 2,
      "name": "Name"
    }
  ]
}
```

_Possible errors:_

_1.- User not found (STATUS 404)_

<h3 align="center">***Filter user by id***</h3>

`GET /user/:id`

No request body needed.

In case everything works well, the answer shall be like:

`STATUS 200`

```json
{
    "email": "name@mail.com",
     "id": 1,
     "name": "Name"
},
```

_Possible errors:_

_1.- User not found (STATUS 404)_

<h3 align="center">***Register new user***</h3>

`POST /user`

```json
{
  "name": "Name",
  "email": "name@mail.com"
}
```

In case everything works well, the answer shall be like:

`STATUS 201`

```json
{
  "email": "name@mail.com",
  "id": 1,
  "name": "Name"
}
```

_Possible errors:_

_1.- E-mail or name not of string type (STATUS 400)_

_2.- E-mail already registered (STATUS 409)_

_3.- Wrong keys error (STATUS 400)_

<h3 align="center">***Update user's data***</h3>

It is allowed to change name and/or e-mail data from user.

`PATCH /user/:id`

```json
{
  "name": "New Name",
  "email": "newmail@mail.com"
}
```

or only name/email alone.

In case everything works well, the answer shall be like:

`STATUS 200`

```json
{
  "email": "newmail@mail.com",
  "id": 1,
  "name": "New Name"
}
```

_Possible errors:_

_1.- E-mail or name not of string type (STATUS 400)_

_2.- E-mail already registered (STATUS 409)_

_3.- Wrong keys error (STATUS 400)_

_4.- User not found (STATUS 404)_

<h3 align="center">***Delete user***</h3>

The user data can be deleted.

`DELETE /user/:id`

No request body needed.

In case everything works well, the answer shall be like:

`STATUS 200`

```json
{
  "email": "mail@mail.com",
  "id": 1,
  "name": "Name"
}
```

_Possible errors:_

_1.- User not found (STATUS 404)_
