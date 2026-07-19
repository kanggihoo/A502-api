# 03-Get current variant assignment for an experiment context [GET]

`GET /api/v4/experiments/{experiment_name}/assignments`

Returns the currently cached variant assignment for the given experiment and context. Defaults to current user if no context is provided.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `experiment_name` | `string` | `path` | Yes |  |
| `context` | `object` | `query` | No | Context parameters (user, namespace, project). Pass every key the experiment declares in `context_keys`; experiments can declare multiple keys. An actor context is resolved from the user. The user defaults to the current user. |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "experiment": string,
  "variant": string,
  "context_key": string,
  "cached": boolean,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

