# 2. Get property fields

## 기본 정보
- **기능**: 특정 그룹·object type의 property field 목록을 조회한다 (커서 기반 페이지네이션).
- **Endpoint**: `GET /api/v4/properties/groups/{group_name}/{object_type}/fields`
- **인증**: Bearer Token 필요
- **권한**: 계층 스코프 사용 시 `read_channel`(채널) 및/또는 `view_team`(팀)

## 설명
지정한 property group과 object type에 대한 field 목록을 조회하는 API이다. 스코프 모드는 상호 배타적인 두 가지가 있다: (1) 계층 스코프(`channel_id`/`team_id`) — 지정 리소스와 그 상위 스코프의 field를 모두 반환하며 채널은 `read_channel`, 팀은 `view_team` 권한이 필요하다. (2) 단일 대상 스코프(`target_type`+`target_id`). 두 모드를 섞으면 400을 반환한다. `object_type`이 `system`이면 스코프 파라미터를 무시하고 항상 `target_type=system`으로 처리된다. `since > 0`이면 해당 시각 이후 변경분(삭제 tombstone 포함)만 반환하는 델타 동기화 모드로 동작한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| group_name | string | Yes | property group 이름 |
| object_type | string | Yes | property field가 적용되는 object 타입 |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| channel_id | string | No | - | 계층 스코프. system/팀/채널 레벨 field 포함. `read_channel` 필요. `target_type`/`target_id`와 배타적 |
| team_id | string | No | - | 계층 스코프. system/팀 레벨 field 포함. `view_team` 필요. `channel_id`가 있으면 무시됨 |
| target_type | string | No | - | 단일 대상 스코프. `system`/`team`/`channel` 중 하나. `channel_id`/`team_id`와 배타적 |
| target_id | string | No | - | 단일 대상 스코프. `target_type`이 `channel`/`team`이면 필수 |
| since | integer | No | - | 밀리초 Unix timestamp. 0보다 크면 `update_at >= since`인 field(tombstone 포함)만 반환 |
| cursor_id | string | No | - | 이전 페이지 마지막 field의 ID (커서 페이지네이션) |
| cursor_create_at | integer | No | - | 이전 페이지 마지막 field의 `create_at`. `since` 미사용 시 `cursor_id`와 함께 필수. `cursor_update_at`과 배타적 |
| cursor_update_at | integer | No | - | 이전 페이지 마지막 field의 `update_at`. `since` 사용 시 `cursor_id`와 함께 필수. `cursor_create_at`과 배타적 |
| per_page | integer | No | - | 페이지당 field 수 |

## Response

### 200 - Property fields retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | property field의 고유 식별자 (26자 영숫자) |
| type | enum | 필드 타입 (`text` \| `select` \| `multiselect`) |
| name | string | 필드 이름 |
| description | string | 필드 설명 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초), 미삭제 시 0 |
| attrs | object | 추가 속성 (select 옵션, 노출 설정 등) |

```json
[
  {
    "id": "string",
    "type": "text",
    "name": "string",
    "description": "string",
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0,
    "attrs": {}
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 (스코프 혼용, 잘못된 커서 키 등) |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 찾을 수 없음 |

## 주의 사항
커서 키는 활성 정렬 모드와 일치해야 한다: 델타 모드(`since > 0`)에서는 `cursor_update_at`, 그 외에는 `cursor_create_at`을 사용해야 하며 잘못 쓰면 400이 반환된다.

---

# 3. Search property fields across multiple object types

## 기본 정보
- **기능**: 여러 object type에 걸쳐 property field를 한 번에 검색한다.
- **Endpoint**: `POST /api/v4/properties/groups/{group_name}/fields/search`
- **인증**: Bearer Token 필요
- **권한**: 계층 스코프 사용 시 `read_channel`(채널) 및/또는 `view_team`(팀) — get property fields와 동일

## 설명
요청한 모든 object type의 매칭 field를 하나의 응답으로 반환하는 API이다. 스코프, `since`, 커서, 권한 의미는 get property fields endpoint와 동일하다. `object_types`가 정확히 `["system"]`이면 스코프/대상 파라미터를 무시하고 `target_type=system`으로 처리되며, 그 외 조합에서 명시적 스코프가 없으면 400을 반환한다. 단일 object type 요청은 단수형 endpoint 호출과 동등하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| group_name | string | Yes | property group 이름 |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| object_types | array(enum) | Yes | 포함할 object type 목록 (`post`/`channel`/`user`/`template`/`system`). 최소 1개, 알 수 없는 값은 400 |
| channel_id | string | No | 계층 스코프. `read_channel` 필요. `target_type`/`target_id`와 배타적 |
| team_id | string | No | 계층 스코프. `view_team` 필요. `channel_id`가 있으면 무시됨 |
| target_type | enum | No | 단일 대상 스코프 (`system`/`team`/`channel`). 계층 스코프 미지정 시 필수 (`["system"]` 예외) |
| target_id | string | No | `target_type`이 `channel`/`team`이면 필수 |
| since | integer | No | 밀리초 Unix timestamp. 0보다 크면 변경분(tombstone 포함)만 반환 |
| cursor_id | string | No | 이전 페이지 마지막 field의 ID |
| cursor_create_at | integer | No | `since` 미사용 시 커서 키. `cursor_update_at`과 배타적 |
| cursor_update_at | integer | No | `since` 사용 시 커서 키. `cursor_create_at`과 배타적 |
| per_page | integer | No | 페이지당 field 수 |

```json
{
  "object_types": ["user"],
  "channel_id": "string",
  "per_page": 20
}
```

## Response

### 200 - Property fields retrieval successful
(2번 endpoint와 동일한 property field 배열)

```json
[
  {
    "id": "string",
    "type": "text",
    "name": "string",
    "description": "string",
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0,
    "attrs": {}
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 찾을 수 없음 |

---

# 6. Get property values for a target

## 기본 정보
- **기능**: 특정 대상(target)의 property value 전체를 조회한다 (커서 기반 페이지네이션).
- **Endpoint**: `GET /api/v4/properties/groups/{group_name}/{object_type}/values/{target_id}`
- **인증**: Bearer Token 필요
- **권한**: 문서에 명시 없음 (조회 성격, 대상 리소스 접근 권한 기준으로 추정)

## 설명
그룹 내 특정 대상의 모든 property value를 조회하는 API이다. `template` object type은 값을 가질 수 없어 400을 반환하고, `system` object type은 전용 endpoint(`/system/values`)를 사용해야 하며 이 경로에서는 400을 반환한다. `since > 0`이면 해당 시각 이후 변경분(tombstone 포함)만 반환한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| group_name | string | Yes | property group 이름 |
| object_type | string | Yes | object 타입 |
| target_id | string | Yes | 대상 object의 ID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| since | integer | No | - | 밀리초 Unix timestamp. 0보다 크면 변경분(tombstone 포함)만 반환 |
| cursor_id | string | No | - | 이전 페이지 마지막 value의 ID |
| cursor_create_at | integer | No | - | `since` 미사용 시 커서 키. `cursor_update_at`과 배타적 |
| cursor_update_at | integer | No | - | `since` 사용 시 커서 키. `cursor_create_at`과 배타적 |
| per_page | integer | No | - | 페이지당 value 수 |

## Response

### 200 - Property values retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | property value의 고유 식별자 (26자 영숫자) |
| field_id | string | 이 값이 속한 property field의 식별자 |
| value | string | JSON 인코딩된 값 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초), 미삭제 시 0 |

```json
[
  {
    "id": "string",
    "field_id": "string",
    "value": "string",
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 (`template`/`system` object type 등) |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

---

# 8. Get property values for the system

## 기본 정보
- **기능**: Mattermost 인스턴스 자체(system)에 붙은 property value를 조회한다.
- **Endpoint**: `GET /api/v4/properties/groups/{group_name}/system/values`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증된 사용자 누구나 조회 가능)

## 설명
그룹 내에서 Mattermost 인스턴스 자체에 부착된 모든 property value를 조회하는 API이다. system 스코프 값은 인증된 사용자라면 누구나 읽을 수 있다. `system` object type의 전용 경로이며, 일반 `{object_type}/values/{target_id}` 경로에 `system`을 넣으면 400을 반환한다. `since > 0`이면 델타 동기화 모드로 동작한다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| group_name | string | Yes | property group 이름 |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| since | integer | No | - | 밀리초 Unix timestamp. 0보다 크면 변경분(tombstone 포함)만 반환 |
| cursor_id | string | No | - | 이전 페이지 마지막 value의 ID |
| cursor_create_at | integer | No | - | `since` 미사용 시 커서 키. `cursor_update_at`과 배타적 |
| cursor_update_at | integer | No | - | `since` 사용 시 커서 키. `cursor_create_at`과 배타적 |
| per_page | integer | No | - | 페이지당 value 수 |

## Response

### 200 - System property values retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | property value의 고유 식별자 (26자 영숫자) |
| field_id | string | 이 값이 속한 property field의 식별자 |
| value | string | JSON 인코딩된 값 |
| create_at | integer | 생성 시각 (밀리초) |
| update_at | integer | 수정 시각 (밀리초) |
| delete_at | integer | 삭제 시각 (밀리초), 미삭제 시 0 |

```json
[
  {
    "id": "string",
    "field_id": "string",
    "value": "string",
    "create_at": 0,
    "update_at": 0,
    "delete_at": 0
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |

---

## 제외된 API
- **01-Create a property field**: field 정의 생성은 관리 성격이며 `permission_*` 속성 설정이 시스템 관리자 전용으로 서술되어 있어 제외됨.
- **04-Update a property field / 05-Delete a property field**: field 정의 관리 성격(권한 서술 없음, field의 `permission_field` 정책에 종속)으로 보수적으로 제외됨.
- **07-Update property values for a target**: 권한 서술이 없고 field의 `permission_values` 정책에 따라 달라지므로 보수적으로 제외됨.
- **09-Update property values for the system**: 시스템 관리자 전용으로 명시되어 제외됨.
