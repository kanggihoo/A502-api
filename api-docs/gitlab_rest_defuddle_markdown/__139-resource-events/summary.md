# Resource Events API 명세서 (관리자 권한 미필요 API)


## 07. Get a list of merge request resource state events [GET]

### 기본 정보

- **기능:** 특정 머지 리퀘스트(MR)의 상태 변경(opened, closed, merged, reopened) 히스토리 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{eventable_id}/resource_state_events`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### Response

#### `200 OK`
```json
[
  {
    "id": 201,
    "user": { "username": "reviewer1" },
    "created_at": "2026-07-23T12:00:00Z",
    "state": "merged"
  }
]
```

---

## 08. Get a single merge request resource state event [GET]

### 기본 정보

- **기능:** 단일 MR 상태 변경 이벤트를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{eventable_id}/resource_state_events/{event_id}`
- **인증:** Bearer Token 필요

---



## 13. Get a list of merge request resource label events [GET]

### 기본 정보

- **기능:** 특정 머지 리퀘스트(MR)의 라벨 추가/제거 변경 히스토리를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{eventable_id}/resource_label_events`
- **인증:** Bearer Token 필요

---

## 14. Get a single merge request resource label event [GET]

### 기본 정보

- **기능:** 단일 MR 라벨 변경 이벤트를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{eventable_id}/resource_label_events/{event_id}`
- **인증:** Bearer Token 필요

---

#
