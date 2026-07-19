---
title: "발신 웹훅"
source: "https://developers.mattermost.com/integrate/webhooks/outgoing/"
created: 2026-07-20
description: "발신 웹훅"
---

[Mattermost v11.0이 출시되었습니다! 새로운 기능 알아보기 »](https://mattermost.com/blog/mattermost-v11-powering-more-mission-critical-collaboration/)

## 발신 웹훅 생성하기

`town-square` 채널에 누군가 `#build`로 시작하는 메시지를 게시한 후 소프트웨어 테스트를 실행하는 외부 애플리케이션을 작성한다고 가정해 보겠습니다.

다음 일반 지침에 따라 Mattermost 발신 웹훅을 설정할 수 있습니다.

1. 먼저 **상품 메뉴 > Integrations > Outgoing Webhook**으로 이동합니다. **Integrations** 옵션이 없으면 발신 웹훅이 Mattermost 서버에서 활성화되지 않았거나 관리자가 아닌 사용자에게 비활성화되어 있을 수 있습니다. **System Console > Integrations > Integration Management**에서 활성화하거나 시스템 관리자에게 요청하세요.
2. **Add Outgoing Webhook**을 선택하고 웹훅의 이름과 설명을 추가합니다. 설명은 최대 500자까지 입력할 수 있습니다.
3. 요청을 전송할 콘텐츠 유형을 선택합니다.
   - `application/x-www-form-urlencoded`를 선택하면 서버가 요청 본문의 파라미터를 URL 형식으로 인코딩합니다.
   - `application/json`을 선택하면 서버가 요청 본문을 JSON 형식으로 구성합니다.
4. 웹훅 응답을 수신할 공개 채널을 선택하거나, 애플리케이션으로 HTTP POST 요청을 보낼 하나 이상의 트리거 단어를 지정합니다. 발신 웹훅에 대해 채널이나 트리거 단어 중 하나 또는 둘 모두를 구성할 수 있습니다. 둘 다 지정된 경우 메시지는 두 값 모두와 일치해야 합니다.
   이 예시에서는 채널을 `town-square`로 설정하고 트리거 단어로 `#build`를 지정합니다.
5. 이전 단계에서 하나 이상의 트리거 단어를 지정한 경우, 발신 웹훅이 트리거되는 시점을 선택합니다.
   - 메시지의 첫 번째 단어가 트리거 단어 중 하나와 정확히 일치하는 경우, 또는
   - 메시지의 첫 번째 단어가 트리거 단어 중 하나로 시작하는 경우
6. 마지막으로 HTTP POST 요청이 전송될 하나 이상의 콜백 URL을 설정한 후 **Save**를 선택합니다. URL이 비공개인 경우 [신뢰할 수 있는 내부 연결](https://docs.mattermost.com/configure/environment-configuration-settings.html#dev-allowuntrustedinternalconnections)로 추가하세요.
7. 다음 페이지에서 **Token** 값을 복사합니다. 이 값은 이후 단계에서 사용됩니다.
   ![설정 성공 메시지와 설명 메시지의 토큰을 보여주는 대화 상자](https://developers.mattermost.com/integrate/faq/images/outgoing_webhooks_token.png)

## 발신 웹훅 사용하기

1. Mattermost로부터 HTTP POST 요청을 수신하는 함수를 애플리케이션에 포함하세요. POST 요청은 다음과 같은 형태여야 합니다:
   ```http
   POST /my-endpoint HTTP/1.1
   Content-Length: 244
   User-Agent: Go 1.1 package http
   Host: localhost:5000
   Accept: application/json
   Content-Type: application/x-www-form-urlencoded
   channel_id=hawos4dqtby53pd64o4a4cmeoo&
   channel_name=town-square&
   team_domain=someteam&
   team_id=kwoknj9nwpypzgzy78wkw516qe&
   post_id=axdygg1957njfe5pu38saikdho&
   text=some+text+here&
   timestamp=1445532266&
   token=zmigewsanbbsdf59xnmduzypjc&
   trigger_word=some&
   user_id=rnina9994bde8mua79zqcg5hmo&
   user_name=somename
   ```
   통합이 JSON 응답을 반환하는 경우 `application/json` 콘텐츠 유형을 반환하는지 확인하세요.
2. 애플리케이션에 설정 가능한 *MATTERMOST\_TOKEN* 변수를 추가하고 7단계의 **Token** 값으로 설정하세요. 애플리케이션은 이 값을 사용하여 HTTP POST 요청이 Mattermost에서 왔는지 확인합니다.
3. 애플리케이션이 `town-square`에 메시지를 다시 게시하려면 HTTP POST 요청에 다음과 같은 JSON 응답으로 응답할 수 있습니다:
   ```json
   {"text": "
   | Component  | Tests Run | Tests Failed                                   |
   |:-----------|:----------|:-----------------------------------------------|
   | Server     | 948       | ✅ 0                           |
   | Web Client | 123       | ⚠️ [2 (자세히 보기)](http://linktologs) |
   | iOS Client | 78        | ⚠️ [3 (자세히 보기)](http://linktologs) |
   "}
   ```
   이 응답은 Mattermost에서 다음과 같이 렌더링됩니다:
   ![서버, 웹 클라이언트 및 iOS 클라이언트의 테스트 결과](https://developers.mattermost.com/integrate/faq/images/webhooksTable.png)

설정이 완료되었습니다!

## 파라미터

발신 웹훅은 `text` 필드 외에도 더 많은 기능을 지원합니다. 지원되는 전체 파라미터 목록은 다음과 같습니다.

| 파라미터 | 설명 | 필수 |
| --- | --- | --- |
| `text` | 게시물에 표시할 [Markdown 형식](https://docs.mattermost.com/messaging/formatting-text.html) 메시지입니다. 알림을 트리거하려면 다른 Mattermost 메시지에서와 같이 `@<username>`, `@channel`, `@here`를 사용하세요. | `attachments`가 설정되지 않은 경우, 예 |
| `response_type` | `comment`로 설정하면 트리거한 메시지에 답글로 응답합니다. 빈 값 또는 `post`로 설정하면 일반 메시지를 생성합니다. 기본값은 `post`입니다. | 아니요 |
| `username` | 메시지를 게시하는 사용자 이름을 재정의합니다. 기본값은 웹훅 생성 시 설정된 사용자 이름입니다. 생성 시 사용자 이름이 설정되지 않은 경우 `webhook`이 사용됩니다. 사용자 이름 재정의가 적용되려면 [통합이 사용자 이름을 재정의하도록 허용](https://docs.mattermost.com/configure/configuration-settings.html#enable-integrations-to-override-usernames) 구성 설정이 활성화되어 있어야 합니다. | 아니요 |
| `icon_url` | 메시지와 함께 게시되는 프로필 사진을 재정의합니다. 기본값은 웹훅 생성 시 설정된 URL입니다. 생성 시 아이콘이 설정되지 않은 경우 표준 웹훅 아이콘이 표시됩니다. 아이콘 재정의가 적용되려면 [통합이 프로필 사진 아이콘을 재정의하도록 허용](https://docs.mattermost.com/configure/configuration-settings.html#enable-integrations-to-override-profile-picture-icons) 구성 설정이 활성화되어 있어야 합니다. | 아니요 |
| `attachments` | 더 풍부한 서식 옵션을 위한 [메시지 첨부 파일](https://developers.mattermost.com/integrate/reference/message-attachments/)입니다. | `text`가 설정되지 않은 경우, 예 |
| `type` | 게시물 `type`을 설정하며, 주로 플러그인에서 사용합니다. 비어 있지 않은 경우 " `custom_` "으로 시작해야 합니다. `attachments` 속성에 값을 지정하면 이 필드는 무시되고 `type` 값이 `slack_attachment`로 설정됩니다. | 아니요 |
| `props` | 게시물 `props`를 설정하며, 게시물에 추가 데이터나 메타데이터를 저장하기 위한 JSON 속성 모음입니다. 주로 REST API를 통해 게시물에 접근하는 다른 통합에서 사용됩니다. 다음 키는 예약되어 있습니다: `from_webhook`, `override_username`, `override_icon_url`, `webhook_display_name`, `attachments`. | 아니요 |
| `priority` | 메시지의 우선순위를 설정합니다. [메시지 우선순위](https://developers.mattermost.com/integrate/reference/message-priority/) 참조 | 아니요 |

더 많은 파라미터를 사용한 응답 예시는 다음과 같습니다:

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 755

{
  "response_type": "comment",
  "username": "test-automation",
  "icon_url": "https://mattermost.com/wp-content/uploads/2022/02/icon.png",
  "text": "\n#### 2017년 7월 27일 테스트 결과\n@channel 요청하신 테스트 결과입니다.\n\n| 컴포넌트     | 실행된 테스트 | 실패한 테스트                                |\n| ---------- | ----------- | ---------------------------------------------- |\n| Server     | 948         | ✅ 0                           |\n| Web Client | 123         | ⚠️ 2 [(자세히 보기)](http://linktologs) |\n| iOS Client | 78          | ⚠️ 3 [(자세히 보기)](http://linktologs) |\n\t\t      ",
  "props": {
    "test_data": {
    "server": 948,
    "web": 123,
    "ios": 78
    }
  }
}
```

이 응답은 다음과 같은 메시지를 생성합니다:

![테스트 결과를 보여주는 test-automation 봇](https://developers.mattermost.com/integrate/webhooks/outgoing/outgoing_webhooks_full_example.png)


