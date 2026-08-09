# _73-project-templates API 요약

이 리소스 그룹은 Jira의 "커스텀 프로젝트 템플릿"을 조회·저장·수정·삭제하는 API 모음이다. 새 프로젝트를 만들 때 쓰는 재사용 가능한 조직 차원의 템플릿(보드, 워크플로우, 필드, 권한 등 구성 묶음)을 관리한다.

## 제외된 API

- `01-create-custom-project-post.md`: 커스텀 템플릿으로 프로젝트를 생성하는 API로, 문서에 "Administer Jira global permission" (사이트 전체 관리자 권한)이 명시적으로 요구되어 있고 "Jira Enterprise edition"에서만 지원된다. SSAFY 교육생 계정(프로젝트 관리자 수준)으로는 호출이 불가능할 가능성이 높아 제외한다.

---

### [중간] 1. 커스텀 프로젝트 템플릿 편집 (PUT /rest/api/3/project-template/edit-template)

## 기본 정보

- **기능:** 기존에 저장된 커스텀 프로젝트 템플릿의 이름, 설명, 생성 옵션을 수정한다.
- **Endpoint:** `PUT /rest/api/3/project-template/edit-template`
- **인증:** Bearer Token(Atlassian API 인증) 필요
- **권한:** 문서에 명시된 별도 권한 없음 (단, Jira Enterprise edition에서만 지원되는 커스텀 템플릿 기능)

## 설명

이미 저장된 커스텀 프로젝트 템플릿(`templateKey`로 식별)의 이름·설명·화면/워크플로우 위임 관리 옵션을 갱신할 때 사용한다. Jira Enterprise edition에서만 지원되는 기능이며, 템플릿 자체의 구조(캐퍼빌리티 구성)는 변경하지 않고 메타데이터만 수정한다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `templateKey` | string | Y (추정) | - | 수정할 템플릿의 고유 식별자 | `"my-template-key"` |
| `templateName` | string | N | - | 템플릿의 이름 | `"My Custom Template"` |
| `templateDescription` | string | N | - | 템플릿에 대한 설명 | `"팀 표준 소프트웨어 프로젝트 템플릿"` |
| `templateGenerationOptions.enableScreenDelegatedAdminSupport` | boolean | N | - | 활성화 시 화면 및 관련 스킴을 참조가 아닌 복사본으로 관리 | `false` |
| `templateGenerationOptions.enableWorkflowDelegatedAdminSupport` | boolean | N | - | 활성화 시 워크플로우 및 워크플로우 스킴을 참조가 아닌 복사본으로 관리 | `false` |

```json
{
  "templateDescription": "팀 표준 소프트웨어 프로젝트 템플릿",
  "templateGenerationOptions": {
    "enableScreenDelegatedAdminSupport": false,
    "enableWorkflowDelegatedAdminSupport": false
  },
  "templateKey": "my-template-key",
  "templateName": "My Custom Template"
}
```

## Response

### `200 OK`

응답 스키마가 `any`로 문서화되어 있어 구체적인 필드는 명시되지 않음.

```json
{}
```

## 주의 사항

- Jira Enterprise edition에서만 지원되는 API이다.
- 응답 본문 스키마가 문서상 `any`로만 표기되어 있어 실제 응답 구조는 호출 후 확인이 필요하다.

---

### [중간] 2. 커스텀 프로젝트 템플릿 조회 (GET /rest/api/3/project-template/live-template)

## 기본 정보

- **기능:** `templateKey` 또는 `projectId`로 라이브(live) 커스텀 프로젝트 템플릿의 상세 정보를 조회한다.
- **Endpoint:** `GET /rest/api/3/project-template/live-template`
- **인증:** Bearer Token(Atlassian API 인증) 필요
- **권한:** 문서에 명시된 별도 권한 없음 (Jira Enterprise edition 전용 기능)

## 설명

`projectId` 또는 `templateKey` 중 하나를 지정해 해당 커스텀 템플릿의 아키타입(프로젝트 유형), 기본 보드 뷰, 설명, 생성 옵션 등 상세 정보를 가져온다. Jira Enterprise edition에서만 지원되는 "라이브 템플릿" 개념을 조회하는 API다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `projectId` | string | N | - | 커스텀 템플릿과 연결된 프로젝트 키(선택) | `"PROJ"` |
| `templateKey` | string | N | - | 조회할 커스텀 템플릿의 키(선택) | `"my-template-key"` |

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `archetype.realType` | enum | 실제 프로젝트 유형(BUSINESS, SOFTWARE, PRODUCT_DISCOVERY, SERVICE_DESK, CUSTOMER_SERVICE, OPS) | `"SOFTWARE"` |
| `archetype.style` | enum | 프로젝트 스타일(classic, next-gen) | `"next-gen"` |
| `archetype.type` | enum | 표시용 프로젝트 유형 | `"SOFTWARE"` |
| `defaultBoardView` | string | 기본 보드 뷰 | `"kanban"` |
| `description` | string | 템플릿 설명 | `"팀 표준 템플릿"` |
| `liveTemplateProjectIdReference` | integer | 라이브 템플릿이 참조하는 프로젝트 ID | `10001` |
| `name` | string | 템플릿 이름 | `"My Custom Template"` |
| `projectTemplateKey.key` | string | 템플릿 키 | `"my-template-key"` |
| `projectTemplateKey.uuid` | string | 템플릿 UUID | `"550e8400-e29b-41d4-a716-446655440000"` |
| `snapshotTemplate` | object | 스냅샷 템플릿 데이터(구조 미상세) | `{}` |
| `templateGenerationOptions.enableScreenDelegatedAdminSupport` | boolean | 화면 위임 관리 지원 여부 | `false` |
| `templateGenerationOptions.enableWorkflowDelegatedAdminSupport` | boolean | 워크플로우 위임 관리 지원 여부 | `false` |
| `type` | enum | 템플릿 유형(LIVE, SNAPSHOT) | `"LIVE"` |

```json
{
  "archetype": {
    "realType": "SOFTWARE",
    "style": "next-gen",
    "type": "SOFTWARE"
  },
  "defaultBoardView": "kanban",
  "description": "팀 표준 템플릿",
  "liveTemplateProjectIdReference": 10001,
  "name": "My Custom Template",
  "projectTemplateKey": {
    "key": "my-template-key",
    "uuid": "550e8400-e29b-41d4-a716-446655440000"
  },
  "snapshotTemplate": {},
  "templateGenerationOptions": {
    "enableScreenDelegatedAdminSupport": false,
    "enableWorkflowDelegatedAdminSupport": false
  },
  "type": "LIVE"
}
```

## 주의 사항

- Jira Enterprise edition에서만 지원되는 API이다.
- `projectId`, `templateKey` 둘 다 선택 파라미터이지만, 실제로는 최소 하나는 지정해야 의미 있는 결과를 얻을 수 있을 것으로 추정된다.

---

### [중간] 3. 커스텀 프로젝트 템플릿 삭제 (DELETE /rest/api/3/project-template/remove-template)

## 기본 정보

- **기능:** 지정한 커스텀 프로젝트 템플릿을 삭제한다.
- **Endpoint:** `DELETE /rest/api/3/project-template/remove-template`
- **인증:** Bearer Token(Atlassian API 인증) 필요
- **권한:** 문서에 명시된 별도 권한 없음 (Jira Enterprise edition 전용 기능)

## 설명

`templateKey`로 식별되는 커스텀 프로젝트 템플릿을 완전히 제거한다. Jira Enterprise edition에서만 지원되는 기능이며, 삭제는 되돌릴 수 없는 작업이므로 신중하게 사용해야 한다.

## Request

### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `templateKey` | string | Y | - | 삭제할 커스텀 템플릿의 키 | `"my-template-key"` |

## Response

### `200 OK`

응답 스키마가 `any`로 문서화되어 있어 구체적인 필드는 명시되지 않음.

```json
{}
```

## 주의 사항

- Jira Enterprise edition에서만 지원되는 API이다.
- 삭제는 복구 불가능한 작업으로 추정되므로 실행 전 확인 절차가 필요하다.

---

### [중간] 4. 커스텀 프로젝트 템플릿 저장 (POST /rest/api/3/project-template/save-template)

## 기본 정보

- **기능:** 기존 프로젝트를 기반으로 새로운 커스텀 프로젝트 템플릿을 저장한다.
- **Endpoint:** `POST /rest/api/3/project-template/save-template`
- **인증:** Bearer Token(Atlassian API 인증) 필요
- **권한:** 문서에 명시된 별도 권한 없음 (Jira Enterprise edition 전용 기능)

## 설명

지정된 프로젝트(`projectId`)의 구성을 기반으로 LIVE 또는 SNAPSHOT 형태의 커스텀 템플릿을 새로 저장한다. 이후 저장된 템플릿은 조회(GET live-template), 편집(PUT edit-template), 삭제(DELETE remove-template) API로 관리할 수 있다. Jira Enterprise edition에서만 지원된다.

## Request

### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `templateName` | string | Y (추정) | - | 저장할 템플릿의 이름 | `"My Custom Template"` |
| `templateDescription` | string | N | - | 템플릿 설명 | `"팀 표준 템플릿"` |
| `templateFromProjectRequest.projectId` | integer | Y (추정) | - | 템플릿의 기반이 되는 대상 프로젝트 ID | `10001` |
| `templateFromProjectRequest.templateType` | enum | Y (추정) | `LIVE`, `SNAPSHOT` | 저장할 템플릿의 유형 | `"LIVE"` |
| `templateFromProjectRequest.templateGenerationOptions.enableScreenDelegatedAdminSupport` | boolean | N | - | 화면 위임 관리 지원 여부 | `false` |
| `templateFromProjectRequest.templateGenerationOptions.enableWorkflowDelegatedAdminSupport` | boolean | N | - | 워크플로우 위임 관리 지원 여부 | `false` |

```json
{
  "templateDescription": "팀 표준 템플릿",
  "templateFromProjectRequest": {
    "projectId": 10001,
    "templateGenerationOptions": {
      "enableScreenDelegatedAdminSupport": false,
      "enableWorkflowDelegatedAdminSupport": false
    },
    "templateType": "LIVE"
  },
  "templateName": "My Custom Template"
}
```

## Response

### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `projectTemplateKey.key` | string | 새로 저장된 템플릿의 키 | `"my-template-key"` |
| `projectTemplateKey.uuid` | string | 새로 저장된 템플릿의 UUID | `"550e8400-e29b-41d4-a716-446655440000"` |

```json
{
  "projectTemplateKey": {
    "key": "my-template-key",
    "uuid": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

## 주의 사항

- Jira Enterprise edition에서만 지원되는 API이다.
- `templateType`을 `LIVE`로 지정하면 원본 프로젝트와 연결이 유지되는 템플릿이, `SNAPSHOT`으로 지정하면 저장 시점의 스냅샷 템플릿이 생성되는 것으로 추정된다.
