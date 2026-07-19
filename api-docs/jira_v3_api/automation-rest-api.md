---
title: "Automation REST API"
source: "https://developer.atlassian.com/cloud/automation/rest/api-group-rule-management/#api-group-rule-management"
created: 2026-07-20
description: ""
---

Cloud
Automation / Reference / REST API

GET

## 규칙 요약 목록 조회

모든 규칙의 요약을 가져옵니다.

**Deprecated:** 응답 본문의 `links` 필드가 최근에 절대 링크 대신 쿼리 파라미터만 반환하도록 변경되었습니다. [변경 로그 공지](https://developer.atlassian.com/cloud/automation/api/changelog/#1-august-2025)를 참조하세요.

Forge 및 OAuth2 앱은 이 REST 리소스에 접근할 수 없습니다.

### 요청

#### 쿼리 파라미터

**cursor**
string

**limit**
number

### 응답

모든 규칙의 규칙 요약을 반환합니다.

#### application/json

RuleSummaryResponse

규칙 요약 검색 결과입니다. 0개 이상의 결과를 포함합니다.

GET /rest/v1/rule/summary

```curl
curl --request GET \
  --url 'https://api.atlassian.com/automation/public/{product}/{cloudid}/rest/v1/rule/summary' \
  --header 'Accept: application/json'
```

200 응답

```json
{
  "links": {
    "self": "?cursor=bbbbbb&limit=100",
    "next": "?cursor=bbbbbb&limit=100",
    "prev": "?cursor=bbbbbb&limit=100"
  },
  "data": [
    {
      "actorAccountId": "5b10ac8d82e05b22cc7d4ef5",
      "ruleScopeARIs": [
        "ari:cloud:jira:182b9218-d56a-453d-9659-3f29ea2aa7eb:project/10001"
      ],
      "authorAccountId": "5b10ac8d82e05b22cc7d4ef5",
      "created": 1743568964.174,
      "updated": 1743568964.174,
      "description": "A rule description",
      "uuid": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
      "labels": [
        "label one"
      ],
      "name": "Rule one",
      "state": "ENABLED"
    }
  ]
}
```

POST

## 규칙 요약 검색

POST를 통해 주어진 기준과 일치하는 규칙의 요약을 가져옵니다.

트리거, 규칙 상태 및 규칙 범위(단일 ARI)로 필터링을 지원합니다.

**Deprecated:** 응답 본문의 `links` 필드가 최근에 절대 링크 대신 쿼리 파라미터만 반환하도록 변경되었습니다. [변경 로그 공지](https://developer.atlassian.com/cloud/automation/api/changelog/#1-august-2025)를 참조하세요.

Forge 및 OAuth2 앱은 이 REST 리소스에 접근할 수 없습니다.

### 요청

#### 요청 본문 application/json

검색할 쿼리 파라미터입니다. trigger, state, scope 또는 limit 중 하나 이상이 있어야 합니다.

**cursor**
string

**trigger**
string

**state**
RuleState

**scope**
ARI

**author**
AccountId

**limit**
number

### 응답

쿼리와 일치하는 규칙 요약을 반환합니다.

#### application/json

RuleSummaryResponse

규칙 요약 검색 결과입니다. 0개 이상의 결과를 포함합니다.

POST /rest/v1/rule/summary

```curl
curl --request POST \
  --url 'https://api.atlassian.com/automation/public/{product}/{cloudid}/rest/v1/rule/summary' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
  "cursor": "ewogICJhZnRlck9iamVjdElkIjogIjExMTIxMTEiLAogICJvcmRlckJ5IjogIklEIiwKICAicGFnZVNpemUiOiA1Cn0=",
  "trigger": "jira.version.event.trigger:created",
  "state": "ENABLED",
  "scope": "ari:cloud:jira:182b9218-d56a-453d-9659-3f29ea2aa7eb:project/10001",
  "author": "<string>",
  "limit": 50
}'
```

200 응답

```json
{
  "links": {
    "self": "?cursor=bbbbbb&limit=100",
    "next": "?cursor=bbbbbb&limit=100",
    "prev": "?cursor=bbbbbb&limit=100"
  },
  "data": [
    {
      "actorAccountId": "5b10ac8d82e05b22cc7d4ef5",
      "ruleScopeARIs": [
        "ari:cloud:jira:182b9218-d56a-453d-9659-3f29ea2aa7eb:project/10001"
      ],
      "authorAccountId": "5b10ac8d82e05b22cc7d4ef5",
      "created": 1743568964.174,
      "updated": 1743568964.174,
      "description": "A rule description",
      "uuid": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
      "labels": [
        "label one"
      ],
      "name": "Rule one",
      "state": "ENABLED"
    }
  ]
}
```

POST

## 새 규칙 생성

제공된 Rule Payload에서 새 규칙을 생성합니다.

새 규칙에 UUID를 제공하는 경우 고유해야 하며 V7이어야 합니다. V7의 시간 기반 특성은 규칙의 정렬 및 페이지네이션에 영향을 미칩니다.

UUID로 규칙 조회 응답과 동일한 구조의 규칙 페이로드를 허용합니다.

Forge 및 OAuth2 앱은 이 REST 리소스에 접근할 수 없습니다.

### 요청

#### 요청 본문 application/json

**rule**
CreateRulePayload
필수

**connections**
array\<ConnectionWriteDTO>

### 응답

규칙이 성공적으로 생성되었습니다.

#### application/json

RuleUuidResponse

POST /rest/v1/rule

```curl
curl --request POST \
  --url 'https://api.atlassian.com/automation/public/{product}/{cloudid}/rest/v1/rule' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
  "rule": {
    "actor": {
      "actor": "<string>",
      "type": "ACCOUNT_ID"
    },
    "authorAccountId": "<string>",
    "canOtherRuleTrigger": true,
    "collaborators": [
      "<string>"
    ],
    "components": [
      {
        "children": [],
        "component": "TRIGGER",
        "conditionParentId": "<string>",
        "conditions": [],
        "connectionId": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
        "parentId": "<string>",
        "schemaVersion": 2154,
        "type": "<string>",
        "value": "<string>"
      }
    ],
    "description": "<string>",
    "labels": [
      "<string>"
    ],
    "name": "<string>",
    "notifyOnError": "FIRSTERROR",
    "ruleScopeARIs": [
      "ari:cloud:jira:182b9218-d56a-453d-9659-3f29ea2aa7eb:project/10001"
    ],
    "state": "ENABLED",
    "trigger": {
      "component": "TRIGGER",
      "conditions": [
        {
          "children": [],
          "component": "TRIGGER",
          "conditionParentId": "<string>",
          "conditions": [],
          "connectionId": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
          "parentId": "<string>",
          "schemaVersion": 2154,
          "type": "<string>",
          "value": "<string>"
        }
      ],
      "connectionId": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
      "schemaVersion": 2154,
      "type": "<string>",
      "value": "<string>"
    },
    "uuid": "<string>",
    "writeAccessType": "OWNER_ONLY"
  },
  "connections": [
    {
      "id": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
      "accountId": "<string>",
      "connectionTargetKey": "com.atlassian.confluence.native",
      "targetConfigJson": "<string>",
      "authType": "OAUTH_3LO"
    }
  ]
}'
```

201 응답

```json
{
  "ruleUuid": "0192e5ac-0e25-71de-ba7b-d972e6a2049a"
}
```

GET

## UUID로 규칙 조회

제공된 UUID의 규칙을 검색하는 요청을 수행합니다. 규칙 페이로드, 트리거, 컴포넌트 및 기타 메타데이터를 포함합니다.

Forge 및 OAuth2 앱은 이 REST 리소스에 접근할 수 없습니다.

### 요청

#### 경로 파라미터

**ruleUuid**
string
필수

#### 쿼리 파라미터

**redactSensitiveFields**
boolean

### 응답

지정된 규칙의 Rule Config를 반환합니다.

#### application/json

RuleConfigResponse

GET /rest/v1/rule/{ruleUuid}

```curl
curl --request GET \
  --url 'https://api.atlassian.com/automation/public/{product}/{cloudid}/rest/v1/rule/{ruleUuid}' \
  --header 'Accept: application/json'
```

200 응답

```json
{
  "rule": {
    "actor": {
      "actor": "<string>",
      "type": "ACCOUNT_ID"
    },
    "authorAccountId": "<string>",
    "canOtherRuleTrigger": true,
    "collaborators": [
      "<string>"
    ],
    "components": [
      {
        "id": "151",
        "children": [],
        "component": "TRIGGER",
        "conditionParentId": "<string>",
        "conditions": [],
        "connectionId": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
        "parentId": "<string>",
        "schemaVersion": 2154,
        "type": "<string>",
        "value": "<string>"
      }
    ],
    "created": 2154,
    "description": "<string>",
    "labels": [
      "<string>"
    ],
    "name": "<string>",
    "notifyOnError": "FIRSTERROR",
    "ruleScopeARIs": [
      "ari:cloud:jira:182b9218-d56a-453d-9659-3f29ea2aa7eb:project/10001"
    ],
    "state": "ENABLED",
    "trigger": {
      "id": "151",
      "component": "TRIGGER",
      "conditions": [
        {
          "id": "151",
          "children": [],
          "component": "TRIGGER",
          "conditionParentId": "<string>",
          "conditions": [],
          "connectionId": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
          "parentId": "<string>",
          "schemaVersion": 2154,
          "type": "<string>",
          "value": "<string>"
        }
      ],
      "connectionId": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
      "schemaVersion": 2154,
      "type": "<string>",
      "value": "<string>"
    },
    "updated": 2154,
    "uuid": "<string>",
    "writeAccessType": "OWNER_ONLY"
  },
  "connections": [
    {
      "id": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
      "accountId": "<string>",
      "connectionTargetKey": "com.atlassian.confluence.native",
      "targetConfigJson": "<string>",
      "authType": "OAUTH_3LO",
      "createdAt": 1743568964.174,
      "updatedAt": 1743568964.174,
      "container": {
        "id": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
        "containerType": "RULE"
      }
    }
  ]
}
```

PUT

## 기존 규칙 업데이트

UUID로 규칙 조회 응답과 동일한 구조의 규칙 페이로드를 받아 기존 규칙을 업데이트합니다. ComponentId는 이미 존재하는 컴포넌트에만 필요합니다. 새 컴포넌트는 필요에 따라 생성되거나 삭제됩니다.

Forge 및 OAuth2 앱은 이 REST 리소스에 접근할 수 없습니다.

### 요청

#### 경로 파라미터

**ruleUuid**
string
필수

#### 요청 본문 application/json

**rule**
RulePayload
필수

**connections**
array\<ConnectionWriteDTO>

### 응답

규칙이 성공적으로 업데이트되었습니다.

#### application/json

RuleUuidResponse

PUT /rest/v1/rule/{ruleUuid}

```curl
curl --request PUT \
  --url 'https://api.atlassian.com/automation/public/{product}/{cloudid}/rest/v1/rule/{ruleUuid}' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
  "rule": {
    "actor": {
      "actor": "<string>",
      "type": "ACCOUNT_ID"
    },
    "authorAccountId": "<string>",
    "canOtherRuleTrigger": true,
    "collaborators": [
      "<string>"
    ],
    "components": [
      {
        "id": "151",
        "children": [],
        "component": "TRIGGER",
        "conditionParentId": "<string>",
        "conditions": [],
        "connectionId": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
        "parentId": "<string>",
        "schemaVersion": 2154,
        "type": "<string>",
        "value": "<string>"
      }
    ],
    "description": "<string>",
    "labels": [
      "<string>"
    ],
    "name": "<string>",
    "notifyOnError": "FIRSTERROR",
    "ruleScopeARIs": [
      "ari:cloud:jira:182b9218-d56a-453d-9659-3f29ea2aa7eb:project/10001"
    ],
    "state": "ENABLED",
    "trigger": {
      "id": "151",
      "component": "TRIGGER",
      "conditions": [
        {
          "id": "151",
          "children": [],
          "component": "TRIGGER",
          "conditionParentId": "<string>",
          "conditions": [],
          "connectionId": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
          "parentId": "<string>",
          "schemaVersion": 2154,
          "type": "<string>",
          "value": "<string>"
        }
      ],
      "connectionId": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
      "schemaVersion": 2154,
      "type": "<string>",
      "value": "<string>"
    },
    "writeAccessType": "OWNER_ONLY"
  },
  "connections": [
    {
      "id": "0192e5ac-0e25-71de-ba7b-d972e6a2049a",
      "accountId": "<string>",
      "connectionTargetKey": "com.atlassian.confluence.native",
      "targetConfigJson": "<string>",
      "authType": "OAUTH_3LO"
    }
  ]
}'
```

200 응답

```json
{
  "ruleUuid": "0192e5ac-0e25-71de-ba7b-d972e6a2049a"
}
```

DELETE

## 비활성화된 규칙 삭제

UUID로 비활성화된 규칙을 삭제합니다.

Forge 및 OAuth2 앱은 이 REST 리소스에 접근할 수 없습니다.

### 요청

#### 경로 파라미터

**ruleUuid**
string
필수

### 응답

규칙이 성공적으로 삭제되었습니다.

DELETE /rest/v1/rule/{ruleUuid}

이 페이지 평가:
