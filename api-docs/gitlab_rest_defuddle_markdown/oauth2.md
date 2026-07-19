

---
title: "OAuth 2.0 ID 제공자(identity provider) API"
source: "https://docs.gitlab.com/api/oauth2/"
created: 2026-07-19
description: "GitLab에 대한 제3자(Third-party) 인증."
---

이 API를 사용하여 제3자 서비스가 [OAuth 2.0](https://oauth.net/2/) 프로토콜을 통해 사용자의 GitLab 리소스에 액세스할 수 있도록 허용합니다. 자세한 내용은 [GitLab을 OAuth 2.0 인증 ID 제공자로 구성하기](https://docs.gitlab.com/integration/oauth_provider/)를 참조하세요.

이 기능은 [doorkeeper Ruby gem](https://github.com/doorkeeper-gem/doorkeeper)을 기반으로 합니다.

## 교차 출처 리소스 공유 (CORS)

많은 `/oauth` 엔드포인트가 교차 출처 리소스 공유(CORS)를 지원합니다. GitLab 15.1부터 다음 엔드포인트도 [CORS 프리플라이트(preflight) 요청](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)을 지원합니다:

- `/oauth/revoke`
- `/oauth/token`
- `/oauth/userinfo`

프리플라이트 요청에는 특정 헤더만 사용할 수 있습니다:

- [단순 요청(simple requests)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#simple_requests)에 나열된 헤더.
- `Authorization` 헤더.

예를 들어, `X-Requested-With` 헤더는 프리플라이트 요청에 사용할 수 없습니다.

## 지원되는 OAuth 2.0 흐름(Flow)

GitLab은 다음 인증 흐름을 지원합니다:

- **PKCE(Proof Key for Code Exchange)를 사용하는 권한 부여 코드(Authorization code)**: 가장 안전합니다. PKCE가 없으면 모바일 클라이언트에 클라이언트 암호(client secrets)를 포함해야 하므로, 클라이언트 및 서버 앱 모두에 권장됩니다.
- **권한 부여 코드(Authorization code)**: 안전하고 일반적인 흐름입니다. 안전한 서버 사이드 앱에 권장되는 옵션입니다.
- **기기 인증 권한 부여(Device Authorization Grant)** (GitLab 17.1 이상): 브라우저 액세스가 불가능한 기기를 대상으로 하는 안전한 흐름입니다. 인증 흐름을 완료하려면 보조 기기가 필요합니다.

[OAuth 2.1](https://oauth.net/2.1/) 드래프트 사양에서는 암시적 권한 부여(Implicit grant) 및 리소스 소유자 비밀번호 자격 증명(Resource Owner Password Credentials) 흐름이 명시적으로 제외되었습니다.

각 흐름의 작동 방식과 사용 사례에 맞는 적절한 흐름을 선택하려면 [OAuth RFC](https://www.rfc-editor.org/rfc/rfc6749)를 참조하세요.

권한 부여 코드(PKCE 사용 또는 미사용) 흐름을 사용하려면 먼저 사용자 계정의 `/user_settings/applications` 페이지를 통해 `application`(애플리케이션)을 등록해야 합니다. 등록하는 동안 적절한 스코프(scope)를 활성화하여 `application`이 액세스할 수 있는 리소스 범위를 제한할 수 있습니다. 생성되면 `application` 자격 증명인 *Application ID*와 *Client Secret*을 획득합니다. *Client Secret*은 **반드시 안전하게 보관해야 합니다**. 애플리케이션 아키텍처가 허용하는 경우 *Application ID*도 비밀로 유지하는 것이 유리합니다.

GitLab의 스코프 목록은 [ID 제공자 문서](https://docs.gitlab.com/integration/oauth_provider/#view-all-authorized-applications)를 참조하세요.

### CSRF 공격 방지

[리다이렉트 기반 흐름을 보호](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics-13#section-3.1)하기 위해, OAuth 사양에서는 `/oauth/authorize` 엔드포인트에 요청할 때마다 "사용자 에이전트에 안전하게 바인딩되는, state 매개변수에 포함된 일회용 CSRF 토큰"을 사용할 것을 권장합니다. 이를 통해 [CSRF 공격](https://wiki.owasp.org/index.php/Cross-Site_Request_Forgery_%28CSRF%29)을 방지할 수 있습니다.

### 프로덕션 환경에서 HTTPS 사용

프로덕션 환경에서는 `redirect_uri`에 HTTPS를 사용하세요. 개발 환경의 경우 GitLab은 비보안 HTTP 리다이렉트 URI를 허용합니다.

OAuth 2.0은 보안을 전적으로 전송 계층(transport layer)에 의존하므로 보호되지 않는 URI를 사용해서는 안 됩니다. 자세한 내용은 [OAuth 2.0 RFC](https://www.rfc-editor.org/rfc/rfc6749#section-3.1.2.1) 및 [OAuth 2.0 위협 모델 RFC](https://www.rfc-editor.org/rfc/rfc6819#section-4.4.2.1)를 참조하세요.

다음 섹션에서 각 흐름을 통해 권한을 부여받는 방법에 대한 자세한 지침을 확인할 수 있습니다.

### PKCE(Proof Key for Code Exchange)를 사용하는 권한 부여 코드(Authorization code)

[PKCE RFC](https://www.rfc-editor.org/rfc/rfc7636#section-1.1)에는 권한 부여 요청부터 액세스 토큰 획득까지의 세부 흐름 설명이 포함되어 있습니다. 다음 단계는 이 흐름의 GitLab 구현에 대해 설명합니다.

PKCE를 사용하는 권한 부여 코드 흐름(줄여서 PKCE 흐름)은 *Client Secret*에 대한 액세스 없이도 공개 클라이언트(public client)에서 액세스 토큰에 대한 클라이언트 자격 증명의 OAuth 교환을 안전하게 수행할 수 있도록 합니다. 이로 인해 PKCE 흐름은 단일 페이지 자바스크립트 애플리케이션(SPA)이나 사용자로부터 암호를 숨기는 것이 기술적으로 불가능한 기타 클라이언트 사이드 앱에 유리합니다.

흐름을 시작하기 전에 `STATE`, `CODE_VERIFIER` 및 `CODE_CHALLENGE`를 생성합니다.

- `STATE`: 요청과 콜백 간의 상태를 유지하기 위해 클라이언트가 사용하는 예측 불가능한 값입니다. CSRF 토큰으로도 사용해야 합니다.
- `CODE_VERIFIER`: `A-Z`, `a-z`, `0-9`, `-`, `.`, `_`, `~` 문자를 사용하는 43자에서 128자 사이의 임의의 문자열입니다.
- `CODE_CHALLENGE`: `CODE_VERIFIER` SHA256 해시의 URL-safe Base64 인코딩 문자열입니다.
	- SHA256 해시는 인코딩하기 전에 바이너리 형식이어야 합니다.
		- Ruby에서는 `Base64.urlsafe_encode64(Digest::SHA256.digest(CODE_VERIFIER), padding: false)`로 설정할 수 있습니다.
		- 참고로, `CODE_VERIFIER` 문자열 `ks02i3jdikdo2k0dkfodf3m39rjfjsdk0wk349rj3jrhf`를 이전 Ruby 스니펫을 사용하여 해시 및 인코딩하면 `CODE_CHALLENGE` 문자열 `2i0WFA-0AerkjQm4X4oDEhqA17QIAKNjXpagHBXmO_U`가 생성됩니다.

1. 권한 부여 코드를 요청합니다. 이를 위해 사용자를 다음과 같은 쿼리 매개변수와 함께 `/oauth/authorize` 페이지로 리다이렉션해야 합니다.
	```plaintext
	https://gitlab.example.com/oauth/authorize?client_id=APP_ID&redirect_uri=REDIRECT_URI&response_type=code&state=STATE&scope=REQUESTED_SCOPES&code_challenge=CODE_CHALLENGE&code_challenge_method=S256&root_namespace_id=ROOT_NAMESPACE_ID
	```
	이 페이지는 사용자에게 `REQUESTED_SCOPES`에 지정된 스코프를 기반으로 앱이 해당 계정에 액세스하도록 요청하는 것을 승인할지 묻습니다. 그 다음 사용자는 지정된 `REDIRECT_URI`로 다시 리다이렉션됩니다. [scope 매개변수](https://docs.gitlab.com/integration/oauth_provider/#view-all-authorized-applications)는 사용자와 관련된 스코프들의 공백으로 구분된 목록입니다. 예를 들어, `scope=read_user+profile`은 `read_user` 및 `profile` 스코프를 요청합니다. `root_namespace_id`는 프로젝트와 연결된 루트 네임스페이스 ID입니다. 이 선택적 매개변수는 연결된 그룹에 [SAML SSO](https://docs.gitlab.com/user/group/saml_sso/)가 구성되어 있을 때 사용해야 합니다. 리다이렉트에는 다음과 같이 권한 부여 코드(`code`)가 포함됩니다:
	```plaintext
	https://example.com/oauth/redirect?code=1234567890&state=STATE
	```
2. 이전 요청에서 반환된 권한 부여 코드(`code`)(다음 예제에서 `RETURNED_CODE`로 표시됨)를 사용하여 임의의 HTTP 클라이언트로 `access_token`을 요청할 수 있습니다. 다음 예제는 Ruby의 `rest-client`를 사용합니다:
	```ruby
	parameters = 'client_id=APP_ID&code=RETURNED_CODE&grant_type=authorization_code&redirect_uri=REDIRECT_URI&code_verifier=CODE_VERIFIER'
	RestClient.post 'https://gitlab.example.com/oauth/token', parameters
	```
	응답 예시:
	```json
	{
	 "access_token": "de6780bc506a0446309bd9362820ba8aed28aa506c71eedbe1c5c4f9dd350e54",
	 "token_type": "bearer",
	 "expires_in": 7200,
	 "refresh_token": "8257e65c97202ed1726cf9571600918f3bffb2544b26e00a61df9897668c33a1",
	 "created_at": 1607635748
	}
	```
3. 새로운 `access_token`을 가져오려면 `refresh_token` 매개변수를 사용합니다. 리프레시 토큰은 `access_token` 자체가 만료된 후에도 사용할 수 있습니다. 이 요청은 다음을 수행합니다:
	- 기존 `access_token` 및 `refresh_token`을 무효화합니다.
	- 응답에 새 토큰을 보냅니다.
	```ruby
	parameters = 'client_id=APP_ID&refresh_token=REFRESH_TOKEN&grant_type=refresh_token&redirect_uri=REDIRECT_URI'
	RestClient.post 'https://gitlab.example.com/oauth/token', parameters
	```
	응답 예시:
	```json
	{
	  "access_token": "c97d1fe52119f38c7f67f0a14db68d60caa35ddc86fd12401718b649dcfa9c68",
	  "token_type": "bearer",
	  "expires_in": 7200,
	  "refresh_token": "803c1fd487fec35562c205dac93e9d8e08f9d3652a24079d704df3039df1158f",
	  "created_at": 1628711391
	}
	```

> [!type-note] Type-note
> `redirect_uri`는 원래 권한 부여 요청에서 사용된 `redirect_uri`와 일치해야 합니다.

이제 액세스 토큰을 사용하여 API에 요청을 보낼 수 있습니다.

### 권한 부여 코드 흐름 (Authorization code flow)

> [!type-note] Type-note
> 상세한 흐름 설명은 [RFC 사양](https://www.rfc-editor.org/rfc/rfc6749#section-4.1)을 확인하세요.

권한 부여 코드 흐름은 기본적으로 [PKCE를 사용하는 권한 부여 코드 흐름](https://docs.gitlab.com/api/oauth2/#authorization-code-with-proof-key-for-code-exchange-pkce)과 동일합니다.

흐름을 시작하기 전에 `STATE`를 생성합니다. 이는 요청과 콜백 간의 상태를 유지하기 위해 클라이언트가 사용하는 예측 불가능한 값입니다. CSRF 토큰으로도 사용해야 합니다.

1. 권한 부여 코드를 요청합니다. 이를 위해 사용자를 다음과 같은 쿼리 매개변수와 함께 `/oauth/authorize` 페이지로 리다이렉션해야 합니다.
	```plaintext
	https://gitlab.example.com/oauth/authorize?client_id=APP_ID&redirect_uri=REDIRECT_URI&response_type=code&state=STATE&scope=REQUESTED_SCOPES&root_namespace_id=ROOT_NAMESPACE_ID
	```
	이 페이지는 사용자에게 `REQUESTED_SCOPES`에 지정된 스코프를 기반으로 앱이 해당 계정에 액세스하도록 요청하는 것을 승인할지 묻습니다. 그 다음 사용자는 지정된 `REDIRECT_URI`로 리다이렉션됩니다. [scope 매개변수](https://docs.gitlab.com/integration/oauth_provider/#view-all-authorized-applications)는 사용자와 관련된 스코프들의 공백으로 구분된 목록입니다. 예를 들어, `scope=read_user+profile`은 `read_user` 및 `profile` 스코프를 요청합니다. `root_namespace_id`는 프로젝트와 연결된 루트 네임스페이스 ID입니다. 이 선택적 매개변수는 연결된 그룹에 [SAML SSO](https://docs.gitlab.com/user/group/saml_sso/)가 구성되어 있을 때 사용해야 합니다. 리다이렉트에는 권한 부여 코드(`code`)가 포함됩니다. 예:
	```plaintext
	https://example.com/oauth/redirect?code=1234567890&state=STATE
	```
2. 이전 요청에서 반환된 권한 부여 코드(`code`)(다음 예제에서 `RETURNED_CODE`로 표시됨)를 사용하여 임의의 HTTP 클라이언트로 `access_token`을 요청할 수 있습니다. 다음 예제는 Ruby의 `rest-client`를 사용합니다:
	```ruby
	parameters = 'client_id=APP_ID&client_secret=APP_SECRET&code=RETURNED_CODE&grant_type=authorization_code&redirect_uri=REDIRECT_URI'
	RestClient.post 'https://gitlab.example.com/oauth/token', parameters
	```
	응답 예시:
	```json
	{
	 "access_token": "de6780bc506a0446309bd9362820ba8aed28aa506c71eedbe1c5c4f9dd350e54",
	 "token_type": "bearer",
	 "expires_in": 7200,
	 "refresh_token": "8257e65c97202ed1726cf9571600918f3bffb2544b26e00a61df9897668c33a1",
	 "created_at": 1607635748
	}
	```
3. 새로운 `access_token`을 가져오려면 `refresh_token` 매개변수를 사용합니다. 리프레시 토큰은 `access_token` 자체가 만료된 후에도 사용할 수 있습니다. 이 요청은 다음을 수행합니다:
	- 기존 `access_token` 및 `refresh_token`을 무효화합니다.
	- 응답에 새 토큰을 보냅니다.
	```ruby
	parameters = 'client_id=APP_ID&client_secret=APP_SECRET&refresh_token=REFRESH_TOKEN&grant_type=refresh_token&redirect_uri=REDIRECT_URI'
	RestClient.post 'https://gitlab.example.com/oauth/token', parameters
	```
	응답 예시:
	```json
	{
	  "access_token": "c97d1fe52119f38c7f67f0a14db68d60caa35ddc86fd12401718b649dcfa9c68",
	  "token_type": "bearer",
	  "expires_in": 7200,
	  "refresh_token": "803c1fd487fec35562c205dac93e9d8e08f9d3652a24079d704df3039df1158f",
	  "created_at": 1628711391
	}
	```

> [!type-note] Type-note
> `redirect_uri`는 원래 권한 부여 요청에서 사용된 `redirect_uri`와 일치해야 합니다.

이제 반환된 액세스 토큰을 사용하여 API에 요청을 보낼 수 있습니다.

### 기기 인증 권한 부여 흐름 (Device authorization grant flow)

> [!type-note] Type-note
> 기기 권한 부여 요청부터 브라우저 로그인의 토큰 응답까지 기기 인증 권한 부여 흐름의 상세한 설명은 [RFC 사양](https://datatracker.ietf.org/doc/html/rfc8628#section-3.1)을 확인하세요.

기기 인증 권한 부여 흐름은 브라우저 상호 작용이 불가능하고 입력이 제한된 기기에서 GitLab 자격 증명을 안전하게 인증할 수 있도록 합니다.

따라서 기기 인증 권한 부여 흐름은 헤드리스 서버 또는 UI가 없거나 제한된 기기에서 GitLab 서비스를 사용하려는 사용자에게 이상적입니다.

1. 기기 권한 부여를 요청하기 위해, 입력이 제한된 기기 클라이언트에서 `https://gitlab.example.com/oauth/authorize_device`로 요청을 보냅니다. 예:
	```ruby
	parameters = 'client_id=UID&scope=read'
	RestClient.post 'https://gitlab.example.com/oauth/authorize_device', parameters
	```
	성공적인 요청 후, `verification_uri`가 포함된 응답이 사용자에게 반환됩니다. 예:
	```json
	{
	    "device_code": "GmRhmhcxhwAzkoEqiMEg_DnyEysNkuNhszIySk9eS",
	    "user_code": "0A44L90H",
	    "verification_uri": "https://gitlab.example.com/oauth/device",
	    "verification_uri_complete": "https://gitlab.example.com/oauth/device?user_code=0A44L90H",
	    "expires_in": 300,
	    "interval": 5
	}
	```
2. 기기 클라이언트는 응답의 `user_code`와 `verification_uri`를 요청한 사용자에게 보여줍니다. 그런 다음 사용자는 브라우저 액세스가 가능한 보조 기기에서 다음을 수행합니다:
	1. 제공된 URI로 이동합니다.
	2. 사용자 코드를 입력합니다.
	3. 안내에 따라 인증을 완료합니다.
3. `verification_uri`와 `user_code`를 표시한 직후, 기기 클라이언트는 초기 응답에서 반환된 관련 `device_code`를 사용하여 토큰 엔드포인트 폴링(polling)을 시작합니다:
	```ruby
	parameters = 'grant_type=urn:ietf:params:oauth:grant-type:device_code&device_code=GmRhmhcxhwAzkoEqiMEg_DnyEysNkuNhszIySk9eS&client_id=1406020730'
	RestClient.post 'https://gitlab.example.com/oauth/token', parameters
	```
4. 기기 클라이언트는 토큰 엔드포인트로부터 응답을 받습니다. 인증에 성공하면 성공 응답이 반환되고, 그렇지 않으면 에러 응답이 반환됩니다. 발생 가능한 에러 응답은 다음 중 하나로 분류됩니다:
	- OAuth 권한 부여 프레임워크 액세스 토큰 에러 응답에 정의된 것들.
	- 여기에 설명된 기기 인증 권한 부여 흐름과 관련된 것들.
	기기 흐름에 특화된 에러 응답은 다음과 같습니다. 각 에러 응답에 대한 자세한 내용은 [기기 인증 권한 부여 관련 RFC 사양](https://datatracker.ietf.org/doc/html/rfc8628#section-3.5) 및 [권한 부여 토큰 관련 RFC 사양](https://datatracker.ietf.org/doc/html/rfc6749#section-5.2)을 참조하세요.
	응답 예시:
	```json
	{
	  "error": "authorization_pending",
	  "error_description": "..."
	}
	```
	이 응답을 받으면 기기 클라이언트는 폴링을 계속합니다.
	폴링 간격이 너무 짧으면 slow down 에러 응답이 반환됩니다. 예:
	```json
	{
	  "error": "slow_down",
	  "error_description": "..."
	}
	```
	이 응답을 받으면 기기 클라이언트는 폴링 속도를 낮추고 새로운 속도로 폴링을 계속합니다.
	인증이 완료되기 전에 기기 코드가 만료되면 expired token 에러 응답이 반환됩니다. 예:
	```json
	{
	  "error": "expired_token",
	  "error_description": "..."
	}
	```
	이 시점에서 기기 클라이언트는 폴링을 중단하고 새로운 기기 권한 부여 요청을 시작해야 합니다.
	권한 부여 요청이 거부되면 access denied 에러 응답이 반환됩니다. 예:
	```json
	{
	  "error": "access_denied",
	  "error_description": "..."
	}
	```
	인증 요청이 거부되었습니다. 사용자는 자격 증명을 확인하거나 시스템 관리자에게 문의해야 합니다.
5. 사용자가 인증에 성공하면 성공 응답이 반환됩니다:
	```json
	{
	    "access_token": "TOKEN",
	    "token_type": "Bearer",
	    "expires_in": 7200,
	    "scope": "read",
	    "created_at": 1593096829
	}
	```

이 시점에서 기기 인증 흐름이 완료됩니다. 반환된 `access_token`을 GitLab에 제공하여 HTTPS를 통해 복제(clone)하거나 API에 액세스할 때와 같이 사용자의 신원을 인증할 수 있습니다.

클라이언트 측 기기 흐름을 구현한 예제 애플리케이션은 [https://gitlab.com/johnwparent/git-auth-over-https](https://gitlab.com/johnwparent/git-auth-over-https)에서 찾을 수 있습니다.

## 액세스 토큰으로 GitLab API 액세스

`access token`(액세스 토큰)을 사용하면 사용자를 대신하여 API에 요청할 수 있습니다. 토큰을 GET 매개변수로 전달할 수 있습니다:

```plaintext
GET https://gitlab.example.com/api/v4/user?access_token=<OAUTH-TOKEN>
```

또는 토큰을 Authorization 헤더에 넣을 수 있습니다:

```shell
curl --header "Authorization: Bearer <OAUTH-TOKEN>" \
  --url "https://gitlab.example.com/api/v4/user"
```

## 액세스 토큰으로 HTTPS를 통한 Git 액세스

[스코프](https://docs.gitlab.com/integration/oauth_provider/#view-all-authorized-applications)가 `read_repository` 또는 `write_repository`인 토큰은 HTTPS를 통해 Git에 액세스할 수 있습니다. 토큰을 비밀번호로 사용하세요. 사용자 이름은 임의의 문자열 값으로 설정할 수 있으나, `oauth2`를 사용해야 합니다:

```plaintext
https://oauth2:<your_access_token>@gitlab.example.com/project_path/project_name.git
```

또는 [Git 자격 증명 도우미(Git credential helper)](https://docs.gitlab.com/user/profile/account/two_factor_authentication/#oauth-credential-helpers)를 사용하여 OAuth로 GitLab에 인증할 수 있습니다. 이는 OAuth 토큰 갱신(refresh)을 자동으로 처리합니다.

## 토큰 정보 조회

토큰의 세부 정보를 확인하려면 Doorkeeper 젬이 제공하는 `token/info` 엔드포인트를 사용하세요. 자세한 내용은 [`/oauth/token/info`](https://github.com/doorkeeper-gem/doorkeeper/wiki/API-endpoint-descriptions-and-examples#get----oauthtokeninfo)를 참조하세요.

액세스 토큰을 다음 방법 중 하나로 제공해야 합니다:

- 매개변수로 제공:
	```plaintext
	GET https://gitlab.example.com/oauth/token/info?access_token=<OAUTH-TOKEN>
	```
- Authorization 헤더에 제공:
	```shell
	curl --header "Authorization: Bearer <OAUTH-TOKEN>" \
	  --url "https://gitlab.example.com/oauth/token/info"
	```

다음은 응답 예시입니다:

```json
{
    "resource_owner_id": 1,
    "scope": ["api"],
    "expires_in": null,
    "application": {"uid": "1cb242f495280beb4291e64bee2a17f330902e499882fe8e1e2aa875519cab33"},
    "created_at": 1575890427
}
```

### 지원 중단된(Deprecated) 필드

`scopes` 및 `expires_in_seconds` 필드는 응답에 포함되지만 현재 지원이 중단되었습니다. `scopes` 필드는 `scope` 필드의 앨리어스(별칭)이고, `expires_in_seconds` 필드는 `expires_in` 필드의 앨리어스입니다. 자세한 내용은 [Doorkeeper API 변경 사항](https://github.com/doorkeeper-gem/doorkeeper/wiki/Migration-from-old-versions#api-changes-5)을 참조하세요.

## 토큰 취소 (Revoke)

토큰을 취소하려면 `revoke` 엔드포인트를 사용하세요. API는 성공을 나타내기 위해 200 응답 코드와 빈 JSON 해시를 반환합니다.

```ruby
parameters = 'client_id=APP_ID&client_secret=APP_SECRET&token=TOKEN'
RestClient.post 'https://gitlab.example.com/oauth/revoke', parameters
```

## OAuth 2.0 토큰 및 GitLab 레지스트리

표준 OAuth 2.0 토큰은 다음과 같이 GitLab 레지스트리에 대해 다양한 수준의 액세스를 지원합니다:

- 사용자가 다음 레지스트리에 인증하는 것을 허용하지 않습니다:
	- GitLab [컨테이너 레지스트리(container registry)](https://docs.gitlab.com/user/packages/container_registry/authenticate_with_container_registry/).
	- GitLab [패키지 레지스트리(Package registry)](https://docs.gitlab.com/user/packages/package_registry/)에 나열된 패키지.
	- [가상 레지스트리(Virtual registries)](https://docs.gitlab.com/user/packages/virtual_registry/).
- 사용자가 [컨테이너 레지스트리 API](https://docs.gitlab.com/api/container_registry/)를 통해 레지스트리를 가져오고, 나열하고, 삭제하는 것을 허용합니다.
- 사용자가 [Maven 가상 레지스트리 API](https://docs.gitlab.com/api/maven_virtual_registries/)를 통해 레지스트리 객체를 가져오고, 나열하고, 삭제하는 것을 허용합니다.
