# Notion OAuth 2.0 토큰 획득 — Postman/curl 가이드

`api-docs/notion-api-priority-filter.md` P1 의 OAuth 2.0(public connection) 연결을
Postman 또는 curl 로 직접 검증하기 위한 절차. 발급받은 `access_token` 을
`.env` 의 `NOTION_API_KEY` 에 넣으면 `notion_client.py` 기반 스크립트들이
Internal token 과 동일하게 동작한다.

> 문서 출처: `api-docs/notion_defuddle_markdown/06-authorization.md`

## 사전 준비 (Notion Developer portal)

1. <https://www.notion.so/my-integrations> 에서 **New integration** → **Public** 선택
2. **Configuration** 탭에서 아래 값 수집
   - `CLIENT_ID` (OAuth client ID)
   - `CLIENT_SECRET` (OAuth client secret)
3. **OAuth configuration** 에 redirect URI 등록
   - Postman 로컬 테스트 예: `https://localhost/callback` 또는 Postman 콜백 URL
4. 공유할 페이지/DB 의 `•••` → **Add connections** 로 이 public connection 추가

## 흐름 개요 (Authorization Code Grant)

```
브라우저 인가 URL  →  사용자 "Allow access"  →  redirect_uri 로 code 수신
                                                        ↓
                            POST /v1/oauth/token (Basic CLIENT_ID:SECRET)
                                                        ↓
                                access_token + refresh_token + bot_id 수신
```

---

## Step 1 — 인가 URL 을 브라우저에서 오픈

아래 URL 의 빈 칸을 채워 브라우저 주소창에 입력:

```
https://api.notion.com/v1/oauth/authorize?owner=user&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI_URLENCODED}&response_type=code&state={STATE_OPTIONAL}
```

| 파라미터 | 값 |
| --- | --- |
| `client_id` | Developer portal 의 CLIENT_ID |
| `redirect_uri` | connection 에 등록한 redirect URI (URL-encode) |
| `response_type` | 항상 `code` |
| `owner` | 항상 `user` |
| `state` | CSRF 방지용 임의값 (선택) |

사용자가 **Select pages** → 페이지/DB 선택 → **Allow access** 하면 Notion 이
`redirect_uri?code={CODE}&state=...` 로 리다이렉트한다. 이 `code` 를 복사한다.

> code 는 1회용이고 수명이 짧다. 받자마자 Step 2 로 바로 진행.

---

## Step 2 — code 를 access_token 으로 교환

엔드포인트: `POST https://api.notion.com/v1/oauth/token`
인증: HTTP Basic `base64(CLIENT_ID:CLIENT_SECRET)`

### curl

```bash
# Basic 인증 헤더를 base64 로 만들기
BASIC=$(printf '%s:%s' "$CLIENT_ID" "$CLIENT_SECRET" | base64)

curl -X POST https://api.notion.com/v1/oauth/token \
  -H "Authorization: Basic $BASIC" \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "authorization_code",
    "code": "PASTE_CODE_HERE",
    "redirect_uri": "PASTE_REDIRECT_URI"
  }'
```

### Postman

- Method: `POST`
- URL: `https://api.notion.com/v1/oauth/token`
- **Authorization** 탭 → Type: **Basic Auth** → Username=`CLIENT_ID`, Password=`CLIENT_SECRET`
- **Headers**: `Content-Type: application/json`
- **Body** (raw, JSON):

```json
{
  "grant_type": "authorization_code",
  "code": "PASTE_CODE_HERE",
  "redirect_uri": "PASTE_REDIRECT_URI"
}
```

### 응답 예시

```json
{
  "access_token": "secret_...",
  "refresh_token": "nrt_...",
  "bot_id": "00000000-0000-0000-0000-000000000000",
  "duplicated_template_id": null,
  "owner": { "type": "user", "user": { "...": "..." } },
  "workspace_icon": "...",
  "workspace_id": "...",
  "workspace_name": "..."
}
```

받은 값 중 아래를 `.env` 에 기록:

```
NOTION_API_KEY={access_token}
NOTION_OAUTH_CLIENT_ID={CLIENT_ID}
NOTION_OAUTH_CLIENT_SECRET={CLIENT_SECRET}
NOTION_OAUTH_REFRESH_TOKEN={refresh_token}
NOTION_OAUTH_REDIRECT_URI={REDIRECT_URI}
```

---

## Step 3 (선택) — access_token 만료 시 refresh

access_token 갱신이 필요하면 refresh_token 으로 새 쌍을 발급받는다.

### curl

```bash
BASIC=$(printf '%s:%s' "$CLIENT_ID" "$CLIENT_SECRET" | base64)

curl -X POST https://api.notion.com/v1/oauth/token \
  -H "Authorization: Basic $BASIC" \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "refresh_token",
    "refresh_token": "PASTE_REFRESH_TOKEN"
  }'
```

### 응답

```json
{
  "access_token": "secret_NEW...",
  "refresh_token": "nrt_NEW...",
  "bot_id": "...",
  "owner": { "type": "user", "user": { "...": "..." } },
  "workspace_id": "...",
  "workspace_name": "..."
}
```

> 새 refresh_token 이 발급되면 기존 refresh_token 은 무효가 된다.
> `.env` 의 `NOTION_OAUTH_REFRESH_TOKEN` 도 새 값으로 교체한다.

이 흐름은 `test_oauth_token.py` 의 O-2 항목이 자동 검증한다
(OAuth 환경변수가 모두 채워져 있을 때).

---

## 발급 후 검증

`.env` 에 `access_token` 만 넣었으면 곧바로 토큰 종류 식별:

```bash
uv run python test_oauth_token.py
```

`O-1 토큰 종류 식별` 항목이 `OAuth 2.0 access_token (user-authorized bot)` 으로
표시되면 정상적으로 OAuth 토큰이 연결된 것이다.

이후에는 P0/P1 스크립트가 Internal token 과 완전히 동일하게 동작한다:

```bash
uv run python test_p0_readonly.py
uv run python test_p1_readonly.py
```

---

## 보안 주의

- `CLIENT_SECRET`, `access_token`, `refresh_token` 은 절대 커밋하지 않는다 (`.gitignore` 됨).
- `.env` 는 로컬 전용. 공유 저장소에 올릴 때는 `.env.example` 만.
- `state` 를 사용해 CSRF 를 방지한다 (Step 1 에서 보낸 state 가 redirect 에 그대로 돌아와야 정상).
