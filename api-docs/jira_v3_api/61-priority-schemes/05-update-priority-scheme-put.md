# 05-Update priority scheme [PUT]

`PUT /rest/api/3/priorityscheme/{schemeId}`

Updates a priority scheme. This includes its details, the lists of priorities and projects in it

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `schemeId` | `integer` | `path` | Yes | The ID of the priority scheme. |

### Request Body (application/json)

```json
{
  "defaultPriorityId": integer, // The default priority of the scheme.
  "description": string, // The description of the priority scheme.
  "mappings": any, // Instructions to migrate the priorities of issues.  `in` mappings are used to migrate the priorities of issues to priorities used within the priority scheme.  `out` mappings are used to migrate the priorities of issues to priorities not used within the priority scheme.   *  When **priorities** are **added** to the priority scheme, no mapping needs to be provided as the new priorities are not used by any issues.  *  When **priorities** are **removed** from the priority scheme, issues that are using those priorities must be migrated to new priorities used by the priority scheme.           *  An `in` mapping must be provided for each of these priorities.  *  When **projects** are **added** to the priority scheme, the priorities of issues in those projects might need to be migrated to new priorities used by the priority scheme. This can occur when the current scheme does not use all the priorities in the project(s)' priority scheme(s).           *  An `in` mapping must be provided for each of these priorities.  *  When **projects** are **removed** from the priority scheme, the priorities of issues in those projects might need to be migrated to new priorities within the **Default Priority Scheme** that are not used by the priority scheme. This can occur when the **Default Priority Scheme** does not use all the priorities within the current scheme.           *  An `out` mapping must be provided for each of these priorities.  For more information on `in` and `out` mappings, see the child properties documentation for the `PriorityMapping` object below.
  "name": string, // The name of the priority scheme. Must be unique.
  "priorities": any, // The priorities in the scheme.
  "projects": any, // The projects in the scheme.
}
```
### Responses

#### 202 - Returned if the request is accepted.

Example (application/json):
```json
"{\"task\":{\"self\":\"https://your-domain.atlassian.net/rest/api/3/task/1\",\"id\":\"1\",\"description\":\"Task description\",\"status\":\"COMPLETE\",\"result\":\"the task result, this may be any JSON\",\"submittedBy\":10000,\"progress\":100,\"elapsedRuntime\":156,\"submitted\":1501708132800,\"started\":1501708132900,\"finished\":1501708133000,\"lastUpdate\":1501708133000},\"updated\":{\"description\":\"This is the default scheme used by all new and unassigned projects\",\"id\":\"1\",\"isDefault\":true,\"name\":\"Default Priority Scheme\",\"priorities\":{\"isLast\":true,\"maxResults\":50,\"startAt\":0,\"total\":3,\"values\":[{\"description\":\"Serious problem that could block progress.\",\"iconUrl\":\"/images/icons/priorities/high.svg\",\"id\":\"1\",\"isDefault\":false,\"name\":\"High\",\"statusColor\":\"#f15C75\"},{\"description\":\"Has the potential to affect progress.\",\"iconUrl\":\"/images/icons/priorities/medium.svg\",\"id\":\"2\",\"isDefault\":true,\"name\":\"Medium\",\"statusColor\":\"#f79232\"},{\"description\":\"Minor problem or easily worked around.\",\"iconUrl\":\"/images/icons/priorities/low.svg\",\"id\":\"3\",\"isDefault\":false,\"name\":\"Low\",\"statusColor\":\"#707070\"}]},\"projects\":{\"isLast\":true,\"maxResults\":50,\"startAt\":0,\"total\":1,\"values\":[{\"avatarUrls\":{\"16x16\":\"secure/projectavatar?size=xsmall&pid=10000\",\"24x24\":\"secure/projectavatar?size=small&pid=10000\",\"32x32\":\"secure/projectavatar?size=medium&pid=10000\",\"48x48\":\"secure/projectavatar?size=large&pid=10000\"},\"id\":\"10000\",\"key\":\"EX\",\"name\":\"Example\",\"projectCategory\":{\"description\":\"Project category description\",\"id\":\"10000\",\"name\":\"A project category\"},\"projectTypeKey\":\"ProjectTypeKey{key='software'}\",\"self\":\"project/EX\",\"simplified\":false}]}}}"
```

#### 400 - Returned if the request isn't valid.

**Mappings Validation Errors**

 *  ``The changes to priority schemes require mapping of priorities. Please provide a value for the 'in' mappings object.`` Priorities are being removed and/or projects are being added to the scheme, but ``in`` mappings are not provided.
 *  ``The changes to priority schemes require mapping of priorities. Please provide a value for the 'out' mappings object.`` Projects are being removed from the scheme, but ``out`` mappings are not provided.
 *  ``The priorities with IDs [ID 1, ID 2, ...] provided as keys for the 'in' mappings object do not exist. Please provide existing priority IDs.`` The listed priority ID(s) have been provided as keys for ``in`` mappings but do not exist. Please confirm the correct priority ID(s) have been provided, they should be priorities that exist on the Jira site which are used by projects being added to the current scheme, but are not in use by the current scheme.
 *  ``The priorities with IDs [ID 1, ID 2, ...] provided as values for the 'in' mappings object do not exist. Please provide existing priority IDs used by the current priority scheme.`` The listed priority ID(s) have been provided as values for ``in`` mappings but do not exist. Please confirm the correct priority ID(s) have been provided, they should be priorities that exist on the Jira site and are in use by the current scheme.
 *  ``The priorities with IDs [ID 1, ID 2, ...] provided as keys for the 'out' mappings object do not exist. Please provide existing priority IDs used by the current priority scheme.`` The listed priority ID(s) have been provided as keys for ``out`` mappings but are invalid. Please confirm the correct priority ID(s) have been provided, they should be priorities that exist on the Jira site and are in use by the current scheme.
 *  ``The priorities with IDs [ID 1, ID 2, ...] provided as values for the 'out' mappings object do not exist. Please provide existing priority IDs used by the default scheme.`` The listed priority ID(s) have been provided as values for ``out`` mappings but are invalid. Please confirm the correct priority ID(s) have been provided, they should be priorities that exist on the Jira site and are in use by the Default Priority Scheme, but are not in use by the current scheme.
 *  ``The priorities with IDs [ID 1, ID 2, ...] do not require mapping. Please remove these keys and their corresponding values from the 'in' mappings object.`` The listed priority ID(s) have been provided as keys for ``in`` mappings but are not required, they can be removed from the mappings object.
 *  ``The priorities with IDs [ID 1, ID 2, ...] require mapping. Please provide mappings in the 'in' mappings object, where these priorities are the keys with corresponding values.`` The listed priority ID(s) have not been provided as keys for ``in`` mappings but are required, add them to the mappings object.
 *  ``The priorities with IDs [ID 1, ID 2, ...] being mapped to are not in the current scheme. Please remove these values and their corresponding keys from the 'in' mappings object.`` The listed priority ID(s) have been provided as keys for ``in`` mappings but are not in use by the current scheme, they can be removed from the mappings object.
 *  ``The priorities with IDs [ID 1, ID 2, ...] do not require mapping. Please remove these keys and their corresponding values from the 'out' mappings object.`` The listed priority ID(s) hve been provided as keys for ``out`` mappings but are not required, they can be removed from the mappings object.
 *  ``The priorities with IDs [ID 1, ID 2, ...] require mapping. Please provide mappings in the 'out' mappings object, where these priorities are the keys with corresponding values.`` The listed priority ID(s) have not been provided as keys for ``out`` mappings but are required, add them to the mappings object.
 *  ``The priorities with IDs [ID 1, ID 2, ...] being mapped to are not in the default scheme. Please remove these values and their corresponding keys from the 'out' mappings object.`` The listed priority ID(s) have been provided as keys for ``out`` mappings but are not in use by the Default Priority Scheme, they can be removed from the mappings object.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user doesn't have the necessary permissions.

#### 409 - Returned if an action with this priority scheme is still in progress.

