# 1. Get brand image

## 기본 정보
- **기능**: 서버에 업로드된 브랜드 이미지를 조회한다.
- **Endpoint**: `GET /api/v4/brand/image`
- **인증**: Bearer Token 불필요
- **권한**: 없음

## 설명
이전에 업로드된 브랜드 이미지를 반환한다. 브랜드 이미지가 업로드된 적이 없으면 404를 반환한다.

## Request

파라미터 없음.

## Response

### 200 - Brand image retrieval successful
이미지 데이터가 반환된다 (문서상 string으로 표현됨).

```json
"string"
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 404 | 브랜드 이미지가 업로드되지 않음 |
| 501 | 명시되지 않음 |
