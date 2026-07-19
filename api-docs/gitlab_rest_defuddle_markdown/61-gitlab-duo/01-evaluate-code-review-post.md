# 01-Evaluate code review [POST]

`POST /api/v4/duo_code_review/evaluations`

Evaluates code changes using GitLab Duo code review

### Request Body (application/json)

```json
{
  "diffs": string (required), // Raw diffs to review
  "mr_title": string (required), // Title of the merge request
  "mr_description": string (required), // Description of the merge request
  "files_content": {} (required), // Full file contents, where keys are file paths and values are the file contents
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

