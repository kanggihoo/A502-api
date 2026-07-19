# 단일 EC2 MVP 인프라·배포 운영 설계

## 상태와 범위

- 상태: 논의 기반 초안. 아래 **확정 결정**은 구현 기준으로 사용하고, **추가 결정 필요** 항목은 인프라 구현 전에 확정한다.
- 대상: 6인·약 5주 MVP, 단일 `t3.xlarge` EC2, GitLab self-hosted 환경과 GitLab Container Registry.
- 서비스 코드: Next.js frontend, Spring Boot backend, FastAPI(및 필요 시 worker). 서비스는 각각 별도 repository로 관리한다.
- 운영 환경: 같은 EC2 안의 `test`와 `production`.
- 제외: Kubernetes, Terraform 중심 운영, GitOps controller, RDS/ElastiCache, 다중 EC2 고가용성, 무중단 배포 보장.

이 문서는 [단일 EC2 MVP 아키텍처](2026-07-13-single-ec2-mvp-architecture.md)의 배포·운영 세부 설계다.

## 확정 결정

1. 서비스는 독립적으로 image를 만들고 자기 서비스만 배포한다. frontend 변경이 Spring·FastAPI 전체 재배포를 일으키지 않는다.
2. 실제 운영 설정은 별도 `infra` repository가 소유한다.
3. CI/CD는 GitLab CI를 사용한다. GitLab Runner가 EC2의 SSH에 접근할 수 있다고 가정한다.
4. image는 GitLab Container Registry에 push한다. mutable한 `latest` 대신 commit SHA 또는 release version을 사용한다.
5. `develop` push는 test의 해당 서비스만 자동 배포한다. `main` merge는 production의 해당 서비스만 자동 배포한다.
6. EC2 배포는 GitLab CI job이 `deploy` 전용 사용자로 SSH 접속해 실행한다. EC2의 image polling은 사용하지 않는다.
7. 공개 reverse proxy는 Nginx 하나만 둔다. Nginx의 80/443만 host에 publish한다.
8. frontend는 Next.js SSR container로 운영한다. Browser의 API·SSE 요청은 같은 origin의 `/api/`, `/sse/`를 사용하고 Nginx가 Spring으로 전달한다.

## Repository 책임

### 서비스 repository

각 frontend, Spring, FastAPI repository는 다음만 소유한다.

- application source, test, `Dockerfile`
- image build·test·Registry push를 호출하는 `.gitlab-ci.yml`
- 자기 서비스의 health endpoint와 runtime contract
- FastAPI API와 worker를 함께 배포할 경우 동일 SHA image를 쓰는 정의

서비스 repository는 production Compose, Nginx 설정, DB volume, 공통 secret을 직접 수정하지 않는다.

### `infra` repository

`infra` repository는 EC2 runtime의 단일 진실 원본이다.

```text
infra/
├─ compose.test.yml
├─ compose.prod.yml
├─ nginx/
│  ├─ nginx.conf
│  └─ conf.d/
├─ scripts/
│  ├─ deploy-service.sh
│  ├─ rollback-service.sh
│  ├─ backup-postgres.sh
│  └─ bootstrap-host.sh
├─ systemd-or-cron/
└─ docs/
   ├─ runbook-deploy.md
   ├─ runbook-rollback.md
   └─ runbook-restore.md
```

소유 범위는 Compose, Docker network/volume, Nginx·TLS, resource limit, health check, deployment·rollback script, backup·log rotation, host bootstrap, 운영 runbook이다. runtime `.env`와 private key는 repository에 넣지 않는다.

공통 GitLab CI template도 `infra` repository에서 제공할 수 있다. 서비스 repository는 이를 `include`해 image naming, SSH setup, deploy·rollback 형식을 통일한다. template 변경은 서비스 pipeline에 영향을 주므로 version/tag로 고정하고, 검증 후 올린다.

## CI/CD와 배포 흐름

### 표준 pipeline

```text
서비스 repository push
  → lint / unit test / 필요한 integration test
  → image build
  → GitLab Container Registry push: <service>:<commit-sha>
  → GitLab Runner SSH → EC2 deploy script
  → 해당 Compose service pull 및 recreate
  → health check / smoke check
  → 성공 기록 또는 직전 SHA rollback
```

- `develop`: test Compose project의 대상 service만 교체한다.
- `main`: production Compose project의 대상 service만 교체한다. 별도 수동 승인 단계는 두지 않는다.
- 모든 deploy job에는 `resource_group: test` 또는 `resource_group: production`을 둔다. 같은 환경의 배포가 겹치지 않는다.
- deploy script는 `<environment>`, 허용된 `<service>`, immutable `<image-tag>`만 받는다. 임의 shell 인자나 Compose project 이름을 받지 않는다.
- `docker compose pull <service>` 후 `docker compose up -d --no-deps <service>`로 대상만 교체한다. 의존 service를 함께 재시작하지 않는다.
- health check 실패 시 직전 정상 image SHA로 rollback한다. rollback 결과도 pipeline log와 운영 알림에 남긴다.
- production은 성공한 pipeline이 만든 image digest를 기록한다. 재배포·rollback은 tag가 아니라 기록한 digest/SHA를 기준으로 한다.

단일 Docker Compose는 rolling deployment를 제공하지 않는다. service 교체 순간의 짧은 502는 MVP에서 허용한다. health check와 빠른 rollback으로 영향을 제한한다.

### DB migration

- DB migration은 Spring 배포 pipeline의 단일 job에서만 수행한다.
- migration 성공 전 application container를 새 버전으로 바꾸지 않는다.
- migration은 이전 application 버전과 호환되게 작성한다. 컬럼 추가 → 새 코드 배포 → 이전 코드 제거 순서를 따른다.
- destructive migration, 대량 data migration, 복구 불가능한 schema 변경은 자동 production 배포에 넣지 않는다. 별도 backup·검토·runbook을 적용한다.

## Nginx와 network

### 외부 routing

```text
app.example.com
  /api/*, /sse/*  → prod-spring:8080
  그 외           → prod-frontend:3000

test.example.com
  /api/*, /sse/*  → test-spring:8080
  그 외           → test-frontend:3000
```

- HTTP 80은 HTTPS redirect와 Let's Encrypt HTTP-01 challenge만 처리한다.
- HTTPS 443은 Nginx가 TLS를 종료한다.
- `test.example.com`에는 Basic Auth와 `X-Robots-Tag: noindex`를 적용한다.
- FastAPI, PostgreSQL, Redis, MinIO는 public hostname이나 Nginx route를 갖지 않는다.
- API 인증·권한은 Spring이 담당한다. Nginx는 인증 진실 원본이 아니다.

### Docker network

```text
Nginx
 ├─ prod-edge : prod-frontend, prod-spring
 └─ test-edge : test-frontend, test-spring

prod-private : prod-spring, prod-fastapi, prod-postgres, prod-redis, prod-minio
test-private : test-spring, test-fastapi, test-postgres, test-redis, test-minio
```

- Spring은 해당 environment의 edge/private network 양쪽에 연결한다.
- FastAPI와 data store는 private network만 연결한다.
- Nginx를 제외한 service에는 host `ports:`를 설정하지 않는다.
- test와 production은 Compose project, network, volume, database, Redis, secret을 각각 분리한다.

### SSE proxy 기준

`/sse/` location에는 최소한 아래를 명시한다.

```nginx
proxy_http_version 1.1;
proxy_buffering off;
proxy_cache off;
proxy_read_timeout 3600s;
add_header X-Accel-Buffering no;
```

Spring의 SSE heartbeat 주기는 Nginx `proxy_read_timeout`보다 충분히 짧게 둔다. timeout, client disconnect, FastAPI cancel 전파는 Spring과 FastAPI contract로 함께 검증한다.

Nginx 설정 변경 pipeline은 `nginx -t`를 통과한 뒤 reload한다. 설정 오류로 proxy 전체가 중단되지 않게 한다. access/error log는 분리하고 rotation한다.

## Next.js 운영 기준

- multi-stage build와 Next `output: "standalone"`을 사용해 runtime image를 작게 유지한다.
- production은 `next dev`가 아닌 Node runtime process를 사용한다.
- frontend container는 `3000`만 Docker network에 열고 health endpoint를 제공한다.
- Browser는 `/api/...`, `/sse/...` 상대 경로로 Spring을 호출한다. CORS와 cross-domain cookie 구성을 만들지 않는다.
- `/_next/static/`의 hashed asset만 장기 cache(`public, immutable`)한다. HTML/SSR response는 cache하지 않는다.
- `NEXT_PUBLIC_*` 값은 build 시 image에 포함된다. 공개 값만 사용하고 secret은 절대 넣지 않는다.
- server-only runtime 값은 container `.env`로 주입한다. SSR에서 Spring을 호출하면 `INTERNAL_API_BASE_URL=http://prod-spring:8080`처럼 내부 주소를 쓰고, 필요한 user cookie와 request ID만 명시적으로 전달한다.

## 보안과 secret

- GitLab protected branch: `main`, production deploy job과 production variable은 protected로 지정한다.
- GitLab variables: masked, protected, environment scope(`test`/`production`)를 적용한다.
- GitLab Runner의 SSH key는 `deploy` 전용 EC2 사용자만 접근한다. root SSH를 금지한다.
- `deploy` 사용자의 `sudo`는 검증된 deploy/rollback script와 필요한 Docker 명령으로 제한한다.
- EC2 runtime secret은 host의 권한 `600` 파일 또는 Docker secret 대체 방식으로 관리한다. Git repository, image layer, application log에 넣지 않는다.
- GitLab Registry pull credential은 EC2에 최소 권한 deploy token으로 보관한다.
- Security Group/firewall은 80/443과 Runner에서 오는 22만 허용한다. 22의 source range는 가능한 좁힌다.
- GitHub OAuth token, LLM key, JWT/internal secret, DB password는 환경별로 분리한다. log와 error response에서 secret·사용자 입력을 redaction한다.

## 자원·data 운영

### 자원 보호

- production container의 CPU/RAM reserve를 먼저 정한다. test와 FastAPI analysis worker에는 낮은 limit을 설정한다.
- 분석 job 동시 실행 수는 production/test 전체에서 1개부터 시작한다.
- job workspace에는 용량, 파일 수, 실행 시간 상한을 둔다. 성공·실패·취소 뒤 cleanup하고 TTL cleanup도 둔다.
- Docker image, container log, workspace, PostgreSQL volume의 disk 사용량을 따로 관찰한다. 80% 도달 전 알림과 정리 절차를 둔다.
- T3 CPU credit, CPU/RAM, disk, container restart 횟수를 최소 운영 지표로 둔다.

### backup과 복구

동일 EC2의 PostgreSQL dump나 MinIO copy는 장애 대비 backup이 아니다. EC2 손실 시 test와 production 데이터가 함께 손실된다.

- 데모 단계에서는 이 위험을 명시적으로 수용할 수 있다.
- 실제 사용자 데이터·OAuth token을 받기 전에는 off-host PostgreSQL backup, retention, encrypt, 정기 restore test를 추가한다.
- 분석 산출물과 user data의 보존·삭제 기간을 정한다.
- DB restore는 실제 runbook과 연습 결과가 있어야 복구 수단으로 인정한다.

## 최소 관측·운영 절차

무거운 Grafana/ELK는 MVP에서 제외한다. 대신 다음을 운영 최소선으로 둔다.

- application structured log와 request/job correlation ID
- container health check와 restart policy
- deploy 성공·실패·rollback 알림
- Nginx access/error log rotation
- disk, CPU, RAM, T3 CPU credit, certificate expiry 확인과 알림
- `deploy`, `rollback`, `DB restore`, `service stop`, `disk cleanup` runbook
- 새 EC2에서 재현 가능한 `bootstrap-host.sh`

## 서비스 간 contract

- frontend는 FastAPI에 직접 접근하지 않는다. Browser와 SSR 모두 Spring을 사용자·권한 경계로 사용한다.
- Spring→FastAPI 호출은 connect/read timeout, retry 조건, idempotency key, cancel 전달을 명시한다.
- FastAPI 장애는 Spring의 무한 대기나 전체 service restart로 번지지 않아야 한다.
- 공개 job 상태와 결과의 진실 원본은 PostgreSQL이다. SSE는 실시간 알림 채널이며 재접속 시 REST로 복구한다.

## 추가 결정 필요

1. Nginx TLS 인증서 갱신 방식: Certbot container와 renewal scheduler의 실제 구성.
2. production/test별 CPU·RAM limit, analysis job 동시 실행 수, workspace disk 상한.
3. PostgreSQL backup 대상, RPO/RTO, retention, 암호화와 restore 책임자.
4. Nginx rate limit·connection limit 수치, body upload 상한, 기본 security header/CSP.
5. GitLab Runner의 실제 network source range와 EC2 SSH firewall rule.
6. Spring–FastAPI API versioning, retry·timeout·idempotency contract.
7. Next.js SSR에서 Spring 데이터를 가져오는 범위와 forwarded cookie 정책.

## 구현 순서

1. `infra` repository와 host bootstrap, production/test Compose skeleton을 만든다.
2. Nginx host routing, TLS, Basic Auth, SSE proxy 설정을 검증한다.
3. GitLab Registry와 `deploy` SSH user를 구성한다.
4. frontend부터 service별 표준 GitLab pipeline과 deploy/rollback script를 적용한다.
5. Spring, FastAPI/worker로 같은 pipeline을 확장하고 service contract·job 제한을 넣는다.
6. healthcheck, log rotation, disk monitoring, backup/restore runbook을 검증한다.
