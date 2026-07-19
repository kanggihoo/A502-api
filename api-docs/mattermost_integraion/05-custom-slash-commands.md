---
title: "사용자 정의 명령어"
source: "https://developers.mattermost.com/integrate/slash-commands/custom/"
created: 2026-07-20
description: "Mattermost 기여, 통합 및 확장에 필요한 모든 것을 제공하는 원스톱 shop입니다."
---

## 사용자 정의 슬래시 명령어

특정 도시의 날씨를 확인할 수 있는 외부 애플리케이션을 작성한다고 가정해 보겠습니다. 사용자 정의 슬래시 명령어를 만들고 명령어의 HTTP `POST` 또는 `GET`을 처리하도록 애플리케이션을 설정하면, 사용자가 `/weather toronto week`와 같은 명령어를 사용하여 해당 도시의 주간 날씨를 확인할 수 있습니다.

다음 일반 지침에 따라 애플리케이션용 사용자 정의 Mattermost 슬래시 명령어를 설정할 수 있습니다.

1. **상품 메뉴 > Integrations > Slash Commands**를 엽니다. 메인 메뉴에 **Integrations** 옵션이 없으면 슬래시 명령어가 Mattermost 서버에서 활성화되지 않았거나 관리자가 아닌 사용자에게 비활성화되어 있을 수 있습니다. **System Console > Integrations > Integration Management**에서 활성화하거나 Mattermost 시스템 관리자에게 요청하세요.
2. **Add Slash Command**를 선택하면 **Add** 대화상자가 나타납니다. 다음 지침에 따라 슬래시 명령어를 구성하세요:
   - 명령어의 **Title**과 **Description**을 설정합니다.
   - **Command Trigger Word**를 설정합니다. 트리거 단어는 고유해야 하며 슬래시로 시작하거나 공백을 포함할 수 없습니다. 또한 [내장 명령어](https://developers.mattermost.com/integrate/slash-commands/built-in/) 중 하나일 수 없습니다.
   - **Request URL**과 **Request Method**를 설정합니다. 요청 URL은 Mattermost가 애플리케이션에 접근하기 위해 호출하는 엔드포인트이며, 요청 메서드는 `POST` 또는 `GET` 중 하나로 요청 URL로 전송되는 요청 유형을 지정합니다.
   - (*선택 사항*) 명령어가 Mattermost에 메시지를 게시할 때 사용할 **Response Username**과 **Response Icon**을 설정합니다. 설정하지 않으면 명령어는 사용자의 사용자 이름과 프로필 사진을 사용합니다.
   - (*선택 사항*) **Autocomplete** 옵션을 선택하여 빈 입력 상자에 `/`를 입력할 때 표시되는 명령어 자동 완성 목록에 슬래시 명령어를 포함시킵니다. 이를 통해 팀원이 명령어를 더 쉽게 발견할 수 있습니다. 또한 명령어의 인수를 나열하는 힌트와 자동 완성 목록에 표시될 간단한 설명을 제공할 수 있습니다.
3. **Save**를 선택합니다. 다음 페이지에서 **Token** 값을 복사합니다. 이 값은 이후 단계에서 사용됩니다.
   ![이미지](https://developers.mattermost.com/integrate/slash-commands/custom/slash_commands_token.png)
4. 다음으로 외부 애플리케이션을 작성합니다. Mattermost로부터 HTTP `POST` 또는 HTTP `GET` 요청을 수신하는 함수를 포함하세요. 요청은 다음과 같은 형태입니다:
   ```http
   POST /weather HTTP/1.1
   Host: weather-service:4000
   Accept: application/json
   Accept-Encoding: gzip
   Authorization: Token qzgakf1nx3yt9dr4n8585ihbxy
   Content-Length: 567
   Content-Type: application/x-www-form-urlencoded
   User-Agent: Mattermost-Bot/1.1
   channel_id=fukxanjgjbnp7ng383at53k1sy&
   channel_name=town-square&
   command=%2Fweather&
   response_url=http%3A%2F%2Flocalhost%3A8066%2Fhooks%2Fcommands%2Fi11f6nnfgfyk8eg56x9omc6dpa&
   team_domain=team-awesome&
   team_id=wx4zz8t4ttgmtxqiwfohijayzc&
   text=toronto+week&
   token=qzgakf1nx3yt9dr4n8585ihbxy&
   trigger_id=ZWZ5ZjRndzR4YmJxOHJlZWh4MXpkaHozbnI6ZXJqNnFjazNyZmd0dWpzODZ3NXI2cmNremg6MTY2MjA0MTY5Njg5NjpNRVFDSUQ5cTZ3MkRHU1RaNjhyaDh1TGl1STlSVHh2R1czSXZ5aGVRYjhkWThuZnlBaUI2YnlPR2ZpWlczR1FmVkdIODlreEp4MmlVT0UxMm9LMjlkZ1d0RC8xbjZRPT0%3D&
   user_id=erj6qck3rfgtujs86w5r6rckzh&
   user_name=alan
   ```
   통합이 JSON 응답을 반환하는 경우 `application/json` 콘텐츠 유형을 반환하는지 확인하세요.
5. HTTP `POST` 또는 `GET` 요청에는 bearer 토큰이 포함된 `Authorization` 헤더가 포함됩니다. 요청이 유효한 것으로 간주되려면 bearer 토큰이 3단계의 **Token** 값과 일치해야 합니다.
6. 애플리케이션이 `town-square`에 메시지를 다시 게시하려면 HTTP `POST` 또는 `GET` 요청에 JSON 페이로드로 응답할 수 있습니다.
   Mattermost는 사용자 경험을 세부 조정하기 위해 응답에서 여러 [파라미터](#response-parameters)를 지원합니다. 예를 들어, 메시지가 게시될 때의 사용자 이름과 프로필 사진을 재정의하거나, [플러그인](https://developers.mattermost.com/integrate/plugins/)에서 사용할 웹훅 메시지를 보낼 때 사용자 정의 게시물 유형을 지정할 수 있습니다. 응답 페이로드에 [첨부 파일 배열](https://developers.mattermost.com/integrate/reference/message-attachments/)과 [대화형 메시지 버튼](https://developers.mattermost.com/integrate/plugins/interactive-messages/)을 포함하면 고급 서식의 메시지를 만들 수 있습니다.
   외부 날씨 애플리케이션은 다음과 같이 JSON 페이로드로 응답할 수 있습니다:
   ```
   {"response_type": "in_channel", "text": "
     ---
     #### 2016년 2월 16일 주의 Ontario, Toronto 날씨
     | 요일              | 설명                        | 최고    | 최저    |
     |:--------------------|:---------------------------------|:-------|:-------|
     | 월, 2월 15일       | 눈발이 섞인 흐림                | 3 °C   | -12 °C |
     | 화, 2월 16일       | 맑음                             | 4 °C   | -8 °C  |
     | 수, 2월 17일       | 부분적으로 흐림                  | 4 °C   | -14 °C |
     | 목, 2월 18일       | 비가 내릴 수 있는 흐림          | 2 °C   | -13 °C |
     | 금, 2월 19일       | 흐림                            | 5 °C   | -7 °C  |
     | 토, 2월 20일       | 구름이 다소 있는 맑음           | 7 °C   | -4 °C  |
     | 일, 2월 21일       | 부분적으로 흐림                 | 6 °C   | -9 °C  |
     ---
   "}
   ```
   JSON 응답은 Mattermost에서 다음과 같이 렌더링됩니다:
   ![이미지](https://developers.mattermost.com/integrate/slash-commands/custom/weatherBot.png)

## 응답 파라미터

슬래시 명령어 응답은 `text` 필드 외에도 더 많은 기능을 지원합니다. 지원되는 전체 파라미터 목록은 다음과 같습니다.

| 파라미터 | 설명 | 필수 |
| --- | --- | --- |
| `text` | 게시물에 표시할 [Markdown 형식](https://docs.mattermost.com/messaging/formatting-text.html) 메시지입니다. | `attachments`가 설정되지 않은 경우, 예 |
| `attachments` | 더 풍부한 서식 옵션을 위한 [메시지 첨부 파일](https://developers.mattermost.com/integrate/reference/message-attachments/)입니다. | `text`가 설정되지 않은 경우, 예 |
| `response_type` | 빈 값 또는 `ephemeral`로 설정하면 사용자만 볼 수 있는 메시지로 응답합니다. `in_channel`로 설정하면 일반 메시지를 생성합니다. 기본값은 `ephemeral`입니다. | 아니요 |
| `username` | 메시지를 게시하는 사용자 이름을 재정의합니다. 기본값은 웹훅 생성 시 설정된 사용자 이름이며, 설정되지 않은 경우 웹훅 생성자의 사용자 이름이 사용됩니다. [구성에서 활성화](https://docs.mattermost.com/configure/configuration-settings.html#enable-integrations-to-override-usernames)되어 있어야 합니다. | 아니요 |
| `channel_id` | 메시지가 게시될 채널을 재정의합니다. 기본값은 명령어가 실행된 채널입니다. | 아니요 |
| `icon_url` | 메시지와 함께 게시되는 프로필 사진을 재정의합니다. 기본값은 웹훅 생성 시 설정된 URL이며, 설정되지 않은 경우 웹훅 생성자의 프로필 사진이 사용됩니다. [구성에서 활성화](https://docs.mattermost.com/configure/configuration-settings.html#enable-integrations-to-override-profile-picture-icons)되어 있어야 합니다. | 아니요 |
| `goto_location` | 사용자를 리디렉션할 URL입니다. `http://`, `https://`, `ftp://`, `ssh://` 및 `mailto://`를 포함한 여러 프로토콜을 지원합니다. | 아니요 |
| `type` | 게시물 `type`을 설정하며, 주로 플러그인에서 사용합니다. 비어 있지 않은 경우 `custom_`으로 시작해야 합니다. `attachments`를 전달하면 이 필드가 무시되고 유형이 `slack_attachment`로 설정됩니다. | 아니요 |
| `extra_responses` | 응답에서 여러 개의 게시물을 보내는 데 사용되는 응답 배열입니다. 이 배열의 각 항목은 자체 명령어 응답 형태를 가지므로 `goto_location`과 `extra_responses` 자체를 제외한 여기에 나열된 다른 모든 파라미터를 포함할 수 있습니다. Mattermost v5.6부터 사용 가능합니다. | 아니요 |
| `skip_slack_parsing` | `true`로 설정하면 Mattermost가 [Slack 호환성](https://developers.mattermost.com/integrate/slash-commands/slack/) 처리를 건너뜁니다. Slack 호환성 로직에 의해 잘못 처리되는 텍스트나 코드가 게시물에 포함된 경우 유용합니다. Mattermost v5.20부터 사용 가능합니다. | 아니요 |
| `props` | 게시물 `props`를 설정하며, 게시물에 추가 데이터나 메타데이터를 저장하기 위한 JSON 속성 모음입니다. 주로 [REST API](https://api.mattermost.com/)를 통해 게시물에 접근하는 다른 통합에서 사용됩니다. 다음 키는 예약되어 있으며 제공되어도 무시됩니다: `from_webhook`, `from_bot`, `from_oauth_app`, `from_plugin`, `force_notification`, `silent_notification`, `override_username`, `override_icon_url`, `override_icon_emoji`, `webhook_display_name`, `card`, `attachments`. | 아니요 |

여러 파라미터를 사용한 응답 페이로드 예시는 다음과 같습니다:

```json
{
    "response_type": "in_channel",
    "text": "\n#### 2017년 7월 27일 테스트 결과\n@channel 요청하신 테스트 결과입니다.\n\n| 컴포넌트     | 실행된 테스트 | 실패한 테스트                                |\n| ---------- | ----------- | ---------------------------------------------- |\n| Server     | 948         | ✅ 0                           |\n| Web Client | 123         | ⚠️ 2 [(자세히 보기)](https://linktologs) |\n| iOS Client | 78          | ⚠️ 3 [(자세히 보기)](https://linktologs) |\n\t\t      ",
    "username": "test-automation",
    "icon_url": "https://mattermost.com/wp-content/uploads/2022/02/icon.png",
    "props": {
        "test_data": {
            "ios": 78,
            "server": 948,
            "web": 123
        }
    },
}
```

## 지연 응답 및 다중 응답

`response_url` 파라미터를 사용하여 슬래시 명령어에 여러 응답을 제공하거나 지연된 응답을 제공할 수 있습니다. 응답 URL을 사용하여 원래 명령어 호출 시점부터 30분 이내에 최대 5개의 추가 메시지를 보낼 수 있습니다.

지연 응답은 작업을 수행하는 데 3초 이상 걸리는 경우 유용합니다. 예를 들어:

- 응답 시간이 3초 이상 걸릴 수 있는 외부 타사 서비스에서 데이터 검색
- 보고서 생성, 배치 처리 또는 응답에 3초 이상 걸리는 기타 장기 실행 프로세스

응답 URL로 전송되는 모든 요청은 일반 텍스트 또는 JSON 인코딩 본문이어야 합니다. JSON 인코딩 메시지는 [Markdown 서식](https://docs.mattermost.com/messaging/formatting-text.html)과 [메시지 첨부 파일](https://developers.mattermost.com/integrate/reference/message-attachments/)을 모두 지원합니다.


