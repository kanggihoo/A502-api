# 1. Get all shared channels for team

## 기본 정보
- **기능**: 팀의 공유 채널(shared channel) 목록을 조회한다.
- **Endpoint**: `GET /api/v4/sharedchannels/{team_id}`
- **인증**: 로그인 필요
- **권한**: `view_team` (해당 팀에 대해)

## 설명
특정 팀의 공유 채널 목록을 페이지 단위로 조회하는 API이다. `manage_shared_channels` 권한이 없는 일반 사용자는 본인이 멤버인 채널로 결과가 제한된다. 최소 서버 버전 5.50.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| team_id | string | Yes | 팀 ID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| page | integer | No | - | 조회할 페이지 |
| per_page | integer | No | - | 페이지당 공유 채널 수 |

## Response

### 200 - Shared channels fetch successful. Result may be empty.
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 공유 채널의 채널 ID |
| team_id | string | 팀 ID |
| home | boolean | 이 클러스터가 공유 채널의 홈 클러스터인지 여부 |
| readonly | boolean | 읽기 전용으로 공유되었는지 여부 |
| name | string | 공유된 채널 이름 (원본 채널 이름과 다를 수 있음) |
| display_name | string | 로컬에 표시되는 채널 표시명 |
| purpose | string | 채널 목적 |
| header | string | 채널 헤더 |
| creator_id | string | 채널을 공유한 사용자 ID |
| create_at | integer | 채널이 공유된 시각 (밀리초) |
| update_at | integer | 공유 채널 레코드가 마지막으로 갱신된 시각 (밀리초) |
| remote_id | string | 공유 채널의 홈인 원격 클러스터 ID |

```json
[
  {
    "id": "string",
    "team_id": "string",
    "home": true,
    "readonly": false,
    "name": "string",
    "display_name": "string",
    "purpose": "string",
    "header": "string",
    "creator_id": "string",
    "create_at": 0,
    "update_at": 0,
    "remote_id": "string"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

## 주의 사항
`manage_shared_channels` 권한이 없으면 본인이 멤버인 채널만 반환된다.

---

# 3. Get remote cluster info by ID for user

## 기본 정보
- **기능**: 원격 클러스터 ID로 원격 클러스터 정보를 조회한다.
- **Endpoint**: `GET /api/v4/sharedchannels/remote_info/{remote_id}`
- **인증**: 로그인 필요
- **권한**: 없음 (해당 원격 클러스터와 공유된 채널에 하나 이상 속해 있어야 함)

## 설명
remoteId를 기준으로 원격 클러스터 정보를 조회하는 API이다. 인증된 사용자여야 하며, 해당 원격 클러스터와 공유된 채널에 최소 하나 이상 속해 있어야 한다. 최소 서버 버전 5.50.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| remote_id | string | Yes | 원격 클러스터 GUID |

### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 |
|---|---|---|---|---|
| include_deleted | boolean | No | - | 삭제된 원격 클러스터 포함 여부 |

## Response

### 200 - Remote cluster info retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| display_name | string | 원격 클러스터의 표시명 |
| create_at | integer | 원격 클러스터가 생성된 시각 (밀리초) |
| last_ping_at | integer | 원격 클러스터가 마지막으로 성공적으로 ping된 시각 (밀리초) |

```json
{
  "display_name": "string",
  "create_at": 0,
  "last_ping_at": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 원격 클러스터를 찾을 수 없음 |

---

# 6. Get remote clusters for a shared channel

## 기본 정보
- **기능**: 공유 채널에 연결된 원격 클러스터들의 정보를 조회한다.
- **Endpoint**: `GET /api/v4/sharedchannels/{channel_id}/remotes`
- **인증**: 로그인 필요
- **권한**: `read_channel` (해당 채널에 대해)

## 설명
특정 공유 채널에 연결된 원격 클러스터들의 정보를 조회하는 API이다. 해당 채널에 대한 `read_channel` 권한이 있어야 한다. 최소 서버 버전 10.11.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| channel_id | string | Yes | 채널 GUID |

## Response

### 200 - Remote clusters retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| display_name | string | 원격 클러스터의 표시명 |
| create_at | integer | 원격 클러스터가 생성된 시각 (밀리초) |
| last_ping_at | integer | 원격 클러스터가 마지막으로 성공적으로 ping된 시각 (밀리초) |

```json
[
  {
    "display_name": "string",
    "create_at": 0,
    "last_ping_at": 0
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 채널을 찾을 수 없음 |

---

# 7. Check if user can DM another user in shared channels context

## 기본 정보
- **기능**: 공유 채널 컨텍스트에서 특정 사용자에게 DM을 보낼 수 있는지 확인한다.
- **Endpoint**: `GET /api/v4/sharedchannels/users/{user_id}/can_dm/{other_user_id}`
- **인증**: 로그인 필요
- **권한**: 없음 (인증되어 있고 대상 사용자를 볼 수 있어야 함)

## 설명
공유 채널 컨텍스트에서 한 사용자가 다른 사용자에게 DM을 보낼 수 있는지 확인하는 API이다. 사용자 가시성(visibility) 외에도 원격 사용자에 대해서는 원격 클러스터의 direct-connect 제한도 함께 평가한다. 최소 서버 버전 10.11.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| user_id | string | Yes | 사용자 GUID |
| other_user_id | string | Yes | 상대 사용자 GUID |

## Response

### 200 - DM permission check successful
| 필드 | 타입 | 설명 |
|---|---|---|
| can_dm | boolean | 상대 사용자에게 DM을 보낼 수 있는지 여부 |

```json
{
  "can_dm": true
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 404 | 사용자를 찾을 수 없음 |

---

## 제외된 API
- **02-Get shared channel remotes by remote cluster**: `manage_secure_connections` 또는 `manage_shared_channels` 권한이 필요해 제외됨.
- **04-Invites a remote cluster to a channel**: `manage_shared_channels` 권한이 필요해 제외됨.
- **05-Uninvites a remote cluster to a channel**: `manage_shared_channels` 권한이 필요해 제외됨.
