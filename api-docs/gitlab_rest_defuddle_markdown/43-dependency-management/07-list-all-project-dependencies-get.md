# 07-List all project dependencies [GET]

`GET /api/v4/projects/{id}/dependencies`

Lists all dependencies for a specified project. This operation partially mirrors the dependency list feature, which is available only for languages and package managers supported by Gemnasium. Responses are paginated and return 20 results by default.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `package_manager` | `array` | `query` | No | Returns dependencies belonging to specified package managers: bundler, yarn, npm, pnpm, bun, maven, composer, pip, conan, go, nuget, sbt, gradle, pipenv, poetry, setuptools, apk, conda, pub, cargo. |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "name": string,
  "version": string,
  "package_manager": string,
  "dependency_file_path": string,
  "vulnerabilities": {
    "severity": string,
    "id": string,
    "name": string,
    "url": string,
  },
  "licenses": {
    "spdx_identifier": string,
    "name": string,
    "url": string,
  },
  "malware": boolean, // Malware status: true if a GLAM identifier is present, false if the SSCS add-on is active but none found, null if the SSCS add-on is inactive.
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

