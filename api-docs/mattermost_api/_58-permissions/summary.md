# 1. Return all system console subsection ancillary permissions

## 기본 정보
- **기능**: 요청한 시스템 콘솔 subsection 권한들에 대응하는 ancillary(부속) 권한 목록을 조회한다.
- **Endpoint**: `POST /api/v4/permissions/ancillary`
- **인증**: Bearer Token 필요
- **권한**: 없음 (문서에 별도 권한 서술 없음, 조회 성격의 유틸리티 API)

## 설명
요청 본문으로 전달한 시스템 콘솔 subsection 권한 이름들에 대해, 해당 권한에 딸린 ancillary 권한들을 요청한 권한 목록에 덧붙여 반환하는 API이다. 최소 서버 버전은 9.10이다.

## Request

### Body
권한 이름 문자열 배열을 전달한다.

```json
[
  "string"
]
```

## Response

### 200 - Successfully returned all ancillary and requested permissions
요청한 권한과 그에 대응하는 ancillary 권한이 합쳐진 문자열 배열을 반환한다.

```json
[
  "string"
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |

## 주의 사항
문서에 Permissions 서술이 없어 일반 인증 사용자 기준 조회 유틸리티로 판정했다. 시스템 콘솔 권한 이름 매핑만 반환하며 시스템 설정을 변경하지 않는다.

---
