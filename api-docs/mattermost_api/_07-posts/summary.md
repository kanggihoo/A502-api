# 3. Search posts across all teams

## 기본 정보
- **기능**: 현재 사용자가 접근 가능한 모든 팀에 걸쳐 게시물을 검색한다.
- **Endpoint**: `POST /api/v4/posts/search`
- **인증**: Bearer Token 필요
- **권한**: 인증된 사용자면 충분 (별도의 이름있는 권한 불요)

## 설명
현재 로그인한 사용자가 조회 가능한 범위 내에서 모든 팀을 대상으로 게시물을 검색한다. 검색어(`terms`)를 기반으로 하며 OR 검색 여부, 삭제된 채널 포함 여부, 페이지네이션 등을 옵션으로 지정할 수 있다. Elasticsearch가 활성화된 5.1 이상 서버에서는 응답에 매칭된 검색어 정보(`matches`)도 함께 제공된다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| terms | string | Yes | 검색어 |
| is_or_search | boolean | No | OR 조건으로 검색할지 여부 |
| time_zone_offset | integer | No | 클라이언트 타임존 오프셋 |
| include_deleted_channels | boolean | No | 삭제된 채널의 게시물도 포함할지 여부 |
| page | integer | No | 페이지 번호 |
| per_page | integer | No | 페이지당 결과 수 |

```json
{
  "terms": "hello world",
  "is_or_search": false,
  "time_zone_offset": 0,
  "include_deleted_channels": false,
  "page": 0,
  "per_page": 60
}
```

## Response

### 200 - Post search successful
| 필드 | 타입 | 설명 |
|---|---|---|
| order | string[] | 검색 결과에 해당하는 게시물 ID 순서 배열 |
| posts | object | 게시물 ID를 키로 하는 게시물 객체 맵 |
| matches | object | 게시물 ID를 키로 하는 매칭된 검색어 목록 맵 (Elasticsearch 활성화된 5.1 이상 서버에서만 채워짐) |

```json
{
  "order": [
    "string"
  ],
  "posts": {},
  "matches": {}
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |

---

# 28. Rewrite a message using AI

## 기본 정보
- **기능**: AI를 이용해 지정된 액션에 따라 메시지를 다시 작성(rewrite)한다.
- **Endpoint**: `POST /api/v4/posts/rewrite`
- **인증**: Bearer Token 필요
- **권한**: 인증된 사용자면 충분 (별도의 이름있는 권한 불요)
- **최소 서버 버전**: 11.2

## 설명
전달된 메시지 텍스트를 지정된 AI 에이전트(`agent_id`)와 액션(`action`)에 따라 재작성하여 반환한다. 지원되는 액션은 커스텀 프롬프트 적용, 축약, 부연 설명, 문장 개선, 맞춤법 교정, 단순화, 요약이다. `action`이 `custom`인 경우 `custom_prompt` 필드가 필수이며, 그 외 액션에서는 선택적으로 사용할 수 있다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| agent_id | string | Yes | 재작성에 사용할 AI 에이전트의 ID |
| message | string | Yes | 재작성할 메시지 텍스트 |
| action | enum("custom" \| "shorten" \| "elaborate" \| "improve_writing" \| "fix_spelling" \| "simplify" \| "summarize") | Yes | 수행할 재작성 액션 |
| custom_prompt | string | No | 재작성용 커스텀 프롬프트. `action`이 `custom`일 때 필수, 그 외에는 선택 |

```json
{
  "agent_id": "string",
  "message": "string",
  "action": "improve_writing",
  "custom_prompt": "string"
}
```

## Response

### 200 - Message rewritten successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| rewritten_text | string | 재작성된 메시지 텍스트 |

```json
{
  "rewritten_text": "string"
}
```

### 500 - Internal server error
| 필드 | 타입 | 설명 |
|---|---|---|
| status_code | integer | HTTP 상태 코드 |
| id | string | 오류 식별자 |
| message | string | 오류 메시지 |
| request_id | string | 요청 추적 ID |

```json
{
  "status_code": 500,
  "id": "string",
  "message": "string",
  "request_id": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 500 | Internal server error |

## 주의 사항
Mattermost 서버 11.2 이상에서만 지원되는 API이다.
