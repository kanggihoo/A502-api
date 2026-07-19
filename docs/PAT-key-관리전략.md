PAT를 받는 대시보드는 “사용자의 API 권한을 서버가 제한적으로 위임받아 대신 호출하는 서비스”로 설계해야 하며, 토큰은 브라우저가 아닌 백엔드에서만 암호화 보관해야 합니다.

## PAT 기반 통합 대시보드 보안 설계

### 1. 사용할 수 있는 자격증명

| 구분 | 사용 여부 | 이유 |
|---|---|---|
| GitLab/Jira/Mattermost API용 PAT | 가능 | 사용자 권한 범위에서 API 호출 |
| OAuth access/refresh token | 가능 | OAuth 앱 등록이 가능한 경우 더 권장 |
| SSAFY 비밀번호 | 금지 | 우리 서비스가 받아서는 안 됨 |
| SSO 세션 쿠키, SAML Response, 웹 로그인 JWT | 금지 | 해당 서비스 웹 로그인 전용 자격증명 |
| SSH 개인키 | 금지 | API 연동용으로 받으면 안 됨 |

PAT는 생성한 사용자의 권한을 상속하므로, 읽기 전용 최소 scope와 만료일을 설정해야 합니다. [GitLab 토큰 문서](https://docs.gitlab.com/security/tokens/)

### 2. 사용자 연결 흐름

```text
사용자 로그인
  → “GitLab 연결” 화면에서 PAT 입력
  → HTTPS POST로 백엔드에 전송
  → 백엔드가 GitLab API로 토큰 유효성·계정 확인
  → 즉시 암호화하여 DB 저장
  → 화면에는 “연결됨” 상태만 표시
```

- PAT는 URL query string이 아닌 HTTPS `POST` body로 받습니다.
- 토큰 입력 페이지에는 광고, 분석, 세션 녹화 등 제3자 스크립트를 넣지 않습니다.
- 브라우저 개발자 도구에서는 사용자가 자기 요청을 볼 수 있습니다. 이것을 숨기려 하지 말고, **PAT를 이후 브라우저에 다시 내려주지 않는 것**이 중요합니다.

### 3. 저장 방식

DB에는 PAT 원문이 아니라 암호문만 저장합니다.

```text
integration_credentials
- user_id
- provider              # gitlab, jira, mattermost 등
- token_ciphertext      # 암호화된 PAT
- nonce, auth_tag
- key_version
- scopes
- expires_at
- verified_at
- revoked_at
```

- AES-256-GCM 같은 인증 암호화로 PAT를 암호화합니다.
- 암호화 키는 DB·소스 코드·Git 저장소와 분리합니다.
- 운영 환경에서는 KMS/Key Vault/Vault 같은 키 관리 서비스를 사용합니다.
- 로그, 예외 메시지, APM, 백업, URL, 응답 JSON에 토큰 원문을 남기지 않습니다.
- 해싱은 적합하지 않습니다. API 호출에 원문이 필요하므로 **암호화**해야 합니다.

OWASP도 secret은 암호화하고, 키를 데이터와 분리하거나 envelope encryption을 사용하도록 권장합니다. [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

### 4. API 호출 구조

```text
브라우저 → 우리 백엔드: 대시보드 데이터 요청
우리 백엔드 → DB: 로그인한 사용자 PAT 암호문 조회
우리 백엔드 → GitLab: PAT를 헤더에 넣어 API 호출
우리 백엔드 → 브라우저: 필요한 결과만 반환
```

백엔드가 API 호출 직전에만 PAT를 복호화합니다.

```http
PRIVATE-TOKEN: <복호화한 사용자 PAT>
```

브라우저에는 GitLab PAT를 보내지 않습니다. 따라서 브라우저 Network 탭에는 사용자의 대시보드 요청만 보이고, 서버가 GitLab에 보내는 PAT는 보이지 않습니다.

### 5. 연결 상태와 해제

화면에는 토큰 원문 대신 상태만 보여줍니다.

```text
GitLab: 연결됨
계정: 사용자명
권한: 읽기 전용
만료일: YYYY-MM-DD
```

버튼은 구분합니다.

- `연결 해제`: 우리 DB의 암호문만 삭제합니다. GitLab PAT는 유지됩니다.
- `GitLab 토큰도 폐기`: 저장된 동일 PAT로 GitLab의 self-revoke API를 호출한 뒤 DB에서도 삭제합니다.

GitLab은 현재 PAT 자신을 revoke하는 `self` endpoint를 제공합니다. 별도의 revoke 전용 PAT를 만들 필요는 없습니다. 단, SSAFY GitLab의 버전·정책상 해당 API가 제한될 수 있으므로 실패 시 GitLab 설정 화면에서 직접 revoke하도록 안내합니다. [GitLab PAT revoke API](https://docs.gitlab.com/api/personal_access_tokens/)

### 6. 운영 원칙

- 사용자별·도구별로 credential을 분리합니다.
- 현재 로그인한 사용자 자신의 PAT만 조회·사용합니다.
- 최소 scope, 짧은 만료일, 만료 전 재연결 안내를 적용합니다.
- `401/403`이 반복되면 연결 만료/폐기 상태로 표시하고 재연결을 요구합니다.
- 관리자도 PAT 원문을 조회할 수 없게 설계합니다.
- SSAFY 및 각 도구의 제3자 토큰 보관·자동 호출 정책을 확인하고 사용자 동의를 받습니다.

## 최종 요약

PAT 기반 연동은 사용자에게 PAT를 한 번 입력받아, 백엔드가 암호화 저장 후 해당 사용자 범위에서만 API를 대신 호출하는 구조입니다. PAT는 브라우저에 재전달하지 않고, DB에는 암호문만 저장하며 암호화 키는 별도 KMS/Vault로 분리합니다. 기본 해제는 DB 토큰 삭제이고, 사용자가 원하면 저장된 같은 PAT로 원 서비스 토큰까지 revoke할 수 있습니다.
