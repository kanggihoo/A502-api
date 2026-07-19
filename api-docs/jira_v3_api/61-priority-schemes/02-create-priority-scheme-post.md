# 02-Create priority scheme [POST]

`POST /rest/api/3/priorityscheme`

Creates a new priority scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "defaultPriorityId": integer (required), // The ID of the default priority for the priority scheme.
  "description": string, // The description of the priority scheme.
  "mappings": any, // Instructions to migrate the priorities of issues.  `in` mappings are used to migrate the priorities of issues to priorities used within the priority scheme.  `out` mappings are used to migrate the priorities of issues to priorities not used within the priority scheme.   *  When **priorities** are **added** to the new priority scheme, no mapping needs to be provided as the new priorities are not used by any issues.  *  When **priorities** are **removed** from the new priority scheme, no mapping needs to be provided as the removed priorities are not used by any issues.  *  When **projects** are **added** to the priority scheme, the priorities of issues in those projects might need to be migrated to new priorities used by the priority scheme. This can occur when the current scheme does not use all the priorities in the project(s)' priority scheme(s).           *  An `in` mapping must be provided for each of these priorities.  *  When **projects** are **removed** from the priority scheme, no mapping needs to be provided as the removed projects are not using the priorities of the new priority scheme.  For more information on `in` and `out` mappings, see the child properties documentation for the `PriorityMapping` object below.
  "name": string (required), // The name of the priority scheme. Must be unique.
  "priorityIds": [
    integer
  ] (required), // The IDs of priorities in the scheme.
  "projectIds": [
    integer
  ], // The IDs of projects that will use the priority scheme.
}
```
### Responses

#### 201 - Returned if the request is completed.

Example (application/json):
```json
"{\"id\":\"10001\"}"
```

#### 202 - Returned if the request is accepted.

Example (application/json):
```json
"{\"id\":\"10001\",\"task\":{\"self\":\"https://your-domain.atlassian.net/rest/api/3/task/1\",\"id\":\"1\",\"description\":\"Task description\",\"status\":\"COMPLETE\",\"result\":\"the task result, this may be any JSON\",\"submittedBy\":10000,\"progress\":100,\"elapsedRuntime\":156,\"submitted\":1501708132800,\"started\":1501708132900,\"finished\":1501708133000,\"lastUpdate\":1501708133000}}"
```

#### 400 - Returned if the request isn't valid.

**Mappings Validation Errors**

 *  ``The priorities with IDs [ID 1, ID 2, ...] require mapping. Please provide mappings in the 'in' mappings object, where these priorities are the keys with corresponding values.`` The listed priority ID(s) have not been provided as keys for ``in`` mappings but are required, add them to the mappings object.

#### 401 - Returned if the authentication credentials are incorrect.

#### 403 - Returned if the user doesn't have the necessary permissions.

#### 409 - Returned if an action with this priority scheme is still in progress.

