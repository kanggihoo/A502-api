# 01-List all wiki pages for a group [GET]

`GET /api/v4/groups/{id}/wikis`

Lists all wiki pages for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `with_content` | `boolean` | `query` | No | Include pages' content |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "format": string,
  "slug": string,
  "title": string,
  "wiki_page_meta_id": integer,
}
```

#### 400 - Bad Request

#### 404 - Not found

