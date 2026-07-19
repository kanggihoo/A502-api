---
title: "Webhooks"
source: "https://docs.gitlab.com/user/project/integrations/webhooks/"
created: 2026-07-20
description: "GitLab에서 프로젝트 및 그룹 웹훅을 구성하고 관리합니다."
---

/

---

Webhook은 실시간 알림을 통해 GitLab을 다른 도구 및 시스템에 연결합니다. GitLab에서 중요한 이벤트가 발생하면 웹훅이 해당 정보를 외부 애플리케이션에 직접 전송합니다. 머지 리퀘스트, 코드 푸시, 이슈 업데이트에 반응하여 자동화 워크플로우를 구축하세요.

웹훅을 사용하면 변경 사항이 발생할 때 팀이 동기화 상태를 유지할 수 있습니다:

- GitLab 이슈가 변경되면 외부 이슈 트래커가 자동으로 업데이트됩니다.
- 채팅 애플리케이션이 파이프라인 완료에 대해 팀원에게 알립니다.
- 코드가 메인 브랜치에 도달하면 커스텀 스크립트가 애플리케이션을 배포합니다.
- 모니터링 시스템이 조직 전체의 개발 활동을 추적합니다.

## 웹훅 이벤트

GitLab의 다양한 이벤트가 웹훅을 트리거할 수 있습니다. 예를 들어:

- 리포지토리에 코드 푸시
- 이슈에 댓글 작성
- 머지 리퀘스트 생성

## 웹훅 제한

GitLab.com은 [웹훅 제한](https://docs.gitlab.com/user/gitlab_com/#webhooks)을 적용합니다. 여기에는 다음이 포함됩니다:

- 프로젝트 또는 그룹당 최대 웹훅 수
- 분당 웹훅 호출 수
- 웹훅 타임아웃 시간

GitLab Self-Managed의 경우 관리자가 이러한 제한을 수정할 수 있습니다.

### 푸시 이벤트 제한

GitLab은 여러 변경 사항이 포함된 푸시 이벤트에 대한 웹훅 트리거를 제한합니다:

- 기본 제한: 푸시당 3개의 브랜치 또는 태그
- 초과 시 동작: 전체 푸시 이벤트에 대해 웹훅이 트리거되지 않음
- 적용 대상: 프로젝트 웹훅 및 시스템 훅 모두
- 설정: GitLab Self-Managed 관리자는 애플리케이션 설정 API를 통해 `push_event_hooks_limit` 설정을 수정할 수 있습니다.

여러 태그나 브랜치를 동시에 자주 푸시하면서 웹훅 알림이 필요한 경우 GitLab 관리자에게 문의하여 이 제한을 늘리세요.

## 그룹 웹훅

- 등급: Premium, Ultimate

그룹 웹훅은 그룹 및 하위 그룹의 모든 프로젝트에서 발생하는 이벤트에 대한 알림을 전송하는 커스텀 HTTP 콜백입니다.

### 그룹 웹훅 이벤트 유형

그룹 웹훅이 수신하도록 구성할 수 있는 이벤트:

- 그룹 및 하위 그룹의 프로젝트에서 발생하는 모든 이벤트
- 그룹별 이벤트(그룹 멤버 이벤트, 프로젝트 이벤트, 하위 그룹 이벤트 포함)

### 프로젝트와 그룹 모두에 웹훅이 있는 경우

그룹과 해당 그룹의 프로젝트 모두에 동일한 웹훅을 구성하면 해당 프로젝트의 이벤트에 대해 두 웹훅이 모두 트리거됩니다. 이를 통해 GitLab 조직의 여러 수준에서 유연한 이벤트 처리가 가능합니다.

## 웹훅 구성

GitLab에서 웹훅을 생성하고 구성하여 프로젝트의 워크플로우와 통합하세요. 특정 요구 사항에 맞는 웹훅을 설정하려면 다음 기능을 사용하세요.

### 웹훅 생성

새 웹훅에는 시크릿 토큰 대신 서명 토큰을 사용하세요. 서명 토큰은 페이로드에 대해 HMAC-SHA256 서명을 계산하므로 엔드포인트가 요청의 신뢰성과 무결성을 모두 확인할 수 있습니다. 시크릿 토큰은 헤더에 평문 텍스트 값만 제공하므로 보장 수준이 낮습니다. 새 웹훅에는 시크릿 토큰을 권장하지 않습니다.

프로젝트 또는 그룹의 이벤트에 대한 알림을 보내는 웹훅을 생성하세요.

전제 조건:

- 프로젝트 웹훅의 경우 프로젝트에 대한 Maintainer 또는 Owner 역할이 있어야 합니다.
- 그룹 웹훅의 경우 그룹에 대한 Owner 역할이 있어야 합니다.

웹훅을 생성하려면:

1. 상단 표시줄에서 **Search or go to**를 선택하고 프로젝트 또는 그룹을 찾습니다.
2. 왼쪽 사이드바에서 **Settings** > **Webhooks**를 선택합니다.
3. **Add new webhook**을 선택합니다.
4. **URL**에 웹훅 엔드포인트의 URL을 입력합니다. 특수 문자는 퍼센트 인코딩을 사용하세요.
5. 선택 사항. 웹훅의 **Name**과 **Description**을 입력합니다.
6. 선택 사항. 요청 인증을 구성합니다. 더 강력한 보안을 위해 서명 토큰을 사용하세요:
   - **서명 토큰** (권장): **Generate signing token**을 선택합니다. 토큰은 한 번만 표시되므로 지금 복사하여 저장하세요. 웹훅 엔드포인트는 이 토큰을 사용하여 [HMAC-SHA256 서명을 검증](https://docs.gitlab.com/user/project/integrations/webhooks/#verify-the-signature)할 수 있습니다.
   - **시크릿 토큰** (비권장): **Secret token** 필드에 토큰을 입력합니다. 이 토큰은 `X-Gitlab-Token` HTTP 헤더에 평문으로 전송되며 서명 토큰보다 보안 수준이 낮습니다. 새 웹훅에는 서명 토큰을 대신 사용하세요.
7. **Trigger** 섹션에서 웹훅을 트리거할 이벤트를 선택합니다.
8. 선택 사항. SSL 검증을 비활성화하려면 **Enable SSL verification** 체크박스를 해제합니다.
9. **Add webhook**을 선택합니다.

### 서명 토큰

서명 토큰을 사용하여 웹훅 페이로드가 GitLab에서 발신되었으며 변조되지 않았음을 확인하세요. 시크릿 토큰과 달리 서명 토큰은 페이로드에 대해 HMAC-SHA256 서명을 계산하는 데 사용됩니다. 즉, 수신자는 수신된 페이로드의 신뢰성과 무결성을 모두 독립적으로 검증할 수 있습니다.

GitLab 웹훅 전송은 [Standard Webhooks](https://www.standardwebhooks.com/) 사양을 따릅니다. 모든 웹훅 요청에는 `webhook-id` 및 `webhook-timestamp` 헤더가 포함됩니다. 서명 토큰이 구성된 경우 GitLab은 `webhook-signature` 헤더도 HMAC-SHA256 서명과 함께 포함합니다. 각 서명의 형식은 `v1,{base64_signature}`입니다. 헤더에는 여러 개의 공백으로 구분된 서명이 포함될 수 있습니다. GitLab은 현재 하나의 서명을 전송하지만, 이는 향후 변경될 수 있습니다. 서명은 문자열 `{message_id}.{timestamp}.{body}`에 대해 계산됩니다. 여기서:

- `{message_id}`는 `webhook-id` 헤더의 값입니다.
- `{timestamp}`는 `webhook-timestamp` 헤더의 값입니다.
- `{body}`는 원시 JSON 요청 본문입니다.

#### 서명 검증

웹훅 엔드포인트에서 서명을 검증하려면:

1. `webhook-id`, `webhook-timestamp`, `webhook-signature` 헤더 값을 검색합니다.
2. `webhook-signature` 값을 공백으로 분할하여 서명 목록을 가져옵니다.
3. 메시지 문자열을 구성합니다: `"{message_id}.{timestamp}.{body}"`.
4. 서명 토큰을 디코딩합니다: `whsec_` 접두사를 제거한 후 나머지를 base64 디코딩합니다.
5. 디코딩된 키를 사용하여 HMAC-SHA256 다이제스트를 계산합니다.
6. 다이제스트를 base64로 인코딩하고 `v1,`을 접두사로 붙입니다.
7. 계산된 서명이 서명 목록의 항목과 일치하는지 확인합니다. 타이밍 공격을 방지하려면 상수 시간 비교를 사용하세요.

Ruby 예제:

```ruby
require 'base64'
require 'openssl'

def valid_signature?(signing_token, message_id, timestamp, body, received_signatures)
  raw_key = Base64.strict_decode64(signing_token.delete_prefix('whsec_'))
  message = "#{message_id}.#{timestamp}.#{body}"
  digest = OpenSSL::HMAC.digest('sha256', raw_key, message)
  expected = "v1,#{Base64.strict_encode64(digest)}"
  received_signatures.split(' ').any? do |sig|
    ActiveSupport::SecurityUtils.secure_compare(expected, sig)
  end
end
```

Python 예제:

```python
import base64
import hashlib
import hmac

def valid_signature(signing_token, message_id, timestamp, body, received_signatures):
    raw_key = base64.b64decode(signing_token.removeprefix('whsec_'))
    message = f"{message_id}.{timestamp}.{body}".encode('utf-8')
    digest = hmac.new(raw_key, message, hashlib.sha256).digest()
    expected = "v1," + base64.b64encode(digest).decode('utf-8')
    return any(
        hmac.compare_digest(expected, sig)
        for sig in received_signatures.split(' ')
    )
```

#### 이전 버전과의 호환성

서명 토큰은 기존 시크릿 토큰과 함께 작동합니다. 동일한 웹훅에 둘 다 구성할 수 있습니다:

- 시크릿 토큰이 구성된 경우 `X-Gitlab-Token` 헤더가 계속 전송됩니다.
- 서명 토큰이 구성된 경우 `webhook-signature` 및 `webhook-id` 헤더가 전송됩니다.

시크릿 토큰을 사용하는 기존 웹훅을 다운타임 없이 서명 토큰으로 마이그레이션하려면 전환 기간 동안 동일한 웹훅에 두 토큰을 모두 구성하세요. `webhook-signature`가 있는 경우 서명을 검증하고, 그렇지 않은 경우 시크릿 토큰으로 대체하도록 수신기를 업데이트하세요.

수신기가 서명을 올바르게 처리하면 웹훅 설정에서 시크릿 토큰을 제거할 수 있습니다.

#### 보안 고려 사항

재생 공격을 방지하려면 페이로드를 처리하기 전에 `webhook-timestamp`의 타임스탬프가 최근인지 확인하세요.

서명 토큰은 API로 절대 반환되지 않습니다.

### 웹훅 URL의 민감한 부분 마스킹

웹훅 URL의 민감한 부분을 마스킹하여 보안을 강화하세요. 마스킹된 부분은 웹훅이 실행될 때 구성된 값으로 대체되며, 로깅되지 않고 데이터베이스에서 암호화되어 저장됩니다.

웹훅 URL의 민감한 부분을 마스킹하려면:

1. 상단 표시줄에서 **Search or go to**를 선택하고 프로젝트 또는 그룹을 찾습니다.
2. 왼쪽 사이드바에서 **Settings** > **Webhooks**를 선택합니다.
3. **URL**에 웹훅의 전체 URL을 입력합니다.
4. 마스킹할 부분을 정의하려면 **Add URL masking**을 선택합니다.
5. **Sensitive portion of URL**에 마스킹하려는 URL 부분을 입력합니다.
6. **How it looks in the UI**에 마스킹된 부분 대신 표시할 값을 입력합니다. 변수 이름은 소문자(`a-z`), 숫자(`0-9`), 밑줄(`_`)만 포함해야 합니다.
7. **Save changes**를 선택합니다.

마스킹된 값은 UI에서 숨겨져 표시됩니다. 예를 들어 `path`와 `value` 변수를 정의한 경우 웹훅 URL은 다음과 같이 표시될 수 있습니다:

```plaintext
https://webhook.example.com/{path}?key={value}
```

### 커스텀 헤더

외부 서비스 인증을 위해 웹훅 요청에 커스텀 헤더를 추가하세요. 웹훅당 최대 20개의 커스텀 헤더를 구성할 수 있습니다.

커스텀 헤더는 다음 조건을 충족해야 합니다:

- 전송 헤더의 값을 덮어쓰지 않아야 합니다.
- 영숫자, 마침표, 대시 또는 밑줄만 포함해야 합니다.
- 문자로 시작하고 문자 또는 숫자로 끝나야 합니다.
- 연속된 마침표, 대시 또는 밑줄이 없어야 합니다.

커스텀 헤더는 **Recent events**에 마스킹된 값으로 표시됩니다.

### 커스텀 웹훅 템플릿

웹훅에 대한 커스텀 페이로드 템플릿을 생성하여 요청 본문에 전송되는 데이터를 제어하세요.

#### 커스텀 웹훅 템플릿 생성

- 프로젝트 웹훅의 경우 프로젝트에 대한 Maintainer 또는 Owner 역할이 있어야 합니다.
- 그룹 웹훅의 경우 그룹에 대한 Owner 역할이 있어야 합니다.

커스텀 웹훅 템플릿을 생성하려면:

1. 웹훅 설정으로 이동합니다.
2. 커스텀 웹훅 템플릿을 설정합니다.
3. 템플릿이 유효한 JSON으로 렌더링되는지 확인합니다.

템플릿에서 이벤트 페이로드의 필드를 사용하세요. 예를 들어:

- `{{build_name}}` (작업 이벤트)
- `{{deployable_url}}` (배포 이벤트)

중첩된 속성에 액세스하려면 마침표를 사용하여 경로 세그먼트를 구분하세요.

#### 커스텀 웹훅 템플릿 예제

다음 커스텀 페이로드 템플릿의 경우:

```json
{
  "event": "{{object_kind}}",
  "project_name": "{{project.name}}"
}
```

`push` 이벤트의 결과 요청 페이로드는 다음과 같습니다:

```json
{
  "event": "push",
  "project_name": "Example"
}
```

커스텀 웹훅 템플릿은 배열의 속성에 액세스할 수 없습니다.

### 브랜치별 푸시 이벤트 필터링

웹훅 엔드포인트로 전송되는 `push` 이벤트를 브랜치 이름으로 필터링하세요. 다음 필터링 옵션 중 하나를 사용하세요:

- **All branches**: 모든 브랜치의 푸시 이벤트 수신
- **Wildcard pattern**: 와일드카드 패턴과 일치하는 브랜치의 푸시 이벤트 수신
- **Regular expression**: 정규식과 일치하는 브랜치의 푸시 이벤트 수신

#### 와일드카드 패턴 사용

와일드카드 패턴을 사용하여 필터링하려면:

1. 웹훅 설정에서 **Wildcard pattern**을 선택합니다.
2. 패턴을 입력합니다. 예를 들어:
   - `*-stable`은 `-stable`로 끝나는 브랜치와 일치합니다.
   - `production/*`은 `production/` 네임스페이스의 브랜치와 일치합니다.

#### 정규식 사용

정규식을 사용하여 필터링하려면:

1. 웹훅 설정에서 **Regular expression**을 선택합니다.
2. [RE2 문법](https://github.com/google/re2/wiki/Syntax)을 따르는 정규식 패턴을 입력합니다.

예를 들어 `main` 브랜치를 제외하려면 다음을 사용하세요:

```plaintext
\b(?:m(?!ain\b)|ma(?!in\b)|mai(?!n\b)|[a-l]|[n-z])\w*|\b\w{1,3}\b|\W+
```

### 상호 TLS를 지원하도록 웹훅 구성

- 제공: GitLab Self-Managed

PEM 형식의 글로벌 클라이언트 인증서를 설정하여 웹훅이 상호 TLS를 지원하도록 구성하세요.

전제 조건:

- GitLab 관리자여야 합니다.

웹훅에 대한 상호 TLS를 구성하려면:

1. PEM 형식의 클라이언트 인증서를 준비합니다.
2. 선택 사항. PEM 암호로 인증서를 보호합니다.
3. GitLab이 인증서를 사용하도록 구성합니다.

1. `/etc/gitlab/gitlab.rb`를 편집합니다:
   ```ruby
   gitlab_rails['http_client']['tls_client_cert_file'] = '<클라이언트 PEM 파일 경로>'
   gitlab_rails['http_client']['tls_client_cert_password'] = '<선택적 비밀번호>'
   ```
2. 파일을 저장하고 GitLab을 재구성합니다:
   ```shell
   sudo gitlab-ctl reconfigure
   ```

구성 후, GitLab은 웹훅 연결을 위한 TLS 핸드셰이크 중에 이 인증서를 서버에 제시합니다.

### 웹훅 트래픽을 위한 방화벽 구성

GitLab이 웹훅을 전송하는 방식에 따라 방화벽을 구성하세요:

- Sidekiq 노드에서 비동기적으로 (가장 일반적)
- Rails 노드에서 동기적으로 (특정 경우)

웹훅은 UI에서 테스트하거나 재시도할 때 Rails 노드에서 동기적으로 전송됩니다.

방화벽을 구성할 때 Sidekiq 노드와 Rails 노드가 모두 웹훅 트래픽을 전송할 수 있는지 확인하세요.

## 웹훅 관리

GitLab에서 구성된 웹훅을 모니터링하고 유지 관리하세요.

### 웹훅 요청 기록 보기

웹훅 요청 기록을 확인하여 성능을 모니터링하고 문제를 해결하세요.

전제 조건:

- 프로젝트 웹훅의 경우 프로젝트에 대한 Maintainer 또는 Owner 역할이 있어야 합니다.
- 그룹 웹훅의 경우 그룹에 대한 Owner 역할이 있어야 합니다.

웹훅의 요청 기록을 보려면:

1. 상단 표시줄에서 **Search or go to**를 선택하고 프로젝트 또는 그룹을 찾습니다.
2. 왼쪽 사이드바에서 **Settings** > **Webhooks**를 선택합니다.
3. 웹훅의 **Edit**을 선택합니다.
4. **Recent events** 섹션으로 이동합니다.

**Recent events** 섹션은 지난 2일 동안 웹훅에 전송된 모든 요청을 표시합니다. 테이블에는 다음이 포함됩니다:

- HTTP 상태 코드:
  - `200` - `299` 코드: 녹색
  - 기타 코드: 빨간색
  - 전송 실패: `internal error`
- 트리거된 이벤트
- 요청 경과 시간
- 요청이 이루어진 상대적 시간

[![상태 코드와 응답 시간을 보여주는 웹훅 이벤트 로그](https://docs.gitlab.com/user/project/integrations/img/webhook_logs_v14_4.png)](https://docs.gitlab.com/user/project/integrations/img/webhook_logs_v14_4.png)

#### 요청 및 응답 세부 정보 확인

전제 조건:

- 프로젝트 웹훅의 경우 프로젝트에 대한 Maintainer 또는 Owner 역할이 있어야 합니다.
- 그룹 웹훅의 경우 그룹에 대한 Owner 역할이 있어야 합니다.

**Recent events**의 각 웹훅 요청에는 **Request details** 페이지가 있습니다. 이 페이지에는 다음의 본문과 헤더가 포함됩니다:

- GitLab이 웹훅 수신기 엔드포인트로부터 받은 응답
- GitLab이 전송한 웹훅 요청

웹훅 이벤트의 요청 및 응답 세부 정보를 확인하려면:

1. 상단 표시줄에서 **Search or go to**를 선택하고 프로젝트 또는 그룹을 찾습니다.
2. 왼쪽 사이드바에서 **Settings** > **Webhooks**를 선택합니다.
3. 웹훅의 **Edit**을 선택합니다.
4. **Recent events** 섹션으로 이동합니다.
5. 이벤트의 **View details**를 선택합니다.

동일한 데이터와 동일한 `Idempotency-Key` 헤더로 요청을 다시 보내려면 **Resend Request**를 선택합니다. 웹훅 URL이 변경된 경우 요청을 다시 보낼 수 없습니다. 프로젝트 웹훅 API를 통해 프로그래밍 방식으로 요청을 다시 보낼 수도 있습니다.

### 웹훅 테스트

웹훅이 제대로 작동하는지 확인하거나 비활성화된 웹훅을 다시 활성화하려면 테스트하세요.

전제 조건:

- 프로젝트 웹훅의 경우 프로젝트에 대한 Maintainer 또는 Owner 역할이 있어야 합니다.
- 그룹 웹훅의 경우 그룹에 대한 Owner 역할이 있어야 합니다.
- `push events`를 테스트하려면 프로젝트에 커밋이 하나 이상 있어야 합니다.

웹훅을 테스트하려면:

1. 상단 표시줄에서 **Search or go to**를 선택하고 프로젝트 또는 그룹을 찾습니다.
2. 왼쪽 사이드바에서 **Settings** > **Webhooks**를 선택하여 이 프로젝트의 모든 웹훅을 확인합니다.
3. 구성된 웹훅 목록에서 직접 웹훅을 테스트하려면:
   1. 테스트할 웹훅을 찾습니다.
   2. **Test** 드롭다운 목록에서 테스트할 이벤트 유형을 선택합니다.
4. 웹훅을 편집하면서 테스트하려면:
   1. 테스트할 웹훅을 찾고 **Edit**을 선택합니다.
   2. 웹훅을 변경합니다.
   3. **Test** 드롭다운 목록을 선택한 다음 테스트할 이벤트 유형을 선택합니다.

일부 이벤트 유형은 프로젝트 및 그룹 웹훅에 대해 테스트가 지원되지 않습니다. 자세한 내용은 [이슈 379201](https://gitlab.com/gitlab-org/gitlab/-/issues/379201)을 참조하세요.

## 웹훅 참조

이 기술 참조를 사용하여:

- GitLab 웹훅의 작동 방식을 이해합니다.
- 웹훅을 시스템과 통합합니다.
- 웹훅 구성을 설정, 문제 해결 및 최적화합니다.

### 웹훅 수신기 요구 사항

안정적인 웹훅 전송을 보장하려면 빠르고 안정적인 웹훅 수신기 엔드포인트를 구현하세요.

느리거나 불안정하거나 잘못 구성된 수신기는 자동으로 비활성화될 수 있습니다. 잘못된 HTTP 응답은 실패한 요청으로 처리됩니다.

웹훅 수신기를 최적화하려면:

1. `200` 또는 `201` 상태로 빠르게 응답:
   - 동일한 요청에서 웹훅을 처리하지 않음
   - 수신 후 웹훅을 처리하기 위해 큐 사용
   - GitLab.com에서 자동 비활성화를 방지하기 위해 타임아웃 제한 전에 응답
2. 잠재적인 중복 이벤트 처리:
   - 웹훅이 타임아웃되면 중복 이벤트에 대비
   - 엔드포인트가 지속적으로 빠르고 안정적인지 확인
3. 응답 헤더와 본문 최소화:
   - GitLab은 나중에 검사할 수 있도록 응답 헤더와 본문을 저장
   - 반환되는 헤더의 수와 크기 제한
   - 빈 본문으로 응답 고려
4. 적절한 상태 코드 사용:
   - 잘못 구성된 웹훅에만 클라이언트 오류 상태 응답(`4xx` 범위) 반환
   - 지원되지 않는 이벤트의 경우 `400`을 반환하거나 페이로드 무시
   - 처리된 이벤트에 대해 `500` 서버 오류 응답 방지

### 자동 비활성화된 웹훅

> [!type-flag] 유형 플래그
> 이 기능의 가용성은 기능 플래그에 의해 제어됩니다. 자세한 내용은 기록을 참조하세요.

GitLab은 4회 연속 실패한 프로젝트 또는 그룹 웹훅을 자동으로 비활성화합니다.

자동 비활성화된 웹훅을 보려면:

1. 상단 표시줄에서 **Search or go to**를 선택하고 프로젝트 또는 그룹을 찾습니다.
2. 왼쪽 사이드바에서 **Settings** > **Webhooks**를 선택합니다.

웹훅 목록에서 자동 비활성화된 웹훅은 다음과 같이 표시됩니다:

- **Temporarily disabled**: 4회 연속 실패
- **Disabled**: 40회 연속 실패

[![비활성화 및 일시적 비활성화 상태 배지를 표시하는 웹훅 목록](https://docs.gitlab.com/user/project/integrations/img/failed_badges_v17_11.png)](https://docs.gitlab.com/user/project/integrations/img/failed_badges_v17_11.png)

#### 일시적으로 비활성화된 웹훅

웹훅이 4회 연속 실패하면 일시적으로 비활성화됩니다. 웹훅이 40회 연속 실패하면 영구적으로 비활성화됩니다.

실패는 다음과 같은 경우에 발생합니다:

- 웹훅 수신기가 `4xx` 또는 `5xx` 범위의 응답 코드를 반환하는 경우
- 웹훅 수신기에 연결하려고 할 때 웹훅이 타임아웃되는 경우
- 웹훅에 다른 HTTP 오류가 발생하는 경우

일시적으로 비활성화된 웹훅은 처음에 1분 동안 비활성화되며, 후속 실패 시 지속 시간이 최대 24시간까지 연장됩니다. 이 기간이 경과하면 웹훅이 자동으로 다시 활성화됩니다.

#### 영구적으로 비활성화된 웹훅

웹훅이 40회 연속 실패하면 영구적으로 비활성화됩니다. 일시적으로 비활성화된 웹훅과 달리 이러한 웹훅은 자동으로 다시 활성화되지 않습니다.

GitLab 17.10 이하에서 영구적으로 비활성화된 웹훅은 데이터 마이그레이션을 거쳤습니다. UI에 40회 실패라고 표시될 수 있지만, **Recent events**에는 4회 실패가 표시될 수 있습니다.

#### 비활성화된 웹훅 다시 활성화

비활성화된 웹훅을 다시 활성화하려면 테스트 요청을 보내세요. 테스트 요청이 `2xx` 범위의 응답 코드를 반환하면 웹훅이 다시 활성화됩니다.

### 전송 헤더

GitLab은 웹훅 요청에 다음 헤더를 엔드포인트에 포함합니다.

| 헤더 | 설명 | 예시 |
| --- | --- | --- |
| `Idempotency-Key` | 웹훅 재시도 간에 일관된 고유 ID. 레거시 이유로 사용 가능, `webhook-id` 권장. | `"f5e5f430-f57b-4e6e-9fac-d9128cd7232f"` |
| `User-Agent` | `"Gitlab/<VERSION>"` 형식의 사용자 에이전트. | `"GitLab/15.5.0-pre"` |
| `webhook-id` | 웹훅 재시도 간에 일관된 고유 메시지 ID. `Idempotency-Key`와 동일. | `"f5e5f430-f57b-4e6e-9fac-d9128cd7232f"` |
| `webhook-signature` | 각각 `v1,{base64_signature}` 형식의 HMAC-SHA256 서명 목록(공백으로 구분). [서명 토큰](https://docs.gitlab.com/user/project/integrations/webhooks/#signing-tokens)이 구성된 경우에만 포함. | `"v1,abc123def456=="` |
| `webhook-timestamp` | 요청이 생성된 Unix 타임스탬프(epoch 이후 초). | `"1744578123"` |
| `X-Gitlab-Event-UUID` | 비재귀적 웹훅의 고유 ID. 재귀적 웹훅(이전 웹훅에 의해 트리거됨)은 동일한 값을 공유. | `"13792a34-cac6-4fda-95a8-c58e00a3954e"` |
| `X-Gitlab-Event` | 웹훅 유형 이름. `"<EVENT> Hook"` 형식의 이벤트 유형에 해당. | `"Push Hook"` |
| `X-Gitlab-Instance` | 웹훅을 전송한 GitLab 인스턴스의 호스트명. | `"https://gitlab.com"` |
| `X-Gitlab-Token` | 웹훅의 시크릿 토큰, 평문으로 전송. 시크릿 토큰이 구성된 경우에만 포함. | `"my-secret-token"` |
| `X-Gitlab-Webhook-UUID` | 각 웹훅의 고유 ID. | `"02affd2d-2cba-4033-917d-ec22d5dc4b38"` |

### 웹훅 본문의 이미지 URL 표시

GitLab은 웹훅 본문에서 상대 이미지 참조를 절대 URL로 재작성합니다.

#### 이미지 URL 재작성 예제

머지 리퀘스트, 댓글 또는 위키 페이지의 원본 이미지 참조가 다음과 같은 경우:

```markdown
![상대 URL을 사용한 마크다운 이미지.](/uploads/$sha/image.png)
```

웹훅 본문에서 재작성된 이미지 참조는 다음과 같습니다:

```markdown
![절대 URL을 사용한 마크다운 이미지.](https://gitlab.example.com/-/project/:id/uploads/<SHA>/image.png)
```

이 예제는 다음을 가정합니다:

- GitLab이 `gitlab.example.com`에 설치됨
- 프로젝트 ID가 `123`

#### 이미지 URL 재작성 예외

GitLab은 다음 경우에 이미지 URL을 재작성하지 않습니다:

- 이미 HTTP, HTTPS 또는 프로토콜 상대 URL을 사용하는 경우
- 링크 레이블과 같은 고급 마크다운 기능을 사용하는 경우

## 관련 주제

- [웹훅 이벤트 및 JSON 페이로드](https://docs.gitlab.com/user/project/integrations/webhook_events/)
- [웹훅 제한](https://docs.gitlab.com/user/gitlab_com/#webhooks)
- [프로젝트 웹훅 API](https://docs.gitlab.com/api/project_webhooks/)
- [그룹 웹훅 API](https://docs.gitlab.com/api/group_webhooks/)
- [시스템 훅 API](https://docs.gitlab.com/api/system_hooks/)
- [웹훅 문제 해결](https://docs.gitlab.com/user/project/integrations/webhooks_troubleshooting/)
- [웹훅과 Twilio로 SMS 알림 보내기](https://www.datadoghq.com/blog/send-alerts-sms-customizable-webhooks-twilio/)
- [GitLab 레이블 자동 적용](https://about.gitlab.com/blog/applying-gitlab-labels-automatically/)
