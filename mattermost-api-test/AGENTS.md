# Mattermost API 동작 테스트 (mattermost-api-test)

## 목적
`api-docs/mattermost-api-priority-filter.md` 의 "첫 API 검증 순서"를 실제 PAT 로 검증하는 POC.
완성도보다 검증 가능성·재현성을 우선한다.

## 구성
- `mattermost_client.py` — 공통 모듈(설정·HTTP 클라이언트·리포트). 모든 테스트가 의존.
- `test_p0_readonly.py` — P0 읽기(사용자·팀·채널·게시글·스레드·봇·상태·북마크).
- `test_p1_readonly.py` — P1 읽기(검색·슬래시 명령·플레이북 가용성).
- `test_webhooks.py` — 쓰기: incoming webhook 생성 + (옵션)전송. **삭제하지 않음**.
- `test_posts_write.py` — 쓰기: 채널 게시글·스레드 답글 작성.

## 인증
- `Authorization: Bearer <PAT>` 헤더.
- user_id 자리에 `me` 리터럴 사용 가능 (`/users/me`, `/users/me/teams/{team_id}/channels`).
- `.env` 변수: `MATTERMOST_TOKEN`.

## 실행 규칙
- 셸 명령은 `rtk` 우선 (`uv run` 은 `rtk proxy uv run ...`).
- 의존성: `uv sync`.
- 실행: `uv run python test_p0_readonly.py` (P1, webhooks, posts_write 동일 패턴).
- 쓰기 스크립트(webhooks, posts_write)는 실제 리소스를 변경하므로 주의.
- 민감 정보(토큰)는 로그에 출력하지 않는다.

## 설계 원칙
- HTTP 오류는 예외로 중단하지 않고 `(status, error)` 로 기록. 403 위치가 핵심.
- 전체 채널 `GET /channels`(관리자 전용) 회피 → 사용자 스코프 사용.
- posts 응답 `{order: [], posts: {}}` 구조.
- **webhook은 남겨둔다.** 통합 서비스의 실제 연동 수단.
- 플레이북/북마크는 버전·플러그인 의존 → 404는 "비활성화"로 해석.
