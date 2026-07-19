# 03-Fetch the Duo Code Review custom instructions for a merge request [GET]

`GET /api/v4/ai/duo_workflows/code_review/custom_instructions`

Fetch all Duo Code Review custom instructions for a merge request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `project_id` | `string` | `query` | Yes | The ID or path of the project |
| `merge_request_iid` | `integer` | `query` | Yes | The IID of the merge request |

### Responses

#### 200 - OK

#### 400 - Validation failed

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

