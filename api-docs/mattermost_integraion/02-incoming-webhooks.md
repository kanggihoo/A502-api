---
title: "수신 웹훅"
source: "https://developers.mattermost.com/integrate/webhooks/incoming/"
created: 2026-07-20
description: "수신 웹훅"
---



## 수신 웹훅 생성하기

Mattermost에 다음 메시지를 게시하는 간단한 수신 웹훅을 만드는 방법을 알아보겠습니다.

![`Hello, this is some text. This is some more text.`를 게시하는 수신 웹훅](https://developers.mattermost.com/integrate/webhooks/incoming/incoming_webhooks_create_simple.png)

1. Mattermost에서 **상품 메뉴 > Integrations > Incoming Webhook**으로 이동합니다.
   - **Integrations** 옵션이 없다면, 수신 웹훅이 Mattermost 서버에서 활성화되지 않았거나 관리자가 아닌 사용자에게 비활성화되어 있을 수 있습니다. 시스템 관리자가 **System Console > Integrations > Integration Management**에서 활성화할 수 있습니다. 수신 웹훅이 활성화되면 아래 단계를 계속 진행하세요.
2. **Add Incoming Webhook**을 선택하고 웹훅의 이름과 설명을 추가합니다. 설명은 최대 500자까지 입력할 수 있습니다.
3. 웹훅 페이로드를 수신할 채널을 선택한 후 **Add**를 선택하여 웹훅을 생성합니다.

그러면 다음과 같은 형태의 웹훅 엔드포인트가 생성됩니다:

```
https://your-mattermost-server.com/hooks/xxx-generatedkey-xxx
```

**이 엔드포인트를 비밀 정보로 취급하세요.** 이 엔드포인트를 알고 있는 사람은 누구나 Mattermost 인스턴스에 메시지를 게시할 수 있습니다.

## 수신 웹훅 사용하기

엔드포인트를 사용하려면 애플리케이션에서 다음 요청을 보내세요:

```http
POST /hooks/xxx-generatedkey-xxx HTTP/1.1
Host: your-mattermost-server.com
Content-Type: application/json
Content-Length: 63

{
    "text": "Hello, this is some text\nThis is more text. 🎉"
}
```

예를 들어, 다음은 동일한 요청을 `cURL`로 보낸 것입니다:

```bash
curl -i -X POST -H 'Content-Type: application/json' -d '{"text": "Hello, this is some text\nThis is more text. 🎉"}' https://your-mattermost-server.com/hooks/xxx-generatedkey-xxx
```

Slack 수신 웹훅과의 호환성을 위해, `Content-Type` 헤더가 설정되지 않은 경우 요청 본문 앞에 `payload=`를 붙여야 합니다:

```
payload={"text": "Hello, this is some text\nThis is more text. 🎉"}
```

성공적인 요청은 다음과 같은 응답을 받습니다:

```
HTTP/1.1 200 OK
Content-Type: text/plain
X-Request-Id: hoan6o9ws7rp5xj7wu9rmysrte
X-Version-Id: 4.7.1.dev.12799cd77e172e8a2eba0f9091ec1471.false
Date: Sun, 04 Mar 2018 17:19:09 GMT
Content-Length: 2

ok
```

모든 웹훅 게시물은 Mattermost 클라이언트에서 사용자 이름 옆에 `BOT` 표시를 표시하여 [피싱 공격](https://en.wikipedia.org/wiki/Phishing)을 방지하는 데 도움을 줍니다.

### 파라미터

수신 웹훅은 `text` 필드 외에도 더 많은 기능을 지원합니다. 지원되는 전체 파라미터 목록은 다음과 같습니다.

| 파라미터 | 설명 | 필수 |
| --- | --- | --- |
| `text` | 게시물에 표시할 [Markdown 형식](https://docs.mattermost.com/messaging/formatting-text.html) 메시지입니다.   알림을 트리거하려면 다른 Mattermost 메시지에서와 같이 `@<username>`, `@channel`, `@here`를 사용하세요. | `attachments`가 설정되지 않은 경우, 예 |
| `channel` | 메시지가 게시될 채널을 재정의합니다. 표시 이름이 아닌 채널 이름을 사용하세요 (예: `Town Square`가 아닌 `town-square`).  다이렉트 메시지로 보내려면 사용자 이름 앞에 "@"를 붙이세요.  기본값은 웹훅 생성 시 설정된 채널입니다.  웹훅은 웹훅 생성자가 속한 모든 공개 채널 및 비공개 채널에 게시할 수 있습니다.  다이렉트 메시지로의 게시물은 대상 사용자와 웹훅 생성자 간의 다이렉트 메시지에 표시됩니다. | 아니요 |
| `username` | 메시지를 게시하는 사용자 이름을 재정의합니다.  기본값은 웹훅 생성 시 설정된 사용자 이름입니다. 생성 시 사용자 이름이 설정되지 않은 경우 `webhook`이 사용됩니다.  사용자 이름 재정의가 적용되려면 [통합이 사용자 이름을 재정의하도록 허용](https://docs.mattermost.com/configure/configuration-settings.html#enable-integrations-to-override-usernames) 구성 설정이 활성화되어 있어야 합니다. | 아니요 |
| `icon_url` | 메시지와 함께 게시되는 프로필 사진을 재정의합니다.  기본값은 웹훅 생성 시 설정된 URL입니다. 생성 시 아이콘이 설정되지 않은 경우 표준 웹훅 아이콘이 표시됩니다.  아이콘 재정의가 적용되려면 [통합이 프로필 사진 아이콘을 재정의하도록 허용](https://docs.mattermost.com/configure/configuration-settings.html#enable-integrations-to-override-profile-picture-icons) 구성 설정이 활성화되어 있어야 합니다. | 아니요 |
| `icon_emoji` | 프로필 사진과 `icon_url` 파라미터를 재정의합니다.  기본값은 없으며 웹훅 생성 시 설정되지 않습니다.  예상 값은 메시지에 입력하는 이모지 이름으로, 콜론(`:`)을 포함하거나 포함하지 않을 수 있습니다.  재정의가 적용되려면 [통합이 프로필 사진 아이콘을 재정의하도록 허용](https://docs.mattermost.com/configure/configuration-settings.html#enable-integrations-to-override-profile-picture-icons) 구성 설정이 활성화되어 있어야 합니다. | 아니요 |
| `attachments` | 더 풍부한 서식 옵션을 위한 [메시지 첨부 파일](https://developers.mattermost.com/integrate/reference/message-attachments/)입니다. | `text`가 설정되지 않은 경우, 예 |
| `type` | 게시물 `type`을 설정하며, 주로 플러그인에서 사용합니다.  비어 있지 않은 경우 `burn_on_read`로 설정되지 않았다면 `custom_`으로 시작해야 합니다. | 아니요 |
| `props` | 게시물에 추가 데이터나 메타데이터를 저장하기 위한 JSON 속성 모음인 게시물 `props`를 설정합니다.  주로 REST API를 통해 게시물에 접근하는 다른 통합에서 사용됩니다.  다음 키는 예약되어 있으며 제공되어도 무시됩니다: `from_webhook`, `from_bot`, `from_oauth_app`, `from_plugin`, `force_notification`, `silent_notification` (대신 최상위 `silent` 필드 사용), `override_username`, `override_icon_url`, `override_icon_emoji`, `webhook_display_name`, `card`, `attachments`.  `card` props는 Mattermost로 추가 정보(Markdown 형식 텍스트)를 보낼 수 있으며, 사용자가 게시물 옆에 표시된 **정보** 아이콘을 선택한 후에만 RHS 패널에 표시됩니다.  **정보** 아이콘은 사용자 지정할 수 없으며, 메시지에 `card` 데이터가 전달된 경우에만 사용자에게 표시됩니다.  이 속성은 Mattermost v5.14부터 사용 가능합니다.  현재 `card` 기능은 모바일을 지원하지 않습니다. | 아니요 |
| `priority` | 메시지의 우선순위를 설정합니다. [메시지 우선순위](https://developers.mattermost.com/integrate/reference/message-priority/) 참조 | 아니요 |
| `silent` | `true`로 설정하면 게시물이 자동으로 전송됩니다. 채널에는 표시되지만 데스크톱/푸시/이메일 알림이 발생하지 않고, 읽지 않음 또는 멘션 카운트가 증가하지 않으며, "새 메시지" 줄도 표시되지 않습니다. 일상적인 봇 상태 업데이트 또는 감사 추적 게시물에 사용하세요. `priority.persistent_notifications`와 상호 배타적입니다. 기본값은 `false`입니다. | 아니요 |

더 많은 파라미터를 사용한 예시 요청은 다음과 같습니다:

```http
POST /hooks/xxx-generatedkey-xxx HTTP/1.1
Host: your-mattermost-server.com
Content-Type: application/json
Content-Length: 630

{
  "channel": "town-square",
  "username": "test-automation",
  "icon_url": "https://mattermost.com/wp-content/uploads/2022/02/icon.png",
  "text": "#### 2017년 7월 27일 테스트 결과\n@channel 실패한 테스트를 검토해주세요.\n\n| 컴포넌트     | 실행된 테스트 | 실패한 테스트                                |\n|:-----------|:-----------:|:-----------------------------------------------|\n| Server     | 948         | ✅ 0                           |\n| Web Client | 123         | ⚠️ 2 [(자세히 보기)](https://linktologs) |\n| iOS Client | 78          | ⚠️ 3 [(자세히 보기)](https://linktologs) |"
}
```

이 내용은 Town Square 채널에 다음과 같이 표시됩니다:

![테스트 결과를 보여주는 test-automation 봇](https://developers.mattermost.com/integrate/webhooks/incoming/incoming_webhooks_full_example.png)

오른쪽 패널에 추가 데이터를 표시하는 예시 요청은 `props` 객체의 `card` 필드에 Markdown 텍스트를 전달하는 방식으로 다음과 같습니다:

```http
POST /hooks/xxx-generatedkey-xxx HTTP/1.1
Host: your-mattermost-server.com
Content-Type: application/json

{
  "channel": "town-square",
  "username": "Winning-bot",
  "text": "#### 새 거래를 성사했습니다!",
  "props": {
    "card": "Salesforce 기회 정보:\n\n [기회 이름](https://salesforce.com/OPPORTUNITY_ID)\n\n-영업 담당자: **Bob McKnight** \n\n 금액: **$300,020.00**"
  }
}
```

웹훅 페이로드에 `card` 속성을 가진 `props` 객체가 있으면 게시된 메시지에 타임스탬프 옆에 작은 정보 아이콘이 표시됩니다. 이 아이콘을 클릭하면 오른쪽 패널이 확장되어 `card` 속성에 포함된 Markdown이 표시됩니다:

![정보 아이콘을 클릭하면 오른쪽 패널이 열려 card 속성의 Markdown을 표시합니다](https://user-images.githubusercontent.com/915956/64055959-ec0cfe80-cb44-11e9-8ee3-b64d47c86032.png)

### Slack 호환성

Mattermost는 Slack용으로 작성된 통합을 Mattermost로 쉽게 마이그레이션할 수 있게 해줍니다. Slack의 `icon_emoji` 파라미터를 사용하면 프로필 아이콘과 `icon_url` 파라미터를 재정의할 수 있으며, Mattermost v5.14부터 지원됩니다.

#### Slack 데이터 형식을 Mattermost로 변환

Mattermost는 Slack에서 수신된 데이터를 자동으로 변환합니다:

1. Slack용으로 작성된 JSON 페이로드에 다음이 포함된 경우 Mattermost markdown으로 변환되어 Slack과 동등하게 렌더링됩니다:
   - URL 링크를 나타내는 `<>` (예: `{"text": "<https://mattermost.com/>"}`)
     - 링크 텍스트를 정의하기 위해 `<>` 내부의 `|` (예: `{"text": "링크를 보려면 <https://mattermost.com/|여기>를 클릭하세요."}`)
     - 사용자 멘션을 트리거하는 `<userid>` (예: `{"text": "<5fb5f7iw8tfrfcwssd1xmx3j7y> 알림입니다."}`)
     - 채널 멘션을 트리거하는 `<!channel>`, `<!here>` 또는 `<!all>` (예: `{"text": "<!channel> 알림입니다."}`)
2. Slack에서와 같이 `payload={"text": "안녕하세요", channel: "@jim"}`처럼 채널 이름을 *@username*으로 재정의하여 다이렉트 메시지를 보낼 수 있습니다.
3. Slack에서와 같이 채널 이름 앞에 *#*를 붙여도 메시지가 올바른 채널로 전송됩니다.

#### GitLab에서 Slack UI를 사용한 Mattermost 웹훅

GitLab은 GitHub의 선도적인 오픈 소스 대안이며 Slack과의 내장 통합을 제공합니다. GitLab의 Slack 인터페이스를 사용하여 코드 변경 없이 Mattermost 웹훅을 직접 추가할 수 있습니다:

1. GitLab에서 **Settings > Services**로 이동하여 **Slack**을 선택합니다.
2. **메인 메뉴 > Integrations > Incoming Webhooks**에서 Mattermost가 제공한 수신 웹훅 URL을 붙여넣습니다.
3. 알림이 표시될 때 표시할 **Username**을 선택적으로 설정합니다. **Channel** 필드는 비워둡니다.
4. **Save**를 선택한 후 설정을 테스트하여 메시지가 Mattermost로 성공적으로 전송되는지 확인합니다.

#### 알려진 Slack 호환성 문제

1. `<#CHANNEL_ID>`를 사용한 채널 참조는 채널에 링크되지 않습니다.
2. `<!everyone>` 및 `<!group>`은 지원되지 않습니다.
3. "mrkdwn", "parse", "link\_names" 파라미터는 지원되지 않습니다. Mattermost는 기본적으로 Markdown을 변환하고 @멘션을 자동으로 링크합니다.
4. `*bold*` 형식의 굵게 표시는 지원되지 않습니다 (`**bold**`로 작성해야 함).
5. 웹훅은 웹훅을 생성한 사용자에게 다이렉트 메시지를 보낼 수 없습니다.

### 팁 및 모범 사례

1. `text`가 게시물당 허용되는 문자 제한보다 길면 메시지는 각각 제한 내에 있는 여러 개의 연속 게시물로 분할됩니다. Mattermost Server v5.0부터 [최대 16383자의 게시물이 지원됩니다](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
2. 웹훅 통합은 HTTP POST 요청을 보낼 수 있다면 모든 프로그래밍 언어로 작성할 수 있습니다.
3. `application/x-www-form-urlencoded` 및 `multipart/form-data` 모두 지원되는 `Content-Type` 헤더입니다. `Content-Type`이 제공되지 않으면 `application/json`으로 간주됩니다.
4. 다이렉트 메시지 채널로 메시지를 보내려면 channel 파라미터에 사용자 이름 앞에 "@" 기호를 추가하세요. 자신의 사용자 이름을 추가하여 웹훅 게시물을 자신과의 다이렉트 메시지 채널로 보낼 수 있습니다.
   ```
   payload={"channel": "@username", "text": "Hello, this is some text\nThis is more text. 🎉"}
   ```
   이렇게 하면 수신 웹훅을 설정한 계정에서 "@" 기호 뒤의 사용자 이름으로 메시지가 전송됩니다. 예를 들어, 사용자 `alice`로 웹훅을 생성하고 웹훅을 사용하여 `bob`에게 다이렉트 메시지를 보내면, 다른 설정(예: username)과 관계없이 `alice`에서 `bob`으로의 다이렉트 메시지로 표시됩니다.
   다른 두 사용자 간의 다이렉트 메시지 채널로 메시지를 보내려면 두 사용자의 사용자 ID를 두 개의 밑줄(\_) 기호로 구분하여 채널을 지정할 수 있습니다. 사용자 ID를 찾으려면 [mmctl user search](https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-user-search)를 사용할 수 있습니다.
   ```
   payload={"channel": "6w41z1q367dujfaxr1nrykr5oc__94dzjnkd8igafdraw66syi1cde", "text": "Hello, this is some text\nThis is more text. 🎉"}
   ```

### 수신 웹훅 문제 해결

**System Console > Logs**에서 수신 웹훅을 디버깅하려면 **System Console > Logging > Enable Webhook Debugging**을 **true**로 설정하고 **System Console > Logging > Console Log Level**을 **DEBUG**로 설정하세요.

일반적인 오류 메시지는 다음과 같습니다:

1. `Couldn't find the channel`: 채널이 존재하지 않거나 유효하지 않음을 나타냅니다. 다음 요청을 보내기 전에 `channel` 파라미터를 수정하세요.
2. `Couldn't find the user`: 사용자가 존재하지 않거나 유효하지 않음을 나타냅니다. 다음 요청을 보내기 전에 `user` 파라미터를 수정하세요.
3. `Unable to parse incoming data`: 수신된 요청의 형식이 잘못되었음을 나타냅니다. JSON 페이로드의 형식이 올바르고 추가 `"`와 같은 오타가 없는지 확인하세요.
4. `curl: (3) [globbing] unmatched close brace/bracket in column N`: Windows에서 cURL 사용 시 일반적인 오류로, 다음과 같은 경우에 발생합니다:
   - JSON 구분자 콜론 주위에 공백이 있는 경우 `payload={"Hello" : "test"}` 또는
   - `-d` 데이터를 감싸기 위해 작은따옴표를 사용하는 경우 `-d 'payload={"Hello":"test"}'`

통합이 생성된 메시지를 렌더링하는 대신 JSON 페이로드 데이터를 출력하는 경우, 통합이 `application/json` 콘텐츠 유형을 반환하고 있는지 확인하세요.

#### 메시지 첨부 파일이 렌더링되지 않는 이유는 무엇인가요?

`attachments`가 웹훅 JSON 페이로드에서 **최상위 필드**인지 확인하세요. `props` 내부에 중첩되지 않아야 합니다. REST API는 `props.attachments`를 사용하지만, 수신 웹훅은 `attachments`가 최상위에 있을 것으로 예상합니다.


