---
title: "Mattermost에서 OAuth 2.0 사용하기"
source: "https://developers.mattermost.com/integrate/apps/authentication/oauth2/"
created: 2026-07-19
description: "OAuth 2.0은 외부 애플리케이션으로부터 들어오는 API 요청을 Mattermost가 승인할 수 있도록 지원하는 프로토콜입니다."
---

권한 부여(Authorization)를 통해 다음과 같은 기능을 사용할 수 있습니다:

- Mattermost 서버에 계정이 있는 사용자가 제3자(Third-party) 애플리케이션에 로그인할 수 있습니다. 기능을 테스트해 보려면 [Mattermost용 OAuth2 클라이언트 샘플 애플리케이션](https://github.com/enahum/mattermost-oauth2-client-sample)을 확인하세요.
- Mattermost 서버가 제3자 API에 대한 요청을 인증할 수 있습니다. 대표적인 애플리케이션으로 Zapier 연동이 있으며, 이를 통해 OAuth 2.0을 거쳐 700개 이상의 애플리케이션을 Mattermost와 연동할 수 있습니다. 자세한 내용은 [Zapier 문서](https://developers.mattermost.com/integrate/zapier-integration/)를 참조하세요.

## 클라이언트 타입 이해하기

Mattermost는 [RFC 6749](https://tools.ietf.org/html/rfc6749)에 정의된 두 가지 유형의 OAuth 2.0 클라이언트를 지원합니다:

### 기밀 클라이언트 (Confidential clients)

- **인증 방식**: 안전하게 보관해야 하는 `client_secret`을 가집니다.
- **사용 사례**: 서버 사이드 애플리케이션, 신뢰할 수 있는 백엔드.
- **토큰 엔드포인트 인증 방법**: `client_secret_post`
- **생성 방식**: UI(기본값) 또는 동적 클라이언트 등록(DCR, Dynamic Client Registration)을 통해 생성.
- **보안**: 서버 측에 자격 증명(credentials)을 안전하게 저장할 수 있습니다.

### 공개 클라이언트 (Public clients)

- **인증 방식**: `client_secret`이 없습니다 (인증 방법 `none` 사용).
- **사용 사례**: 싱글 페이지 애플리케이션(SPA), 모바일 앱, 브라우저 기반 앱 등 자격 증명을 안전하게 저장할 수 없는 환경.
- **보안**: 권한 부여 코드 흐름(Authorization Code Flow) 사용 시 **반드시 PKCE를 사용해야 합니다**.
- **토큰 엔드포인트 인증 방법**: `none`
- **생성 방식**: API 호출 시 `is_public: true` 매개변수를 전달하거나, DCR 사용 시 `token_endpoint_auth_method: "none"`으로 설정하여 생성.
- **제한 사항**: 리프레시 토큰(Refresh Token)을 받지 못하며, 액세스 토큰(Access Token)만 발급받습니다.

## Mattermost에 애플리케이션 등록하기

애플리케이션이 Mattermost에 대한 API 호출을 인증하고, Mattermost가 애플리케이션의 API 요청을 승인할 수 있도록 하려면 Mattermost에 애플리케이션을 등록해야 합니다. 이를 통해 OAuth 2.0 자격 증명(기밀 클라이언트의 경우 Client ID 및 Secret, 공개 클라이언트의 경우 Client ID만)을 생성하게 됩니다.

OAuth 2.0을 사용하여 Zapier 연동을 구성하려는 경우, [Zapier 문서](https://developers.mattermost.com/integrate/zapier-integration/)를 참조하세요.

### OAuth 2.0 애플리케이션 활성화하기

OAuth 2.0 애플리케이션 기능은 기본적으로 비활성화되어 있으며, 시스템 관리자가 다음과 같이 활성화할 수 있습니다:

1. 시스템 관리자 계정으로 Mattermost 서버에 로그인합니다.
2. **System Console > Integrations > Integration Management**로 이동합니다.
3. [Enable OAuth 2.0 Service Provider](https://docs.mattermost.com/administration/config-settings.html#enable-oauth-2-0-service-provider) 설정을 **True**로 변경합니다.
4. (선택 사항) 외부 애플리케이션이 사용자 이름과 프로필 사진을 지정하여 메시지를 게시할 수 있도록 허용하려면, [Enable integrations to override usernames](https://docs.mattermost.com/configure/configuration-settings.html#enable-integrations-to-override-usernames) 및 [Enable integrations to override profile picture icons](https://docs.mattermost.com/configure/configuration-settings.html#enable-integrations-to-override-profile-picture-icons) 설정을 **True**로 변경합니다.
5. (선택 사항) 시스템 관리자가 아닌 일반 사용자도 OAuth 2.0 애플리케이션을 생성할 수 있도록 허용하려면, [Restrict managing integrations to Admins](https://docs.mattermost.com/administration/config-settings.html#restrict-managing-integrations-to-admins) 설정을 **False**로 변경합니다.
6. (선택 사항) 동적 클라이언트 등록(Dynamic Client Registration)을 활성화하려면, **System Console > Integrations > Integration Management**에서 **Enable Dynamic Client Registration**을 **True**로 변경합니다. 중요한 보안 고려 사항은 [동적 클라이언트 등록](#동적-클라이언트-등록-dynamic-client-registration) 섹션을 참조하세요.

### OAuth 2.0 애플리케이션 등록하기

1. **Product menu > Integrations**로 이동합니다.
2. **OAuth 2.0 Applications**를 선택한 후, **Add OAuth 2.0 Application**을 선택합니다.
3. **Is Trusted** 설정: **Yes**로 설정하면 Mattermost에서 해당 애플리케이션을 신뢰할 수 있는 앱으로 간주합니다. 이 경우 사용자가 해당 제3자 애플리케이션에 로그인할 때 별도의 승인(승낙) 과정을 거치지 않습니다. **No**로 설정하면 사용자가 처음 로그인할 때 권한 승인 또는 거부를 선택할 수 있는 안내 페이지가 표시됩니다.
   * *오직 시스템 관리자만 OAuth 2.0 애플리케이션을 신뢰할 수 있는 앱(Trusted)으로 설정할 수 있습니다.*
4. **Is Public Client** 설정: **Yes**로 설정하면 싱글 페이지 애플리케이션(SPA)이나 모바일 앱 등을 위한 공개 클라이언트로 등록됩니다. 공개 클라이언트는 Client Secret을 받지 못하며, 권한 부여 코드 흐름에 반드시 PKCE를 사용해야 합니다. **No**(기본값)로 설정하면 Client Secret을 가진 기밀 클라이언트로 등록됩니다.
5. **Display Name** 지정: 최대 64자의 애플리케이션 이름을 입력합니다. 이 이름은 사용자가 권한을 부여할 때, **Settings > Security > OAuth 2.0 Applications**에서 승인된 앱 목록을 볼 때, 그리고 **Integrations** 메뉴에서 OAuth 2.0 애플리케이션 목록을 볼 때 표시됩니다.
6. **Description** 추가: 애플리케이션에 대한 짧은 설명입니다. 사용자가 **Settings > Security > OAuth 2.0 Applications**에서 승인된 앱 목록을 볼 때 이 설명이 표시됩니다.
7. **Homepage** 지정: OAuth 2.0 애플리케이션의 홈 페이지 주소입니다. 사용자가 앱 페이지에 방문하여 기능을 더 자세히 알아볼 수 있도록 돕습니다. URL은 유효해야 하며, 서버 구성에 따라 `http://` 또는 `https://`로 시작해야 합니다.
8. (선택 사항) **Icon URL** 추가: 사용자가 **Settings > Security > OAuth 2.0 Applications** 및 **Integrations** 메뉴에서 애플리케이션 목록을 볼 때 표시될 이미지입니다. 유효한 URL이어야 하며, `http://` 또는 `https://`로 시작해야 합니다.
9. **Callback URLs** 추가: 사용자가 애플리케이션의 권한을 승인하거나 거부한 후 Mattermost가 리다이렉트할 URL입니다. 이 URL은 인증 코드나 액세스 토큰을 처리하는 유일한 경로가 됩니다. 두 개 이상의 URL을 지정한 경우 사용자는 초기 인증에 사용된 URL로 리다이렉트됩니다. 각 URL은 서로 다른 줄에 작성되어야 하며, `http://` 또는 `https://`로 시작해야 합니다.
10. **Save**를 클릭하여 애플리케이션을 생성합니다.
    ![image](https://developers.mattermost.com/integrate/apps/authentication/oauth2/oauth2_app_screen.png)
11. 생성이 완료되면 **Client ID**, **Client Secret**, 그리고 승인된 리다이렉트 URL들이 표시됩니다. 이 값들을 복사하여 Mattermost와 연동할 애플리케이션에 입력하세요.
    ![image](https://developers.mattermost.com/integrate/apps/authentication/oauth2/oauth2_confirmation_screen.png)

## 애플리케이션에 권한 부여하기

OAuth 2.0 애플리케이션을 생성하고 나면, Mattermost 서버의 모든 사용자가 자동으로 해당 앱에 접근할 수 있게 됩니다.

애플리케이션은 앱을 등록한 사용자의 권한을 자동으로 이어받지 않습니다. 권한은 실제로 OAuth 흐름을 거쳐 인증을 완료한 개별 사용자(앱 등록자 또는 시스템의 다른 모든 사용자)의 권한을 기반으로 작동합니다.

애플리케이션이 Mattermost 서버에 신뢰할 수 있는(Trusted) OAuth 2.0 앱으로 등록된 경우 사용자의 추가 권한 승인이 필요하지 않습니다. 그렇지 않은 경우, 사용자가 처음 앱을 로그인하여 인증할 때 권한 승인 또는 거부를 선택하는 페이지가 나타납니다.

사용자가 승인하면 애플리케이션은 해당 사용자를 대신하여 요청을 보낼 수 있는 액세스 토큰을 받습니다. 이후 애플리케이션은 해당 사용자가 권한을 가진 모든 작업을 수행할 수 있습니다.

사용자는 **Settings > Security > OAuth 2.0 Applications**에서 승인된 앱 목록을 확인하고, 원할 경우 권한 부여를 취소할 수 있습니다.

## 지원하는 OAuth 흐름

Mattermost는 OAuth 2.0 애플리케이션을 위해 [권한 부여 코드(Authorization Code)](https://oauth.net/2/grant-types/authorization-code/) 및 [암시적(Implicit)](https://oauth.net/2/grant-types/implicit/) 승인 흐름을 지원합니다.

### 클라이언트 타입별 흐름 지원 여부

| 클라이언트 타입 | 권한 부여 코드 흐름 | 암시적 흐름 | PKCE 필수 여부 |
| --- | --- | --- | --- |
| 공개 클라이언트 | 지원됨 | 지원됨 | **필수** (코드 흐름에만 적용) |
| 기밀 클라이언트 | 지원됨 | 지원됨 **(권장하지 않음)** | 선택 사항 |

**주요 참고 사항:**

- 공개 클라이언트는 리프레시 토큰(Refresh Token) 승인 유형을 **사용할 수 없습니다**. 리프레시 토큰 없이 오직 액세스 토큰만 받습니다.
- 암시적 흐름에서는 PKCE가 필요하지 않습니다 (인증 코드 교환이 일어나지 않기 때문).
- 기밀 클라이언트는 선택적으로 PKCE를 사용할 수 있습니다. 만약 권한 부여 요청 시 `code_challenge`를 포함하여 흐름을 시작했다면, 이후 토큰 요청 단계에서도 PKCE 검증이 강제됩니다.

## PKCE (Proof Key for Code Exchange)

[PKCE (RFC 7636)](https://tools.ietf.org/html/rfc7636)는 인증 코드 가로채기 공격을 방지하는 보안 확장 프로토콜입니다. Client Secret을 안전하게 보관할 수 없는 싱글 페이지 애플리케이션(SPA)이나 모바일 앱과 같은 공개 클라이언트에 특히 중요합니다.

### PKCE가 필수인 경우

- **공개 클라이언트**: 권한 부여 코드 흐름을 사용할 때 **반드시** PKCE를 사용해야 합니다. Mattermost 서버는 PKCE 매개변수가 포함되지 않은 공개 클라이언트의 권한 부여 요청을 거부합니다.
- **기기/기밀 클라이언트**: PKCE 사용은 선택 사항입니다. 단, 권한 부여 요청에 PKCE 매개변수를 포함했다면, 토큰 요청 시에도 PKCE 흐름을 완료해야 합니다.

### PKCE 작동 방식

PKCE는 OAuth 흐름에 다음 두 가지 매개변수를 추가합니다:

1. **권한 부여 요청 (Authorization request)**: `code_challenge`(해싱된 값)와 `code_challenge_method`를 포함합니다 (Mattermost는 `S256`만 지원합니다).
2. **토큰 요청 (Token request)**: `code_verifier`(해싱하기 전의 원본 값)를 포함합니다.

서버는 `code_verifier`가 원래의 `code_challenge`와 일치하는지 검증함으로써, 권한 부여를 시작한 클라이언트와 완료하려는 클라이언트가 동일한지 확인합니다.

## 동적 클라이언트 등록 (Dynamic Client Registration)

동적 클라이언트 등록(DCR)을 사용하면 애플리케이션이 시스템 관리자의 수동 구성 없이도 프로그래밍 방식으로 OAuth 클라이언트를 등록할 수 있습니다. 이는 [RFC 7591](https://tools.ietf.org/html/rfc7591)을 준수합니다.

### DCR 활성화하기

DCR은 기본적으로 비활성화되어 있으며, 시스템 관리자가 다음과 같이 활성화할 수 있습니다:

1. **System Console > Integrations > Integration Management**로 이동합니다.
2. **Enable Dynamic Client Registration** 설정을 **True**로 변경합니다.

### DCR 사용하기

기능이 활성화되면 애플리케이션은 등록 엔드포인트(`/api/v4/oauth/apps/register`)로 요청을 보내 자신을 공개 또는 기밀 클라이언트로 등록할 수 있습니다. 애플리케이션은 리다이렉트 URI와 인증 방법을 지정하여 등록을 수행합니다:

- `token_endpoint_auth_method: "none"`으로 설정 시: Client Secret이 없는 공개 클라이언트 생성
- `token_endpoint_auth_method: "client_secret_post"`로 설정 시: Client Secret이 포함된 기밀 클라이언트 생성

### 메타데이터 검색 (Discovery Endpoint)

Mattermost는 `/.well-known/oauth-authorization-server` 주소에서 [OAuth 2.0 Authorization Server Metadata](https://tools.ietf.org/html/rfc8414) 엔드포인트를 제공하여, DCR의 활성화 여부 및 지원되는 인증 방식 등 서버의 기능을 외부에 공시합니다.

## 리프레시 토큰 (Refresh tokens)

**기밀 클라이언트**는 리프레시 토큰을 받으며, 이를 사용하여 새로운 액세스 토큰을 획득할 수 있습니다. **공개 클라이언트**는 보안상의 이유로 리프레시 토큰을 받지 못합니다.

## OAuth 엔드포인트

- 권한 부여 URI (Authorize URI): `/oauth/authorize`
- 토큰 URI (Token URI): `/oauth/access_token`
- 사용자 정보 URI (User info URI): `/api/v4/users/me`

## 애플리케이션 삭제하기

애플리케이션을 삭제하면 모든 사용자의 접근 권한이 취소됩니다. 애플리케이션을 생성한 사용자와 시스템 관리자만 애플리케이션을 삭제할 수 있습니다.
