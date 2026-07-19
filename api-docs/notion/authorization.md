---
title: "권한 부여 (Authorization)"
source: "https://developers.notion.com/guides/get-started/authorization"
created: 2026-07-19
description: "이 가이드는 Notion 커넥션 및 개인 액세스 토큰에 대한 권한 부여 흐름을 설명합니다."
---
## 권한 부여(Authorization)란 무엇인가요?

권한 부여는 커넥션이나 토큰에 Notion 데이터에 접근할 수 있는 권한을 부여하는 프로세스입니다. [내부 커넥션(Internal connections)](https://developers.notion.com/guides/get-started/internal-connections)은 정적 API 토큰을 사용하고, [개인 액세스 토큰(personal access tokens)](https://developers.notion.com/guides/get-started/personal-access-tokens)은 사용자 범위의 정적 API 토큰을 사용하며, [공개 커넥션(public connections)](https://developers.notion.com/guides/get-started/public-connections)은 [OAuth 2.0](https://oauth.net/2/) 프로토콜을 사용합니다.

## 내부 커넥션 인증 흐름 설정

내부 커넥션을 사용하려면 먼저 [개발자 포털(Developer portal)](https://app.notion.com/developers/connections)에서 커넥션을 생성해야 합니다.

내부 커넥션은 선택한 워크스페이스와 연결됩니다. 커넥션을 생성하려면 워크스페이스 소유자여야 합니다.

![](https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/docs/fd25d1f-integrations_7.png?w=2500&fit=max&auto=format&n=kSI9TVzPayvF1_1o&q=85&s=a3d54f2aa4e0405039a9a88ac58733db)

개발자 포털에서 새 커넥션을 생성합니다.

커넥션이 생성되면 `Configuration` 탭에서 필요한 설정을 업데이트할 수 있으며, 이 탭에서 설치 액세스 토큰(installation access token)을 가져올 수 있습니다.

설치 액세스 토큰은 REST API 요청을 인증하는 데 사용됩니다. 커넥션은 모든 API 요청에 동일한 토큰을 전송합니다.

![](https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/69c7487-integrations_8.png?w=2500&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=2cfdc4db42a0f68849cefb49df7d7b84)

Configuration 탭에서 설치 액세스 토큰을 찾습니다.

### 커넥션 권한

커넥션이 Notion 워크스페이스 페이지와 상호 작용하려면 먼저 해당 페이지를 커넥션과 수동으로 공유해야 합니다. 페이지를 커넥션과 공유하려면, Notion 워크스페이스에서 해당 페이지로 이동하여 우측 상단의 ••• 메뉴를 클릭하고 `커넥션 추가(Add connections)`까지 아래로 스크롤한 다음, 검색창을 사용하여 드롭다운 목록에서 커넥션을 찾아 선택합니다.

커넥션이 공유되면 API 요청을 보낼 수 있습니다. 페이지가 공유되지 않은 경우, API 요청 시 에러 응답이 반환됩니다.

**설치 액세스 토큰을 절대 공유하지 마세요**

설치 액세스 토큰은 보안 비밀 정보입니다. 커넥션 보안을 유지하려면 토큰을 소스 코드에 저장하거나 버전 관리 시스템(Git 등)에 커밋하지 마세요. 대신 환경 변수에서 토큰을 읽어오도록 구성하세요. 보안 비밀 관리자(Secret Manager)나 배포 시스템을 사용하여 환경 변수에 토큰을 설정하는 것을 권장합니다.

[자세히 알아보기: API 키 처리를 위한 모범 사례](https://developers.notion.com/guides/get-started/handling-api-keys)

### 내부 커넥션으로 API 요청 보내기

커넥션이 워크스페이스와 상호 작용할 때마다 모든 API 요청의 `Authorization` 헤더에 설치 액세스 토큰을 포함해야 합니다. 그러나 Notion의 [JavaScript용 SDK](https://github.com/makenotion/notion-sdk-js)를 사용하여 REST API와 상호 작용하는 경우, 클라이언트를 초기화할 때 토큰이 한 번만 설정됩니다.

```http
GET /v1/pages/b55c9c91-384d-452b-81db-d1ef79372b75 HTTP/1.1
Authorization: Bearer {INTEGRATION_TOKEN}
```

```javascript
const { Client } = require("@notionhq/client")

// 클라이언트 초기화
const notion = new Client({
    auth: process.env.NOTION_TOKEN,
})

const getUsers = async () => {
    const listUsersResponse = await notion.users.list({})
}
```

[JavaScript용 Notion SDK](https://github.com/makenotion/notion-sdk-js)를 사용하지 않는 경우, 모든 요청에 다음과 같이 [`Notion-Version`](https://developers.notion.com/reference/versioning) 및 [`Content-type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) 헤더도 함께 설정해야 합니다:

JSON

```json
headers: {
  Authorization: `Bearer ${process.env.NOTION_TOKEN}`,
  "Notion-Version": "2026-03-11",
  "Content-Type": "application/json",
}
```

API로부터 에러 응답을 받으면 커넥션이 페이지에 제대로 [추가되었는지](https://www.notion.com/help/add-and-manage-connections-with-the-api#manage-connections-in-your-workspace) 확인하세요. 그래도 문제가 해결되지 않으면 [상태 코드(Status codes)](https://developers.notion.com/reference/status-codes) 페이지에서 자세한 정보를 참조하세요.

## 개인 액세스 토큰(PAT) 인증 흐름 설정

개인 액세스 토큰(PAT, Personal Access Tokens)은 Notion 사용자가 [개발자 포털](https://www.notion.so/developers)에서 직접 생성합니다. OAuth 흐름이나 페이지 선택 창(page picker)이 없습니다. PAT는 토큰을 생성한 사용자로 동작하며, 선택한 워크스페이스에서 해당 사용자의 권한을 그대로 사용합니다.

스크립트, CLI 워크플로우, Worker 또는 신뢰할 수 있는 도구가 본인 계정으로 동작해야 할 때 PAT를 사용하세요. 팀 소유의 워크스페이스 자동화에는 내부 커넥션을 사용하고, 다른 Notion 사용자가 여러분의 앱을 설치해야 하는 경우에는 공개 커넥션을 사용하세요.

PAT는 다른 Notion API 토큰과 동일한 `Authorization` 헤더를 사용합니다:

```http
GET /v1/users/me HTTP/1.1
Authorization: Bearer {PERSONAL_ACCESS_TOKEN}
Notion-Version: 2026-03-11
```

생성 단계, 워크스페이스 관리자 제어 기능, 티어 기본값 및 보안 가이드는 [개인 액세스 토큰](https://developers.notion.com/guides/get-started/personal-access-tokens)을 참조하세요.

## 공개 커넥션 인증 흐름 설정

공개 커넥션은 생성 시 선택한 [설치 범위(installation scope)](https://developers.notion.com/guides/get-started/public-connections#installation-scope)(모든 워크스페이스 또는 특정 워크스페이스 세트) 내의 모든 Notion 워크스페이스에 설치할 수 있습니다.

공개 커넥션은 단일 설치 액세스 토큰을 가진 단일 워크스페이스에 종속되지 않으므로, 대신 [OAuth 2.0 프로토콜](https://oauth.net/2/)을 준수하여 워크스페이스와의 상호 작용 권한을 부여받습니다.

### 공개 커넥션 만드는 방법

[개발자 포털](https://app.notion.com/developers/connections)로 이동하여 새로운 공개 커넥션을 생성합니다.

OAuth 구성 섹션의 리다이렉트 URI와 커넥션의 [설치 범위(installation scope)](https://developers.notion.com/guides/get-started/public-connections#installation-scope)(**Any workspace(모든 워크스페이스)** 또는 **Selected workspaces only(선택한 워크스페이스만)** 중 하나)를 포함하여 커넥션 세부 정보를 입력합니다. 이 설정은 생성 후에는 변경할 수 없습니다.

리다이렉트 URI는 사용자가 공개 커넥션 권한을 승인한 후 이동하게 될 URI입니다. 자세히 알아보려면 [OAuth의 리다이렉트 URI 설명](https://www.oauth.com/oauth2-servers/redirect-uris/)을 읽어보세요.

마켓플레이스 목록 세부 정보(설명, 카테고리, 이미지 등)는 **Listings** 섹션을 통해 별도로 관리됩니다. 자세한 내용은 [마켓플레이스에 등록하기(List on the Marketplace)](https://developers.notion.com/guides/get-started/marketplace-listing) 가이드를 참조하세요.

### 공개 커넥션 권한 부여 개요

커넥션이 공개로 전환되면, 공개 인증 흐름을 사용하도록 커넥션 코드를 업데이트할 수 있습니다.

개요로서, 권한 부여 흐름은 다음 단계를 포함합니다. 각 단계는 아래에서 더 자세히 설명합니다.

### 1단계 - 사용자를 커넥션의 권한 부여 URL로 안내하기

[개발자 포털](https://app.notion.com/developers/connections)에서 공개 커넥션을 생성한 후, **Configuration** 탭에서 커넥션의 보안 비밀 정보(secrets)에 접근합니다. 내부 커넥션과 마찬가지로 이 값들은 보호되어야 하며 소스 코드나 버전 관리 시스템에 포함되어서는 안 됩니다.

![](https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/c535461-integrations_10.png?w=2500&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=9ed48b65c760339590d3eecb6299ee23)

공개 커넥션 검토 제출 후 권한 부여 URL(Authorization URL) 필드가 활성화됩니다.

예를 들어, 이러한 비밀 정보를 사용하는 `.env` 파일은 다음과 같을 수 있습니다:

```shellscript
#.env

OAUTH_CLIENT_ID=<your-client-id>
OAUTH_CLIENT_SECRET=<your-client-secret>
NOTION_AUTH_URL=<your-auth-url>
```

공개 커넥션의 권한 부여 흐름을 시작하려면, 사용자가 될 대상을 권한 부여 URL로 리다이렉트합니다. 일반적인 패턴은 Notion REST API와 상호 작용하는 커넥션 앱 내에 하이퍼링크를 포함하는 것입니다. 예를 들어, 사용자가 자신의 워크스페이스에 Notion 페이지를 생성할 수 있게 해주는 앱은 먼저 사용자를 권한 부여 URL로 보내야 합니다.

다음 예시는 하이퍼링크를 통해 제공되는 권한 부여 URL의 모습입니다:

```html
<a href="https://api.notion.com/v1/oauth/authorize?owner=user&client_id=463558a3-725e-4f37-b6d3-0889894f68de&redirect_uri=https%3A%2F%2Fexample.com%2Fauth%2Fnotion%2Fcallback&response_type=code">Add to Notion</a>
```

URL은 `https://api.notion.com/v1/oauth/authorize`로 시작하며 다음 매개변수를 가집니다:

| 매개변수 | 설명 | 필수 여부 |
| --- | --- | --- |
| `client_id` | 커넥션 설정에서 확인할 수 있는 커넥션 식별자입니다. | ✅ |
| `redirect_uri` | 액세스 권한을 부여한 후 사용자가 돌아올 URL입니다. | ✅ |
| `response_type` | 항상 `code`를 사용합니다. | ✅ |
| `owner` | 항상 `user`를 사용합니다. | ✅ |
| `state` | 사용자가 상호 작용 또는 작업 중에 있었던 경우, 사용자가 돌아온 후 상태를 복구하는 데 이 매개변수를 사용할 수 있습니다. 또한 CSRF 공격을 방지하는 데도 사용할 수 있습니다. |  |

권한 부여 URL에 접속하면, 커넥션에 Notion 템플릿 옵션이 포함되어 있는지 여부에 따라 사용자에게 서로 다른 화면이 표시됩니다.

#### 템플릿 옵션이 없는 표준 커넥션의 승인 화면 (기본값)

표준 커넥션 권한 흐름에서는 커넥션의 [기능(capabilities)](https://developers.notion.com/reference/capabilities)을 설명하는 화면이 표시되어, 커넥션이 워크스페이스에서 수행하고자 하는 작업 권한을 사용자에게 보여줍니다. 사용자는 액세스 권한을 부여할 페이지를 선택하거나 요청을 취소할 수 있습니다.

![](https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/docs/ec39f97-Screen_Shot_2021-07-22_at_2.58.28_PM.png?w=2500&fit=max&auto=format&n=kSI9TVzPayvF1_1o&q=85&s=18cb8d57b8f8093555222f83699a700a)

표준 커넥션 권한 부여를 위한 승인 화면 (템플릿 옵션 없음)

사용자가 **취소(Cancel)**를 누르면, `error` 쿼리 매개변수가 추가된 리다이렉트 URI로 이동합니다.

```text
www.example.com/my-redirect-uri?error=access_denied&state=
```

이 `error` 쿼리 매개변수를 사용하여 필요에 따라 앱의 상태를 조건부로 업데이트할 수 있습니다.

사용자가 `페이지 선택(Select pages)`을 선택하면 페이지 선택 창(page picker) 인터페이스가 열립니다. 사용자는 페이지 선택 창에서 커넥션과 공유할 페이지 및 데이터베이스를 검색하고 선택할 수 있습니다.

페이지 선택 창에는 사용자가 [모든 권한(full access)](https://www.notion.com/help/sharing-and-permissions)을 가진 페이지나 데이터베이스만 표시됩니다. 사용자가 리소스를 커넥션과 공유하려면 해당 리소스에 대한 모든 권한이 필요하기 때문입니다.

![](https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/a4009ce-Screen_Shot_2021-07-22_at_3.09.51_PM.png?w=2500&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=d8b29f9d96747e4e91e2a5608f611a1f)

페이지 선택 창 인터페이스

사용자는 본인이 사용할 수 있는 비공개 페이지와 공개 페이지를 모두 포함하여 커넥션에 액세스 권한을 줄 페이지를 선택할 수 있습니다. 상위 페이지를 선택하면 하위 페이지에 대한 액세스 권한도 자동으로 제공되므로 하위 페이지에 신속하게 권한을 줄 수 있습니다. 상황이 변경되면 사용자는 나중에 이 화면으로 다시 돌아와 액세스 설정을 업데이트할 수 있습니다.

사용자가 `액세스 허용(Allow access)`을 클릭하면, 임시 권한 부여 `code`와 함께 `redirect_uri`로 리다이렉트됩니다. 사용자가 액세스를 거부하면 `error` 쿼리 매개변수와 함께 `redirect_uri`로 리다이렉트됩니다.

사용자가 `액세스 허용(Allow access)`을 클릭했더라도 이후의 나머지 인증 흐름을 완료하지 않으면 커넥션은 선택된 페이지에 액세스할 수 *없습니다*.

#### Notion 템플릿 옵션이 있는 커넥션의 승인 화면

공개 커넥션은 인증 흐름 중에 템플릿으로 사용할 공개 Notion 페이지를 제공하는 옵션을 지원합니다.

워크스페이스에 템플릿을 추가하려면 다음 단계를 완료하세요:

- 사용자가 복제할 수 있도록 하고 싶은 워크스페이스 내의 공개 페이지를 선택합니다.
- [개발자 포털](https://app.notion.com/developers/connections)에서 해당 커넥션으로 이동하여 **Configuration** 탭을 열고, Basic information 섹션으로 스크롤합니다.
- 배포 설정의 맨 아래로 스크롤하여 **Notion URL for optional template** 입력창에 선택한 Notion 페이지의 URL을 추가합니다.

![](https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/b4ae671-integrations11.png?w=2500&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=f5cd7e893edd0864dc2aaaaef09cc031)

커넥션 설정의 Notion URL for optional template 입력창

이 URL이 추가되면 인증 흐름 승인 화면의 모습이 업데이트됩니다.

다시 안내 화면으로 돌아가서, 커넥션이 Notion 템플릿 옵션을 제공하는 경우 권한 흐름의 첫 단계에서는 커넥션의 [기능(capabilities)](https://developers.notion.com/reference/capabilities)을 설명합니다. 이는 커넥션이 워크스페이스에서 무엇을 할 수 있는지를 사용자에게 보여주며, 사용자에게 `다음(Next)`을 클릭하도록 안내합니다.

![](https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/77076c7-template_prompt1.png?w=2500&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=885dc89b073e5019cd12152a24e45550)

Notion 템플릿 옵션이 있는 커넥션의 승인 화면

다음 단계에서 사용자는 제공된 템플릿을 복제하거나, 커넥션과 공유할 기존 페이지를 직접 선택할 수 있습니다.

![](https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/9788bdb-template_prompt_2.png?w=2500&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=2ca3fc12da1dc649db7f8128100996bf)

사용자가 템플릿 복제를 선택하면 다음 작업이 자동으로 수행됩니다:

- 커넥션이 사용자의 워크스페이스에 추가됩니다.
- 템플릿이 워크스페이스에 새 페이지로 복제됩니다.
- 새 페이지가 커넥션과 공유됩니다.

사용자가 커넥션과 공유할 페이지를 선택하도록 결정하면, [표준 커넥션 승인 화면](#템플릿-옵션이-없는-표준-커넥션의-승인-화면-기본값)의 일부인 페이지 선택 창 인터페이스로 계속 진행합니다.

사용자가 공개 커넥션을 승인한 후에는 해당 사용자만 커넥션과 상호 작용하거나 페이지 및 데이터베이스를 공유할 수 있습니다. 내부 커넥션과 달리, 워크스페이스의 여러 멤버가 공개 커넥션을 사용하려는 경우 각 사용자는 커넥션에 대해 개별적으로 인증 흐름을 거쳐야 합니다.

**사용자 권한 부여 실패**

사용자 권한 부여 실패가 발생할 수 있습니다. 사용자가 요청을 `취소(Cancel)`하는 경우 실패가 트리거됩니다. 필요한 경우 이러한 케이스를 정상적으로 처리할 수 있도록 커넥션을 구축하세요.

일부 경우 Notion은 사용자를 공개 커넥션 생성 시 설정한 `redirect_uri`로 리다이렉트하며, 이때 `error` 쿼리 매개변수를 함께 보냅니다. Notion은 [OAuth 사양의 공통 에러 코드](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2.1)를 사용합니다. `error` 코드를 사용하여 사용자가 리다이렉트되었을 때 도움이 되는 메시지를 화면에 보여주도록 구현하세요.

### 2단계 - Notion이 사용자를 커넥션의 리다이렉트 URI로 리다이렉트하고 code 매개변수를 포함시킴

처음 공개 커넥션을 만들 때 리다이렉트 URI를 지정했습니다. 사용자가 화면의 안내에 따라 커넥션에 대한 `액세스 허용(Allow access)`을 완료하면, Notion은 임시 `code`를 생성하고 쿼리 스트링에 다음 정보를 포함하여 리다이렉트 URI로 요청을 보냅니다:

| 매개변수 | 설명 | 필수 여부 |
| --- | --- | --- |
| `code` | 임의의 임시 권한 부여 코드입니다. | ✅ |
| `state` | 사용자가 [액세스 요청을 받았을 때](#템플릿-옵션이-없는-표준-커넥션의-승인-화면-기본값) 커넥션이 제공한 값입니다. |  |

다음 단계를 완료하려면 리다이렉트에서 제공된 `code` 쿼리 매개변수를 가져옵니다. 가져오는 방법은 앱의 기술 스택에 따라 다릅니다.

예를 들어, React 컴포넌트에서는 `useRouter()` 훅을 통해 쿼리 매개변수를 사용할 수 있습니다:

```javascript
export default function AuthRedirectPage() {
  const router = useRouter();
  const { code } = router.query;
  ...
}
```

### 3단계 - Notion API에 POST 요청으로 code 전송하기

커넥션은 임시 `code`를 `access_token`으로 교환해야 합니다.

이 단계를 구성하려면 먼저 리다이렉트 URI에서 `code`를 가져옵니다.

그 다음, Notion의 토큰 엔드포인트인 [https://api.notion.com/v1/oauth/token](https://api.notion.com/v1/oauth/token)으로 `POST` 요청을 보내며 `code`를 함께 전송합니다.

이 엔드포인트는 API 레퍼런스 문서의 [토큰 생성(create a token)](https://developers.notion.com/reference/create-a-token) 부분에 더 자세히 설명되어 있습니다.

요청은 HTTP 기본 인증(Basic Authentication)을 사용하여 승인됩니다. 자격 증명은 커넥션의 `CLIENT_ID`와 `CLIENT_SECRET`을 다음과 같이 콜론으로 구분하여 결합한 값입니다:

```shellscript
CLIENT_ID:CLIENT_SECRET
```

이 두 값은 모두 [개발자 포털](https://app.notion.com/developers/connections)에서 찾을 수 있습니다.

[HTTP 기본 인증](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)에서는 자격 증명이 `Authorization` 헤더에 추가되기 전에 `base64`로 인코딩됩니다.

요청 본문에는 다음과 같은 JSON 인코딩 필드가 포함됩니다:

| 필드 | 타입 | 설명 | 필수 여부 |
| --- | --- | --- | --- |
| `"grant_type"` | `string` | 항상 `"authorization_code"`를 사용합니다. | ✅ |
| `"code"` | `string` | `"redirect_uri"`로 들어오는 요청에서 받은 임시 권한 부여 코드입니다. | ✅ |
| `"redirect_uri"` | `string` | 권한 부여 단계에서 제공되었던 `"redirect_uri"`입니다. | ✅/❌\*      \* 만약 리다이렉트 URI가 권한 부여 URL의 쿼리 매개변수로 제공되었거나, 커넥션 설정에 둘 이상의 리다이렉트 URI가 포함된 경우 이 필드는 필수입니다. 그렇지 않으면 허용되지 않습니다. 자세한 내용은 [토큰 생성 페이지](https://developers.notion.com/reference/create-a-token)를 참조하세요. |

다음은 권한 부여 코드를 액세스 토큰으로 교환하기 위한 요청 예시입니다:

```http
POST /v1/oauth/token HTTP/1.1
Authorization: Basic "$CLIENT_ID:$CLIENT_SECRET"
Content-Type: application/json

{"grant_type":"authorization_code","code":"e202e8c9-0990-40af-855f-ff8f872b1ec6", "redirect_uri":"https://example.com/auth/notion/callback"}
```

이 예제에 상응하는 Node.js 코드는 다음과 같습니다:

```javascript
...
const clientId = process.env.OAUTH_CLIENT_ID;
const clientSecret = process.env.OAUTH_CLIENT_SECRET;
const redirectUri = process.env.OAUTH_REDIRECT_URI;

// base64 인코딩
const encoded = btoa(`${clientId}:${clientSecret}`);

const response = await fetch("https://api.notion.com/v1/oauth/token", {
    method: "POST",
    headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: `Basic ${encoded}`,
},
    body: JSON.stringify({
        grant_type: "authorization_code",
        code: "your-temporary-code",
        redirect_uri: redirectUri,
    }),
});
...
```

### 4단계 - Notion이 access_token, refresh_token 및 추가 정보를 담아 응답함

Notion은 요청에 대해 `access_token`, `refresh_token` 및 추가 정보를 반환합니다. `access_token`은 이후의 Notion REST API 요청을 인증하는 데 사용됩니다. `refresh_token`은 액세스 토큰을 갱신하여 새로운 `access_token`을 생성하는 데 사용됩니다.

응답에는 다음과 같은 JSON 인코딩 필드가 포함됩니다:

| 필드 | 타입 | 설명 | Not null 여부 |
| --- | --- | --- | --- |
| `"access_token"` | `string` | Notion API에 대한 요청을 인증하는 데 사용되는 액세스 토큰입니다. | ✅ |
| `"refresh_token"` | `string` | 새로운 액세스 토큰을 생성하는 데 사용되는 리프레시 토큰입니다. | ✅ |
| `"bot_id"` | `string` | 이 권한 부여에 대한 식별자입니다. | ✅ |
| `"duplicated_template_id"` | `string` | 사용자의 워크스페이스에 생성된 새 페이지의 ID입니다. 새 페이지는 개발자가 커넥션과 함께 제공한 템플릿의 복사본입니다. 개발자가 템플릿을 제공하지 않은 경우 이 값은 `null`입니다. |  |
| `"owner"` | `object` | 이 커넥션을 보고 공유할 수 있는 사람에 대한 정보가 포함된 객체입니다. 커넥션을 승인한 사용자를 나타내는 [user 객체](https://developers.notion.com/reference/user)가 반환됩니다. | ✅ |
| `"workspace_icon"` | `string` | UI에서 이 권한 부여 정보를 표시할 때 사용할 수 있는 이미지 URL입니다. |  |
| `"workspace_id"` | `string` | 이 권한 부여가 발생한 워크스페이스의 ID입니다. | ✅ |
| `"workspace_name"` | `string` | UI에서 이 권한 부여 정보를 표시할 때 사용할 수 있는 이름(문자열)입니다. |  |

**토큰 요청 실패**

커넥션이 `code`를 `access_token`으로 교환하려고 할 때 문제가 발생하면, 응답 본문에 `"error"` 필드가 포함된 JSON이 반환됩니다. Notion은 [OAuth 사양의 공통 에러 코드](https://datatracker.ietf.org/doc/html/rfc6749#section-5.2)를 사용합니다.

### 5단계 - 커넥션이 향후 요청을 위해 access_token 및 refresh_token을 저장함

커넥션이 수신한 `access_token`과 `refresh_token`을 모두 저장할 수 있는 방법을 구성해야 합니다. `access_token`은 Notion API에 대해 인증된 요청을 하는 데 사용되며, `refresh_token`은 새로운 `access_token`을 생성하는 데 사용됩니다.

**토큰 저장 및 권한 사용을 위한 팁**

- 데이터베이스를 구축하는 것이 액세스 토큰을 저장하는 일반적인 솔루션입니다. 데이터베이스를 사용하는 경우 `access_token`, `refresh_token`, 그리고 커넥션이 해당 토큰으로 액세스하는 대응하는 Notion 리소스 간에 관계를 생성하세요. 예를 들어, Notion 데이터베이스나 페이지 ID를 저장하는 경우, 해당 레코드를 데이터베이스나 페이지 읽기/쓰기 요청 시 사용하는 올바른 `access_token` 및 지속적인 토큰 라이프사이클 관리를 위한 `refresh_token`과 연결해 둡니다.
- 커넥션이 `access_token` 및 `refresh_token`과 함께 받는 모든 정보를 저장하세요. UI나 제품 요구사항이 언제 변경되어 이 데이터가 필요할지 모르기 때문입니다. 정보를 다시 생성하기 위해 사용자에게 권한 부여 흐름을 다시 반복하도록 유도하는 것은 매우 어렵거나 불가능합니다.
- 토큰과 함께 반환되는 `bot_id`는 권한 부여에 대한 Notion 봇을 식별합니다. 성공적인 권한 부여 응답이 있을 때마다 토큰 쌍을 저장하세요. 여기에는 동일한 커넥션의 재승인도 포함되며, 이때 Notion은 새로운 `access_token`과 `refresh_token`을 반환할 수 있습니다.

### 6단계 - 액세스 토큰 갱신하기 (Refresh)

액세스 토큰을 갱신하면 새로운 액세스 토큰과 새로운 리프레시 토큰이 생성됩니다.

[4단계](#4단계---notion이-access_token-refresh_token-및-추가-정보를-담아-응답함)에서 제공받은 `refresh_token`을 Notion의 토큰 엔드포인트인 [https://api.notion.com/v1/oauth/token](https://api.notion.com/v1/oauth/token)으로 `POST` 요청에 담아 전송합니다.

이 엔드포인트는 API 레퍼런스 문서의 [토큰 갱신(refresh a token)](https://developers.notion.com/reference/refresh-a-token) 부분에 더 자세히 설명되어 있습니다.

요청은 HTTP 기본 인증(Basic Authentication)을 사용하여 승인됩니다. 자격 증명은 커넥션의 `CLIENT_ID`와 `CLIENT_SECRET`을 다음과 같이 콜론으로 구분하여 결합한 값입니다:

```shellscript
CLIENT_ID:CLIENT_SECRET
```

이 두 값은 모두 [개발자 포털](https://app.notion.com/developers/connections)에서 찾을 수 있습니다.

[HTTP 기본 인증](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)에서는 자격 증명이 `Authorization` 헤더에 추가되기 전에 `base64`로 인코딩됩니다.

요청 본문에는 다음과 같은 JSON 인코딩 필드가 포함됩니다:

| 필드 | 타입 | 설명 | 필수 여부 |
| --- | --- | --- | --- |
| `"grant_type"` | `string` | 항상 `"refresh_token"`을 사용합니다. | ✅ |
| `"refresh_token"` | `string` | 권한 부여 단계에서 반환받은 `"refresh_token"`입니다. | ✅ |

다음은 `refresh_token`을 새 액세스 토큰 및 새 리프레시 토큰으로 교환하기 위한 요청 예시입니다:

```http
POST /v1/oauth/token HTTP/1.1
Authorization: Basic "$CLIENT_ID:$CLIENT_SECRET"
Content-Type: application/json

{"grant_type":"refresh_token","refresh_token":"nrt_4991090011501Ejc6Xn4sHguI7jZIN449mKe9PRhpMfNK"}
```

이 예제에 상응하는 Node.js 코드는 다음과 같습니다:

```javascript
...
const clientId = process.env.OAUTH_CLIENT_ID;
const clientSecret = process.env.OAUTH_CLIENT_SECRET;

// base64 인코딩
const encoded = btoa(`${clientId}:${clientSecret}`);

const response = await fetch("https://api.notion.com/v1/oauth/token", {
    method: "POST",
    headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: `Basic ${encoded}`,
},
    body: JSON.stringify({
        grant_type: "refresh_token",
        refresh_token: "your-refresh-token",
    }),
});
...
```
