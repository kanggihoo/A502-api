# 2. Get metadata

## 기본 정보
- **기능**: 서버의 SAML 메타데이터를 조회한다.
- **Endpoint**: `GET /api/v4/saml/metadata`
- **인증**: Bearer Token 불필요
- **권한**: 없음

## 설명
서버에서 SAML 메타데이터를 조회한다. 서버에 SAML이 올바르게 설정되어 있어야 한다.

## Request

파라미터 없음.

## Response

### 200 - SAML metadata retrieval successful
SAML 메타데이터가 문자열로 반환된다.

```json
"string"
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 501 | 명시되지 않음 |

## 주의 사항
- 서버에 SAML이 설정되어 있지 않으면 사용할 수 없다.

---

# 3. Get metadata from Identity Provider

## 기본 정보
- **기능**: Identity Provider로부터 SAML 메타데이터를 조회한다.
- **Endpoint**: `POST /api/v4/saml/metadatafromidp`
- **인증**: Bearer Token 불필요
- **권한**: 없음

## 설명
지정한 URL의 Identity Provider(IdP)로부터 SAML 메타데이터를 가져온다. 서버에 SAML이 올바르게 설정되어 있어야 한다.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| saml_metadata_url | string | No | SAML IdP 데이터를 가져올 URL |

```json
{
  "saml_metadata_url": "string"
}
```

## Response

### 200 - SAML metadata retrieval successful
SAML 메타데이터가 문자열로 반환된다.

```json
"string"
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 501 | 명시되지 않음 |

## 주의 사항
- 서버에 SAML이 설정되어 있지 않으면 사용할 수 없다.
