# Handoff — GitLab API 동작 테스트 POC → 다음 세션

## 한 줄 요약

SSAFY self-hosted GitLab(`lab.ssafy.com`) REST API 읽기 권한 검증 POC 완료.
P0(12개) + P1(9개) = **총 21개 읽기 엔드포인트 전부 200 정상 응답**.
제품 비전의 "데이터 수집·통합 대시보드" 계층은 읽기 권한상 기술적 차단 없음 확인.

## 저장소 / 산출물

- **GitHub (public)**: https://github.com/kanggihoo/gitlab-api-test
- **로컬 경로**: `/Users/kkh/Desktop/A502-api/gitlab-api-test/`
- **커밋 3건** (main 브랜치):
  - `f19da0a` 초기 버전 (gitlab_client, test_p0_readonly, test_webhooks, README, .env.example)
  - `dc02eec` P0 리포트 error/elapsed_ms 필드 매핑 버그 수정
  - `9bc7f2c` P1 읽기 후보 스크립트 + README 매트릭스
- **스크립트 구성**:
  - `gitlab_client.py` — 공통: 설정 로드, GitLabClient(HTTP 래퍼), Report(터미널+JSON 리포트)
  - `test_p0_readonly.py` — P0 읽기 전용 12개 검증
  - `test_p1_readonly.py` — P1 읽기 후보 9개 검증
  - `test_webhooks.py` — webhook 생성·조회·삭제 (쓰기, Maintainer 전제, **아직 실행 안 함**)
- **참조 문서**: `/Users/kkh/Desktop/A502-api/api-docs/gitlab-api-priority-filter.md` (우선순위 필터), `/Users/kkh/Desktop/A502-api/api-docs/gitlab_rest_defuddle_markdown/` (GitLab REST API 원문)
- **워크스페이스 지침**: `/Users/kkh/Desktop/A502-api/AGENTS.md`

## 검증으로 확정된 사실 (재검증 불필요)

### 권한 / 스코프
- 토큰 하나(`read_api` scope)로 P0+P1 읽기 전부 가능. 읽기 권한 한계선 확인 완료.
- 읽기 권한 조사에 더 이상 시간 쓸 필요 없음.

### 토큰 주인 / 대상 프로젝트
- 현재 사용자: `@11kkh19` (강기호), id=30128, active
- 자동 탐지된 대상 프로젝트: `s15-webmobile1-sub1/S15P11A502`, **숫자 id=1373907**, default_branch=main
- 프로젝트 식별자: 숫자 id(불변, 권장) 또는 URL-encoded path `s15-webmobile1-sub1%2FS15P11A502`

### 멤버 구성 (62명, 페이지네이션으로 전수 확인 완료)
- Owner(50): 1명 — `ssafyadmin` (SSAFY 연구팀, 인스턴스 관리자)
- Maintainer(40): 56명 — 감시원/코치/교수 + 팀원 대부분 (구분 불가)
- **Developer(30): 5명 — 진짜 팀원**: brightrain453(이현우), developersmminwoo(김민우), dutjddnr0916(여성욱), hyejeong2823(허정원), minjae5024(이민재)
- **팀장 식별 불가** — 팀장도 Maintainer(40)라 감시원/코치와 섞임. 별도 메타데이터(이름 매핑/그룹 구조/별도 설정) 필요.

### 핵심 설계 원칙 (제품에 반영 확정)
1. **항상 프로젝트 스코프** (`/projects/{숫자ID}/...`). `scope=all` 금지 — 타팀 데이터 노출됨 (실제 `scope=all` 이슈 조회 시 enjoytrip/BaekjoonHub 등 타팀 이슈 섞임 확인).
2. **페이지네이션 필수** — `per_page=20` 기본이라 62명/다수 데이터는 루프 수집 필요. 현재 코드는 미구현.
3. **숫자 id 기준** — path는 프로젝트 이동/이름 변경 시 깨짐, 숫자 id는 불변.
4. **데이터 0개 ≠ API 실패** — 빈 리스트도 `ok=True`. "데이터 부재" vs "권한 차단" 구분이 검증 목적.

## 미해결 / 다음에 할 일 (우선순위 순)

### 1. 통합(integrations) 상세 분석 — 최우선 (아키텍처 결정 분기)
- P1 6-1 `GET /projects/{id}/integrations` 통과했으나 **활성 통합 목록 상세 미분석**.
- 리포트(`results/P1_읽기_전용_API_검증_20260716_001600.json`)의 6-1 sample 확인 필요.
- 결정해야 할 것: Jenkins/Jira/Mattermost를 GitLab 내장 통합으로 쓸지, 직접 각 도구 API 호출할지, webhook 수신할지.
- 이 결정이 제품 아키텍처(수집 계층 설계)를 좌우함.

### 2. webhook 검증 (쓰기, 아직 실행 안 함)
- `test_webhooks.py` 코드는 있으나 사용자가 "webhook 제외" 결정.
- 재검토 시: `webhook.site` 같은 수신 사이트로 권한만 먼저 확인 (Maintainer 토큰 + `api` scope 필요).
- `WEBHOOK_TEST_URL` env 설정 시에만 동작 (안전장치).
- 주의: `lab.ssafy.com` → `localhost` 직접 불가 (서버가 자기 localhost 가리킴). 터널링(ngrok/cloudflared) 또는 EC2 수신 서버 필요.

### 3. 페이지네이션 일반화
- 현재 `gitlab_client.py`는 단일 페이지만 조회.
- 62명 멤버처럼 20개 초과 데이터를 전수 수집하려면 `page` 루핑 + `X-Total`/`X-Total-Pages` 헤더 처리 추가.
- 이미 대화에서 62명 전수 조회용 ad-hoc 스크립트로 검증은 완료(위 멤버 구성 참조), 정식 코드화만 남음.

### 4. 팀장 역할 식별 방안 조사
- access_level만으론 팀장/감시원 구분 불가.
- 후보: GitLab 커스텀 역할, 그룹 구조 매핑, 별도 설정 파일, 사용자 수동 지정.

### 5. 프로토타입 통합 대시보드 / 알림 흐름 설계
- 읽기 데이터 수집은 기술적 가능성 확정 → 실제 제품 UI/알림 흐름 설계 단계.
- Mattermost 알림, 행동 가능한 정보 선별, 원문 URL 매핑 포함.

## 기술적 노트

- **`.env` 존재함 (gitignored)** — 실제 토큰 포함. 절대 커밋 금지. `.env.example`만 커밋 대상.
- **`results/` gitignored** — P0/P1 리포트 JSON 3개 로컬에 있음. 민감 정보(프로젝트명/멤버명 등) 포함 가능.
- **실행**: `cd gitlab-api-test && uv sync && uv run python test_p0_readonly.py` (또는 test_p1_readonly.py / test_webhooks.py)
- uv 기반 가상환경 (.python-version: 3.12, 의존성: requests, python-dotenv)
- Python 3.12 사용

## 다음 세션 추천 스킬

- **통합 분석/대시보드 설계 진입 시**: `superpowers:brainstorming` (요구사항 탐색 후 설계)
- **페이지네이션 구현 등 코드 작업**: TDD 접근 시 `superpowers:test-driven-development`
- **결과 정리/문서화**: `structured-summary`
