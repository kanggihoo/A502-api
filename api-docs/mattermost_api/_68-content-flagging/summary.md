# 1. Get content flagging configuration

## 기본 정보
- **기능**: 콘텐츠 신고(content flagging) 설정(신고 사유 목록 등)을 조회한다.
- **Endpoint**: `GET /api/v4/content_flagging/flag/config`
- **인증**: Bearer Token 필요
- **권한**: 없음 (일반 사용자 호출 가능)

## 설명
게시물을 신고할 때 사용자에게 보여줄 신고 사유 목록과 신고자 코멘트 필수 여부 등 콘텐츠 신고 설정을 조회하는 API이다. Enterprise Advanced 라이선스가 필요하며, feature flag로 기능이 비활성화되어 있으면 404를 반환한다.

## Response

### 200 - Configuration retrieved successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| reasons | array(string) | 콘텐츠 신고 사유 목록 |
| reporter_comment_required | boolean | 신고 시 신고자 코멘트 필수 여부 |

```json
{
  "reasons": ["string"],
  "reporter_comment_required": true
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 404 | feature flag로 기능 비활성화됨 |
| 500 | 서버 내부 오류 |
| 501 | 설정으로 비활성화되었거나 Enterprise Advanced 라이선스 없음 |

## 주의 사항
Enterprise Advanced 라이선스가 필요하다. 서버에 라이선스가 없으면 501을 반환한다.

---

# 2. Get content flagging status for a team

## 기본 정보
- **기능**: 특정 팀에서 콘텐츠 신고 기능 활성화 여부를 조회한다.
- **Endpoint**: `GET /api/v4/content_flagging/team/{team_id}/status`
- **인증**: Bearer Token 필요
- **권한**: 해당 팀 접근 권한 (팀 멤버)

## 설명
지정한 팀에서 콘텐츠 신고 기능이 활성화되어 있는지 여부를 조회하는 API이다. Enterprise Advanced 라이선스가 필요하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| team_id | string | Yes | 콘텐츠 신고 상태를 조회할 팀 ID |

## Response

### 200 - Content flagging status retrieved successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| enabled | boolean | 해당 팀의 콘텐츠 신고 활성화 여부 |

```json
{
  "enabled": true
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 403 | 해당 팀 접근 권한 없음 |
| 404 | 팀을 찾을 수 없거나 feature flag로 기능 비활성화됨 |
| 500 | 서버 내부 오류 |

---

# 3. Flag a post

## 기본 정보
- **기능**: 게시물을 사유와 코멘트를 붙여 신고한다.
- **Endpoint**: `POST /api/v4/content_flagging/post/{post_id}/flag`
- **인증**: Bearer Token 필요
- **권한**: 해당 게시물이 속한 채널 접근 권한

## 설명
게시물을 신고 사유와 코멘트를 첨부해 신고하는 API이다. 신고 사유는 서버에 설정된 사유 목록 중 하나여야 한다. 게시물이 속한 채널에 접근 가능한 사용자만 호출할 수 있으며, Enterprise Advanced 라이선스가 필요하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| post_id | string | Yes | 신고할 게시물 ID |

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| reason | string | No | 신고 사유. 설정된 사유 목록 중 하나여야 함 |
| comment | string | No | 신고자 코멘트 |

```json
{
  "reason": "string",
  "comment": "string"
}
```

## Response

### 200 - Post flagged successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 성공 시 "ok" 반환 |

```json
{
  "status": "ok"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 입력 또는 필수 필드 누락 |
| 403 | 해당 게시물을 신고할 권한 없음 |
| 404 | 게시물을 찾을 수 없거나 feature flag로 기능 비활성화됨 |
| 500 | 서버 내부 오류 |
| 501 | 설정으로 비활성화되었거나 Enterprise Advanced 라이선스 없음 |

---

# 4. Get content flagging property fields

## 기본 정보
- **기능**: 콘텐츠 신고 리포트에 연결될 수 있는 property field 목록을 조회한다.
- **Endpoint**: `GET /api/v4/content_flagging/fields`
- **인증**: Bearer Token 필요
- **권한**: 없음 (일반 사용자 호출 가능)

## 설명
게시물 신고에 대한 메타데이터를 저장하는 데 사용되는 property field 목록을 조회하는 API이다. Enterprise Advanced 라이선스가 필요하다.

## Response

### 200 - Custom fields retrieved successfully

```json
{}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 404 | feature flag로 기능 비활성화됨 |
| 500 | 서버 내부 오류 |
| 501 | 설정으로 비활성화되었거나 Enterprise Advanced 라이선스 없음 |

---

# 5. Get content flagging property field values for a post

## 기본 정보
- **기능**: 특정 게시물의 신고 관련 property field 값들을 조회한다.
- **Endpoint**: `GET /api/v4/content_flagging/post/{post_id}/field_values`
- **인증**: Bearer Token 필요
- **권한**: 해당 게시물 접근 권한

## 설명
특정 게시물의 콘텐츠 신고 리포트에 연결된 property field 값들을 조회하는 API이다. 게시물에 걸린 신고에 대한 추가 컨텍스트를 제공한다. Enterprise Advanced 라이선스가 필요하다.

## Request

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---|---|---|
| post_id | string | Yes | property field 값을 조회할 게시물 ID |

## Response

### 200 - Property field values retrieved successfully
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
| 403 | 해당 게시물 접근 권한 없음 |
| 404 | 게시물을 찾을 수 없거나 feature flag로 기능 비활성화됨 |
| 500 | 서버 내부 오류 |

---

## 제외된 API
- **06-Get a flagged post with all its content / 07-Remove a flagged post / 08-Keep a flagged post / 11-Search content reviewers / 12-Assign a content reviewer / 13-Generate and download a flagged post report**: 해당 팀의 content reviewer만 호출 가능하여 제외됨.
- **09-Get / 10-Update the system content flagging configuration**: 시스템 관리자 전용으로 제외됨.

## 공통 주의 사항
이 카테고리 전체가 Enterprise Advanced 라이선스와 feature flag 활성화를 요구한다. 서버에 라이선스가 없거나 기능이 꺼져 있으면 404/501이 반환되어 실제로는 사용하지 못할 수 있다.
