---
title: "슬래시 명령어"
source: "https://developers.mattermost.com/integrate/slash-commands/"
created: 2026-07-20
description: "슬래시 명령어는 웹 서비스로 HTTP 요청을 트리거하며, 서비스는 이에 응답하여 하나 이상의 메시지를 게시할 수 있습니다."
---

[Mattermost v11.0이 출시되었습니다! 새로운 기능 알아보기 »](https://mattermost.com/blog/mattermost-v11-powering-more-mission-critical-collaboration/)

## Mattermost의 슬래시 명령어

슬래시 명령어는 `/`로 시작하는 메시지로, 웹 서비스로 HTTP 요청을 트리거하며 서비스는 이에 응답하여 하나 이상의 메시지를 게시할 수 있습니다.

슬래시 명령어에는 **자동 완성**이라는 추가 기능이 있어, 메시지 상자에 입력된 내용을 기반으로 가능한 명령어 목록을 표시합니다. 빈 메시지 상자에 `/`를 입력하면 모든 슬래시 명령어 목록이 표시됩니다. 메시지 상자에 슬래시 명령어를 입력하면 자동 완성이 명령어의 가능한 인수와 플래그도 표시합니다.

[발신 웹훅](https://developers.mattermost.com/integrate/webhooks/outgoing/)과 달리 슬래시 명령어는 공개 채널 외에도 비공개 채널 및 다이렉트 메시지에서 작동하며, 입력 시 자동 완성되도록 구성할 수 있습니다. Mattermost는 여러 [내장 슬래시 명령어](https://docs.mattermost.com/channels/interact-with-channels.html)를 포함하고 있습니다. 또한 [사용자 정의 슬래시 명령어](https://developers.mattermost.com/integrate/slash-commands/custom/)를 만들 수도 있습니다.

## 팁 및 모범 사례

1. 슬래시 명령어는 메시지를 쉽게 게시할 수 있도록 설계되었습니다. 채널 생성과 같은 다른 작업을 위해서는 [Mattermost API](https://api.mattermost.com/)도 함께 사용해야 합니다.
2. [Mattermost Server v5.0 이상](https://docs.mattermost.com/administration/important-upgrade-notes.html)을 실행하는 서버의 게시물 크기는 16383자로 제한됩니다. `extra_responses` 필드를 사용하여 트리거된 슬래시 명령어에 여러 개의 게시물로 응답할 수 있습니다.
3. [System Console > Integrations > Integration Management](https://docs.mattermost.com/configure/configuration-settings.html#enable-custom-slash-commands)에서 슬래시 명령어를 생성할 수 있는 사용자를 제한할 수 있습니다.
4. Mattermost [발신 웹훅](https://developers.mattermost.com/integrate/webhooks/outgoing/)은 Slack과 호환됩니다. Slack 발신 웹훅에 사용된 코드를 복사하여 Mattermost 통합을 만드는 데 사용할 수 있습니다. Mattermost는 [Slack의 독점 JSON 페이로드 형식을 자동으로 변환](https://developers.mattermost.com/integrate/slash-commands/slack/#translate-slacks-data-format-to-mattermost)합니다.
5. 외부 애플리케이션은 모든 프로그래밍 언어로 작성될 수 있습니다. Mattermost 서버가 보낸 요청을 수신하고 필요한 JSON 형식으로 응답하는 URL을 제공해야 합니다.

## FAQ

### 슬래시 명령어를 디버깅하려면 어떻게 해야 하나요?

**System Console > Logs**에서 슬래시 명령어를 디버깅하려면 **System Console > Logging > Enable Webhook Debugging**을 **true**로 설정하고 **System Console > Logging > Console Log Level**을 **DEBUG**로 설정하세요.

### 슬래시 명령어에서 여러 응답을 보내려면 어떻게 해야 하나요?

`extra_responses` 파라미터를 사용하여 다음과 같이 여러 응답을 보낼 수 있습니다.

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 696

{
    "response_type": "in_channel",
    "text": "\n#### 2017년 7월 27일 테스트 결과\n@channel 요청하신 테스트 결과입니다.\n\n| 컴포넌트     | 실행된 테스트 | 실패한 테스트                                |\n| ---------- | ----------- | ---------------------------------------------- |\n| Server     | 948         | ✅ 0                           |\n| Web Client | 123         | ⚠️ 2 [(자세히 보기)](http://linktologs) |\n| iOS Client | 78          | ⚠️ 3 [(자세히 보기)](http://linktologs) |\n\t\t      ",
    "username": "test-automation",
    "icon_url": "https://www.mattermost.org/wp-content/uploads/2016/04/icon.png",
    "props": {
        "test_data": {
            "ios": 78,
            "server": 948,
            "web": 123
        }
    },
    "extra_responses": [
       {
         "text": "메시지 2",
         "username": "test-automation"
       },
       {
         "text": "메시지 3",
         "username": "test-automation"
       }
     ]
}
```

### 슬래시 명령어가 응답을 구성하는 데 시간이 오래 걸리면 어떻게 하나요?

명령어 수신을 확인하기 위해 즉시 `ephemeral` 메시지로 응답한 다음, `response_url`을 사용하여 원래 명령어 호출 시점부터 30분 이내에 최대 5개의 추가 메시지를 보낼 수 있습니다.

### 슬래시 명령어가 localhost에 연결하지 못하는 이유는 무엇인가요?

기본적으로 Mattermost는 루프백(`127.0.0.0/8`) 및 다양한 개인용 서브넷을 포함한 특정 일반 IP 범위로 확인되는 외부 연결을 금지합니다.

개발 중에는 `config.json`에서 `ServiceSettings.AllowedUntrustedInternalConnections`를 `"127.0.0.0/8"`로 설정하거나 **System Console > Advanced > Developer**를 통해 이 동작을 재정의할 수 있습니다. 자세한 내용은 [구성 설정 문서](https://docs.mattermost.com/configure/environment-configuration-settings.html#allow-untrusted-internal-connections)를 참조하세요.

### 슬래시 명령어를 POST와 GET 중 어떤 방식으로 구성해야 하나요?

모범 사례는 요청이 멱등성(idempotent)인 경우에만 `GET`을 사용하는 것입니다. 즉, 요청을 안전하게 반복할 수 있고 주어진 입력에 대해 동일한 응답을 반환할 것으로 예상될 수 있어야 합니다. 슬래시 명령어를 호스팅하는 일부 서버는 `GET` 요청의 쿼리 문자열을 통해 전달되는 데이터 양에 제한을 둘 수도 있습니다.

그러나 궁극적으로는 선택은 사용자의 몫입니다. 확실하지 않은 경우 슬래시 명령어를 `POST` 요청으로 구성하세요.

### 슬래시 명령어가 계속해서 빈 응답을 반환하며 실패하는 이유는 무엇인가요?

`Content-Type: application/json` 헤더를 보내는 경우 본문은 유효한 JSON이어야 합니다. JSON 디코딩에 실패하면 이 오류 메시지가 발생합니다.

또한 `response_type`을 제공해야 합니다. 이 필드가 누락되면 Mattermost는 기본값을 가정하지 않습니다.

### 슬래시 명령어가 JSON 데이터를 형식화하지 않고 출력하는 이유는 무엇인가요?

`Content-Type: application/json` 헤더를 보내고 있는지 확인하세요. 그렇지 않으면 본문이 일반 텍스트로 처리되어 그대로 게시됩니다.

### 슬래시 명령어는 Slack과 호환되나요?

[Slack 호환성](https://developers.mattermost.com/integrate/slash-commands/slack/) 페이지를 참조하세요.

### 봇 계정을 사용하여 슬래시 명령어에 응답하려면 어떻게 해야 하나요?

#### 통합을 개발하는 경우

- 응답에 사용할 봇 계정의 [개인 액세스 토큰](https://developers.mattermost.com/integrate/reference/personal-access-token/)을 설정하세요.
- [REST API](https://api.mattermost.com/#tag/posts/operation/CreatePost)를 사용하여 액세스 토큰으로 게시물을 생성하세요.

#### 플러그인을 개발하는 경우

[`CreatePost`](https://developers.mattermost.com/integrate/reference/server/server-reference/#API.CreatePost) 플러그인 API를 사용하세요. 게시물의 `UserId`를 봇 계정의 `UserId`로 설정해야 합니다. 임시 게시물을 생성하려면 대신 [`SendEphemeralPost`](https://developers.mattermost.com/integrate/reference/server/server-reference/#API.SendEphemeralPost) 플러그인 API를 사용하세요.

## 슬래시 명령어 문제 해결

슬래시 명령어 문제 해결에 대한 도움은 [Mattermost 사용자 커뮤니티](https://mattermost.com/pl/default-ask-mattermost-community)에 가입하세요.


