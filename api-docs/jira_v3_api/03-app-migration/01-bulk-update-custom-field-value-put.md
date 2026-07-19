# 01-Bulk update custom field value [PUT]

`PUT /rest/atlassian-connect/1/migration/field`

Updates the value of a custom field added by Connect apps on one or more issues.
The values of up to 200 custom fields can be updated.

**[Permissions](#permissions) required:** Only Connect apps can make this request

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `Atlassian-Transfer-Id` | `string` | `header` | Yes | The ID of the transfer. |

### Request Body (application/json)

```json
{
  "updateValueList": [
    {
      "_type": enum("StringIssueField" | "NumberIssueField" | "RichTextIssueField" | "SingleSelectIssueField" | "MultiSelectIssueField" | "TextIssueField") (required), // The type of custom field.
      "fieldID": integer (required), // The custom field ID.
      "issueID": integer (required), // The issue ID.
      "number": number, // The value of number type custom field when `_type` is `NumberIssueField`.
      "optionID": string, // The value of single select and multiselect custom field type when `_type` is `SingleSelectIssueField` or `MultiSelectIssueField`.
      "richText": string, // The value of richText type custom field when `_type` is `RichTextIssueField`.
      "string": string, // The value of string type custom field when `_type` is `StringIssueField`.
      "text": string, // The value of of text custom field type when `_type` is `TextIssueField`.
    }
  ], // The list of custom field update details.
}
```
### Responses

#### 200 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

#### 403 - Returned if:
* the transfer ID is not found.
* the authorisation credentials are incorrect or missing.

