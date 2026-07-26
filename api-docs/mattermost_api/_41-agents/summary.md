# 1. Get available agents

## 기본 정보
- **기능**: 사용 가능한 AI 에이전트 목록을 조회한다.
- **Endpoint**: `GET /api/v4/agents`
- **인증**: 로그인 필요
- **권한**: 없음 (인증만 필요)

## 설명
AI 플러그인의 bridge API로부터 사용 가능한 모든 에이전트를 조회하는 API이다. 사용자 ID가 제공되면 해당 사용자가 접근 가능한 에이전트만 반환된다. 최소 서버 버전 11.2.

## Response

### 200 - Agents retrieved successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| agents | object[] | 사용 가능한 에이전트 목록 |
| agents[].id | string | 에이전트 고유 식별자 |
| agents[].displayName | string | 사람이 읽을 수 있는 에이전트 이름 |
| agents[].username | string | 에이전트 봇에 연결된 사용자명 |
| agents[].service_id | string | 이 에이전트를 제공하는 서비스 ID |
| agents[].service_type | string | 서비스 유형 (예: openai, anthropic) |

```json
{
  "agents": [
    {
      "id": "string",
      "displayName": "string",
      "username": "string",
      "service_id": "string",
      "service_type": "string"
    }
  ]
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 500 | 서버 오류 |

---

# 2. Get agents bridge status

## 기본 정보
- **기능**: AI 플러그인 bridge의 상태(가용 여부)를 조회한다.
- **Endpoint**: `GET /api/v4/agents/status`
- **인증**: 로그인 필요
- **권한**: 없음 (인증만 필요)

## 설명
AI 플러그인 bridge의 상태를 조회하는 API이다. 가용 여부(boolean)와, 사용 불가일 경우 사유 코드를 반환한다. 최소 서버 버전 11.2.

## Response

### 200 - Status retrieved successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| available | boolean | AI 플러그인 bridge 가용 여부 |
| reason | string | 사용 불가 시 사유 코드 (translation ID) |

```json
{
  "available": true,
  "reason": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 500 | 서버 오류 |

---

# 3. Get available LLM services

## 기본 정보
- **기능**: 사용 가능한 LLM 서비스 목록을 조회한다.
- **Endpoint**: `GET /api/v4/llmservices`
- **인증**: 로그인 필요
- **권한**: 없음 (인증만 필요)

## 설명
AI 플러그인의 bridge API로부터 사용 가능한 모든 LLM 서비스를 조회하는 API이다. 사용자 ID가 제공되면 해당 사용자가 (허용된 봇을 통해) 접근 가능한 서비스만 반환된다. 최소 서버 버전 11.2.

## Response

### 200 - LLM services retrieved successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| services | object[] | 사용 가능한 LLM 서비스 목록 |
| services[].id | string | LLM 서비스 고유 식별자 |
| services[].name | string | LLM 서비스 이름 |
| services[].type | string | 서비스 유형 (예: openai, anthropic, azure) |

```json
{
  "services": [
    {
      "id": "string",
      "name": "string",
      "type": "string"
    }
  ]
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 500 | 서버 오류 |

---
