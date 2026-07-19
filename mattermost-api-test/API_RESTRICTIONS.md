# SSAFY Mattermost API 권한 및 연동 제약사항 정리

SSAFY Mattermost 환경에서 실행한 읽기 전용 API 검증 스크립트([test_p0_readonly.py](file:///Users/kkh/Desktop/A502-api/mattermost-api-test/test_p0_readonly.py), [test_p1_readonly.py](file:///Users/kkh/Desktop/A502-api/mattermost-api-test/test_p1_readonly.py))의 결과 데이터([results/P0_읽기_전용_API_검증_20260719_234537.json](file:///Users/kkh/Desktop/A502-api/mattermost-api-test/results/P0_%EC%9D%BD%EA%B8%B0_%EC%A0%84%EC%9A%A9_API_%EA%B2%80%EC%A6%9D_20260719_234537.json), [results/P1_읽기_전용_API_검증_20260719_234606.json](file:///Users/kkh/Desktop/A502-api/mattermost-api-test/results/P1_%EC%9D%BD%EA%B8%B0_%EC%A0%84%EC%9A%A9_API_%EA%B2%80%EC%A6%9D_20260719_234606.json))를 분석하여, **권한이 없거나 플랫폼 제약으로 사용할 수 없는 API 항목**을 정리한 문서입니다.

이 문서는 SSAFY Mattermost 기반의 통합 워크스페이스를 설계할 때 기술 의사결정의 기초 자료로 활용됩니다.

---

## 1. 종합 요약

| 검증 단계 | API 기능 | HTTP Endpoint | 검증 결과 | 주 원인 분석 | 연동 가능 여부 |
| :--- | :--- | :--- | :---: | :--- | :---: |
| **P0** | bot 계정 가용성 조회 | `GET /bots` | **실패 (403)** | 개인용 토큰(PAT) 권한 부족 (`read_bots` 등 누락) | **조건부 가능** (권한 추가 필요) |
| **P0** | 채널 북마크 조회 | `GET /channels/{id}/bookmarks` | **실패 (501)** | 라이선스 제약 (북마크 기능 미지원) | **불가능** |
| **P1** | 팀 검색 | `POST /teams/search` | **실패 (501)** | 공개전용 팀 검색 페이징 미구현 | **우회 가능** (전체 조회 후 자체 필터링) |
| **P1** | 게시글 검색 | `POST /teams/{id}/posts/search` | **실패 (400)** | 스크립트 파라미터 유효성 오류 (검색어 누락) | **가능** (정상 요청 시 호출 가능) |
| **P1** | 플레이북 가용성 조회 | `GET /plugins/playbooks/...` | **실패 (404)** | 플레이북 플러그인 비활성화 | **불가능** |

---

## 2. 상세 실패 분석 및 대안

### 2.1. bot 계정 가용성 조회 (`GET /bots`)
* **상태 코드:** `403 Forbidden`
* **에러 메시지:** `"403 작업을 할 수 있는 권한이 없습니다. (권한 부족 — 필요 permission 확인. manage_webhooks/read_bots 등)"`
* **원인 분석:**
  * 현재 인증에 사용 중인 Personal Access Token(PAT)의 권한 수준(Role)이 `system_user`로 제한되어 있어, 전체 봇 계정 목록 조회를 허용하는 `read_bots` 권한이 누락된 것으로 판단됩니다.
* **비즈니스 영향:**
  * 대시보드 등에서 현재 팀에 연동되어 있는 활성 봇 계정 목록을 파악하거나, 신규 봇 가용성을 자동으로 점검하기 어렵습니다.
* **해결 방안 및 대안:**
  * **방안 A (권한 획득):** Mattermost 시스템 관리자에게 봇 조회 권한(`read_bots`)을 포함한 토큰 재발급을 요청합니다.
  * **방안 B (우회):** 봇 목록 조회를 생략하고, 통합 워크스페이스에 연동될 봇의 ID(또는 Username)를 설정 파일(`Config`)을 통해 정적으로 관리합니다.

### 2.2. 채널 북마크 조회 (`GET /channels/{channel_id}/bookmarks`)
* **상태 코드:** `501 Not Implemented`
* **에러 메시지:** `"501 해당 라이선스에서는 채널 북마크 기능을 지원하지 않습니다."`
* **원인 분석:**
  * 채널 북마크 기능은 Mattermost 특정 버전(v9.5+) 혹은 엔터프라이즈(E20/Professional) 이상의 상위 등급 라이선스가 활성화되어 있어야 동작합니다. SSAFY Mattermost 서버는 해당 등급의 라이선스를 적용하지 않았거나 해당 기능이 지원되지 않는 구버전/무료 에디션 상태인 것으로 해석됩니다.
* **비즈니스 영향:**
  * 채널 내에서 핀(Pin)된 주요 게시물이나 링크 등의 "북마크" 목록을 통합 워크스페이스 대시보드로 연동하여 가져올 수 없습니다.
* **해결 방안 및 대안:**
  * 북마크 대신 기존의 **채널 고정 메시지(Pinned Posts)** API인 `GET /channels/{channel_id}/pinned`를 활용하여 주요 공지사항 및 링크를 가져오는 구조로 우회합니다.

### 2.3. 팀 검색 (`POST /teams/search`)
* **상태 코드:** `501 Not Implemented`
* **에러 메시지:** `"501 공개전용 팀 검색에는 페이징이 구현되지 않았습니다."`
* **원인 분석:**
  * Mattermost 내부 검색 구현상, 공개전용 팀 검색을 수행할 때 페이징 처리(`page`, `per_page` 등)를 지원하지 않는 제약이 있거나 서버 구성상 막혀 있는 것으로 보입니다.
* **비즈니스 영향:**
  * 팀 이름 키워드를 통해 동적으로 서버 전체의 팀을 조회하는 UI 기능을 직접 구현하기 까다롭습니다.
* **해결 방안 및 대안:**
  * 현재 사용자의 소속 팀 목록 조회(`GET /users/me/teams`) API는 **성공(200 OK)**하므로, 서버에 검색 쿼리를 던져 필터링하는 대신 **내 소속 팀 전체 목록을 메모리에 로드한 뒤 클라이언트가 필터링**하는 방식으로 안전하게 구현할 수 있습니다.

### 2.4. 플레이북 가용성 조회 (`GET /plugins/playbooks/api/v0/playbooks`)
* **상태 코드:** `404 Not Found`
* **에러 메시지:** `"404 죄송합니다, 페이지를 찾을 수 없습니다. (리소스 없음 — team_id/channel_id/post_id 또는 기능 비활성화 확인)"`
* **원인 분석:**
  * Mattermost의 Incident Collaboration 플러그인(Playbooks)이 서버 설정에서 비활성화되어 있거나 self-hosted 인스턴스에 설치되지 않아 Endpoint 자체가 존재하지 않는 상태입니다.
* **비즈니스 영향:**
  * 팀 빌딩 시 체크리스트 제공, 프로세스 자동화 템플릿(Playbook) 연동 가설을 검증할 수 없습니다.
* **해결 방안 및 대안:**
  * SSAFY Mattermost 내의 플레이북 연동은 불가능한 것으로 확정하고, 자동화 체크리스트 등은 Mattermost의 기본 메시지 포맷(인터랙티브 메시지 버튼)이나 외부 Notion API 등을 결합하여 별도 시스템으로 구현해야 합니다.

### 2.5. 게시글 검색 (`POST /teams/{team_id}/posts/search`)
* **상태 코드:** `400 Bad Request`
* **에러 메시지:** `"400 요청 본문에 terms이(가) 없거나 유효하지 않습니다."`
* **원인 분석 (구현 제약 아님):**
  * `test_p1_readonly.py`에서 검색어가 비어 있는 `json_body={"terms": "", ...}` 상태로 호출하여 발생한 단순 파라미터 유효성 에러입니다.
* **연동 가능성:**
  * 권한 부족이 아닌 단순 클라이언트 데이터 포맷 에러이므로, 실제 검색 키워드(예: `{"terms": "테스트", ...}`)를 탑재하여 호출하면 정상 동작할 것으로 예상됩니다. 추후 필요시 정상 호출을 검증할 수 있습니다.

---

## 3. 향후 설계 및 의사결정 반영 사항

1. **Mattermost SDK 개발 범위 축소:**
   * 연동 범위에서 **Playbook 플러그인** 및 **Bookmarks API**는 완전히 제외합니다.
   * 필요시 대체 수단으로 기본 메시지 API, Pinned Posts API, Notion DB 연동을 조합합니다.
2. **토큰 권한 협의:**
   * 통합 워크스페이스의 봇 계정 모니터링 가설을 포기할 수 없는 경우, SSAFY 인프라 관리 조직에 `read_bots` 권한이 가용한 System Admin 대행 토큰 협의를 진행해야 합니다. 협의가 어려울 경우 정적 매핑으로 처리합니다.
3. **API 에러 방어 코드 구성:**
   * 403 Forbidden(권한 부족) 혹은 501/404(기능 미지원) 발생 시, 애플리케이션 전체가 다운되지 않고 해당 위젯만 비활성화("Mattermost 설정에 의해 지원되지 않는 기능입니다" 문구 출력 등)되도록 예외 처리를 철저히 설계합니다.
