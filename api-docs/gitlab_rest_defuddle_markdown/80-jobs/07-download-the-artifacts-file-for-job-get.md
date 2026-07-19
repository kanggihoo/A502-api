# 07-Download the artifacts file for job [GET]

`GET /api/v4/jobs/{id}/artifacts`

Download the artifacts file for job

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | Job's ID |
| `token` | `string` | `query` | No | Job's authentication token |
| `direct_download` | `boolean` | `query` | No | Perform direct download from remote storage instead of proxying artifacts |

### Responses

#### 200 - Download allowed

#### 302 - Found

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Artifact not found

#### 429 - Too Many Requests

