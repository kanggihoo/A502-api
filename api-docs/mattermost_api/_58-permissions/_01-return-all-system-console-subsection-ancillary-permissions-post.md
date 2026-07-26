# 01-Return all system console subsection ancillary permissions [POST]

`POST /api/v4/permissions/ancillary`

Returns all the ancillary permissions for the corresponding system console subsection permissions appended to the requested permission subsections. __Minimum server version__: 9.10


### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 200 - Successfully returned all ancillary and requested permissions

Schema (application/json):
```json
[
  string
]
```

#### 400 - 

