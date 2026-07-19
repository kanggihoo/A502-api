# 13-Update AI False Positive Detection results [POST]

`POST /api/v4/vulnerabilities/{vulnerability_id}/flags/ai_detection`

Updates the confidence score and explanation for AI-based False Positive Detection flows.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `vulnerability_id` | `string` | `path` | Yes | The ID of a vulnerability |

### Request Body (application/json)

```json
{
  "confidence_score": integer (required), // Confidence score from 0-100
  "description": string (required), // Explanation for the detection result
  "origin": string, // Origin of the AI detection
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

