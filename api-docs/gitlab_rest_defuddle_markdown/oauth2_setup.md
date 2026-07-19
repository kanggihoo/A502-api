# GitLab OAuth 2.0 초기 연동 및 토큰 획득 가이드



## 1단계: GitLab에 애플리케이션 등록

OAuth 2.0 흐름을 시작하려면 먼저 GitLab 계정에 애플리케이션을 등록하여 자격 증명(Client Credentials)을 획득해야 합니다.

1. **등록 페이지 이동:**
   GitLab 사용자 계정의 `/user_settings/applications` 페이지로 이동합니다.
2. **정보 입력:**
   * **Name:** 애플리케이션 이름
   * **Redirect URI:** 인증 성공 후 인증 코드를 전달받을 콜백 URL (개발 환경에서는 HTTP가 허용되나, 실제 서비스 환경에서는 반드시 HTTPS여야 함)
   * **Scopes (권한 범위):** 애플리케이션에 허용할 스코프를 활성화합니다.
     * API 호출 필요 시: `api` 또는 `read_user`
     * Git 저장소 접근 필요 시: `read_repository` 또는 `write_repository`
3. **자격 증명 발급 및 보관:**
   애플리케이션을 생성하면 다음 두 가지 정보를 획득하게 됩니다.
   * **Application ID (Client ID):** 애플리케이션 식별자 (외부 공개 가능)
   * **Client Secret (Client 비밀번호):** 인증 시 사용하는 보안 비밀키 (**절대 노출 금지 및 안전하게 저장**)

---

## 2단계: 인증 방식 선택 및 준비

애플리케이션의 아키텍처에 따라 적합한 OAuth 2.0 흐름을 선택하고 연동 준비를 합니다.

### A. PKCE 사용 권한 부여 코드 흐름 (싱글 페이지 앱/모바일 앱 권장)
*Client Secret*을 안전하게 숨길 수 없는 클라이언트 사이드 앱(예: React, Vue, iOS/Android 앱)에 사용합니다.

* **STATE 생성:** 요청과 콜백 간의 상태를 유지하고 CSRF 공격을 방지하기 위한 예측 불가능한 임의의 문자열.
* **CODE_VERIFIER 생성:** `A-Z`, `a-z`, `0-9`, `-`, `.`, `_`, `~` 문자로 구성된 43자~128자 사이의 임의 문자열.
* **CODE_CHALLENGE 생성:** `CODE_VERIFIER`를 SHA256 해싱(바이너리 포맷)한 후, URL-Safe Base64 인코딩한 문자열.
  * *Ruby 예시:* `Base64.urlsafe_encode64(Digest::SHA256.digest(CODE_VERIFIER), padding: false)`

### B. 일반 권한 부여 코드 흐름 (웹 백엔드 서버 앱 권장)
비밀 키(*Client Secret*)를 서버 측 환경 변수 등으로 안전하게 숨길 수 있는 전통적인 웹 애플리케이션에 사용합니다.

* **STATE 생성:** CSRF 방지용 임의의 문자열.

---

## 3단계: 권한 부여 코드(Authorization Code) 요청

사용자를 GitLab의 승인 페이지로 리다이렉트하여 인증 동의를 받고 코드를 전달받습니다.

### A. PKCE 사용 시 리다이렉트 URL
```plaintext
https://<gitlab-domain>/oauth/authorize?client_id=APP_ID&redirect_uri=REDIRECT_URI&response_type=code&state=STATE&scope=REQUESTED_SCOPES&code_challenge=CODE_CHALLENGE&code_challenge_method=S256
```

### B. 일반 흐름 리다이렉트 URL
```plaintext
https://<gitlab-domain>/oauth/authorize?client_id=APP_ID&redirect_uri=REDIRECT_URI&response_type=code&state=STATE&scope=REQUESTED_SCOPES
```

* **결과:** 사용자가 권한 승인 시, GitLab은 지정한 `REDIRECT_URI`로 인증 코드(`code`)와 요청 시 보냈던 `state`를 담아 리다이렉트합니다.
  ```plaintext
  https://example.com/oauth/redirect?code=RETURNED_CODE&state=STATE
  ```

---

## 4단계: 액세스 토큰(Access Token) 획득

전 단계에서 받은 인증 코드(`code`)를 사용하여 실제 API 호출과 Git 접근에 사용할 토큰을 요청합니다.

### A. PKCE 사용 시 토큰 요청 (POST)
* **Endpoint:** `https://<gitlab-domain>/oauth/token`
* **Parameters (Form Data):**
  ```plaintext
  client_id=APP_ID
  &code=RETURNED_CODE
  &grant_type=authorization_code
  &redirect_uri=REDIRECT_URI
  &code_verifier=CODE_VERIFIER
  ```

### B. 일반 흐름 토큰 요청 (POST)
* **Endpoint:** `https://<gitlab-domain>/oauth/token`
* **Parameters (Form Data):**
  ```plaintext
  client_id=APP_ID
  &client_secret=APP_SECRET
  &code=RETURNED_CODE
  &grant_type=authorization_code
  &redirect_uri=REDIRECT_URI
  ```

### 성공 응답 예시 (JSON)
요청 성공 시 사용 기한이 제한된 액세스 토큰과 토큰 갱신을 위한 리프레시 토큰이 반환됩니다.
```json
{
 "access_token": "ACCESS_TOKEN_STRING",
 "token_type": "bearer",
 "expires_in": 7200,
 "refresh_token": "REFRESH_TOKEN_STRING",
 "created_at": 1607635748
}
```

---

## 5단계: 획득한 토큰 활용

발급받은 `access_token`을 활용하여 GitLab 서비스에 접근합니다.

### A. GitLab REST API 호출
* **Authorization 헤더 사용 (권장):**
  ```shell
  curl --header "Authorization: Bearer <ACCESS_TOKEN>" \
       --url "https://<gitlab-domain>/api/v4/user"
  ```
* **Query Parameter 사용:**
  ```plaintext
  GET https://<gitlab-domain>/api/v4/user?access_token=<ACCESS_TOKEN>
  ```

### B. HTTPS를 통해 Git 저장소 접근 (Clone / Push / Pull)
* `read_repository` 혹은 `write_repository` 스코프가 있는 토큰을 사용합니다.
* Username은 `oauth2`로 지정하고, Password 자리에 발급받은 `access_token`을 입력합니다.
  ```plaintext
  https://oauth2:<ACCESS_TOKEN>@<gitlab-domain>/<project_path>/<project_name>.git
  ```
