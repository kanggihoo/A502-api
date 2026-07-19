# 08-Get columns [GET]

`GET /rest/api/3/filter/{id}/columns`

Returns the columns configured for a filter. The column configuration is used when the filter's results are viewed in *List View* with the *Columns* set to *Filter*.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None, however, column details are only returned for:

 *  filters owned by the user.
 *  filters shared with a group that the user is a member of.
 *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.
 *  filters shared with a public project.
 *  filters shared with the public.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the filter. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"label\":\"Key\",\"value\":\"issuekey\"},{\"label\":\"Summary\",\"value\":\"summary\"}]"
```

#### 400 - Returned if the user does not have permission to view the filter.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if a column configuration is not set for the filter.

