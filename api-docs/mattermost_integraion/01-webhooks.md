---
title: "웹훅"
source: "https://developers.mattermost.com/integrate/webhooks/"
created: 2026-07-20
description: "웹훅"
---

[Mattermost v11.0이 출시되었습니다! 새로운 기능 알아보기 »](https://mattermost.com/blog/mattermost-v11-powering-more-mission-critical-collaboration/)

Mattermost는 외부 애플리케이션을 서버에 쉽게 통합할 수 있도록 웹훅을 지원합니다.

### 수신 웹훅 (Incoming webhooks)

수신 웹훅을 사용하여 Mattermost 공개 채널, 비공개 채널 및 다이렉트 메시지에 메시지를 게시할 수 있습니다. 메시지는 각 애플리케이션에 대해 생성된 Mattermost URL로 HTTP POST 요청을 통해 전송되며, 요청 본문에는 특정 형식의 JSON 페이로드가 포함됩니다.

[수신 웹훅 생성하기](https://developers.mattermost.com/integrate/webhooks/incoming/)

### 발신 웹훅 (Outgoing webhooks)

발신 웹훅은 메시지가 다음 조건 중 하나 또는 모두에 해당할 때 웹 서비스로 HTTP POST 요청을 보내고 응답을 처리하여 Mattermost로 다시 전달합니다:

- 지정된 채널에 게시된 경우
- 첫 번째 단어가 정의된 트리거 단어(예: `gif`)와 일치하거나 해당 단어로 시작하는 경우

발신 웹훅은 공개 채널에서만 지원됩니다. 비공개 채널 또는 다이렉트 메시지에서 작동하는 트리거가 필요하다면 대신 [슬래시 명령어](https://developers.mattermost.com/integrate/slash-commands/) 사용을 고려해보세요.


