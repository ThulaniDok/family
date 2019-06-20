# Device Registry Service

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all family members

**Definition**

`GET /family`

**Response**

- `200 OK` on success

```json
[
    {

    "name": "Sandi",
    "gender": "female",
    "age": "27",
    "occupation": "consultant"
    },
    {

    "name": "Dok",
    "gender": "male",
    "age": "30",
    "occupation": "programmer"
    }
]
```

### Registering a new member

**Definition**

`POST /family`

**Arguments**

- `"name":string` name of the member
- `"gender":string` gender of the member
- `"age":string` age of the member
- `"occupation":string` work, study or doing nothing

If a member with the given name already exists, the existing device will be overwritten.

**Response**

- `201 Created` on success

```json
{

    "name": "Sandi",
    "gender": "female",
    "age": "27",
    "occupation": "consultant"
}
```

## Lookup device details

`GET /family/<name>`

**Response**

- `404 Not Found` if the device does not exist
- `200 OK` on success

```json
{

    "name": "Sandi",
    "gender": "female",
    "age": "27",
    "occupation": "consultant"
}
```

## Delete a member

**Definition**

`DELETE /family/<name>`

**Response**

- `404 Not Found` if the member does not exist
- `204 No Content` on success