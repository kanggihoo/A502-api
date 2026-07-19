# Jira API 동작 테스트 (jira-api-test)

## 목적
`api-docs/jira-api-priority-filter.md` 의 "첫 API 검증 순서"를 실제 PAT 로 검증하는 POC.
완성도보다 검증 가능성·재현성을 우선한다.

## 구성
- `jira_client.py` — 공통 모듈(설정·HTTP 클라이언트·리포트). 모든 테스트가 의존.
- `test_p0_readonly.py` — P0 읽기 전용(사용자·프로젝트·JQL·이슈·댓글·remote link·필터).
- `test_p1_readonly.py` — P1 읽기 후보(우선순위·이슈타입·컴포넌트·버전·대시보드·JQL parse).
- `test_webhooks.py` — webhook 권한 검증(GET /webhook 시도, 403 예상).

## 인증
OAuth 2.0 (Bearer Token) 방식.
- `.env` 변수: `JIRA_OAUTH_TOKEN`, `JIRA_CLOUD_ID`.
- 세션 헤더에 `Authorization: Bearer <JIRA_OAUTH_TOKEN>` 추가.
- API Endpoint URL에 `JIRA_CLOUD_ID`가 포함된 OAuth 게이트웨이 주소 (`https://api.atlassian.com/ex/jira/{cloudId}/rest/api/3`) 사용.

## 실행 규칙
- 셸 명령은 `rtk` 우선(`uv run` 은 `rtk proxy uv run ...`).
- 의존성: `uv sync`.
- 실행: `uv run python test_p0_readonly.py` (P1, webhooks 동일 패턴).
- 민감 정보(토큰/이메일)는 로그에 출력하지 않는다.

## 설계 원칙
- HTTP 오류는 예외로 중단하지 않고 `(status, error)` 로 기록. 403 이 어디서 나는지가 핵심.
- JQL 의 `username`/`userkey` 사용 금지 → `accountId` 또는 `currentUser()`.
- webhook(403)은 "실패"가 아니라 "확인된 제약" 으로 기록.
