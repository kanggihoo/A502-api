# 소개 
SSAFY openAPI는 SSAFY 학습 플랫폼에서 제공하는 핵심 기능 중 하나 
SSAFY 학습 플랫폼에서 제공하는 콘텐츠, 데이터, 서비스를 활용할 수 있도록 XML , JSON 형태로 제공하는 REST 방식의 인터페이스 

SSAFY 교육생은 프로젝트 개발시 SSAFY Open API를 통해 공개된 데이터, 서비스를 활용하여 창조적이고 다양한 컨텐츠 직접 개발 가능. 

# OpenAPI 구성 

1. Provider 서비스 등록 (SSAFY 서버 (Auth Server , SSAFY GIT) <-> 서비스 제공자)
2. Provider 서비스 등록완료 

3. 클라이언트 어플리케이션 등록요청  Clent -> SSAFY 서버 
4. 클라이언트 어플리케이션 등록 완료 SSAFY 서버 -> Client 
5. API Key 신청, 권한 요청 Client -> SSAFY 서버 
6. API Key 발급 Client <- SSAFY 서버 
7. API 요청(API Key) Client -> SSAFY 서버 
8. API Key 검증 
9. API 요청 및 응답 <-> 서비스 제공자(Provider Service)
10. API 응답 SSAFY 서버 -> Client 

- Client 서비스는 Open API 를 통해 기능 및 데이터를 요청하는 어플리케이션, 팀, 사용자를 포함. 

- Provider 서비스는 OpenAPI를 통해 기능 및 데이터를 제공하는 서비스로, SSAFY GIT 자체 서비스와 미니앱 형태의 교육생이 개발한 우수 프로젝트를 포함 

- SSAFY GIT은 OpenAPI를 통해 자체 기능을 제공함과 동시에, Open API를 제공하는 내/외부 서비스를 관리하며 , 클라이언트 서비스 요청에 대한 권한 체크 등 OpenAPI의 전반을 관리합니다. 

## Open API 목록 
SSAFY 학습 플랫폼에서 제공하는 OpenAPI 목록입니다. 
1. SSAFY 로그인 : 교육생 프로젝트에서 SSAFY GIT 연동 SSO 로그인 기능 구현 
2. SSAFY 프로필 : 이름, 이메일, 기수, 지역, 퇴소여부, 1학기 분반, 팀 정보 조회 
3. SSAFY 메시지 : Mattermost의 채널, 게시물 , 사용자 등록 및 조회 기능 제공 
4. SSAFY 데이터 : SSAFY 데이터셋 제공(데이터별 사용 신청 후 사용가능)

# REST API 

## REQUEST 
SSAFY open API REQUEST 규격을 구성하는 요소는 다음과 같습니다. 
메서드(Method) : SSAFY Open API 호출 시 사용해야할 HTTP 요청 메서드 
호스트(Host) : 요청을 받는 SSAFY Open API 서버의 도베인 

## RESPONSE 

### 1. 응답형식 
SSAFY Open API는 요청에 대해 응답 코드와 응답 필드로 구성된 응답을 제공.

### 2. 상태 코드 
200 : OK 
400 : Bad Request 
401 : 인증 오류 
403 : 권한 오류  
429 : 지정된 시간에 너무 많은 요청 
500(Internal Server Error) : 시스템 오류 
502(Bad Gateway) : 시스템 오류(서버가 요청 처리하는데 필요한 응답을 얻기 위해 게이트 웨이로 작업하는 동안 잘못된 응답을  수신)
503(Service Unavailable) :  서비스 점검중 



# SSAFY 어플리케이션 가이드 

## 1. 개요 
- 본 문서는 개발자 센터에서 제공하는 어플리케이션 신청, 설정 , 사용 가이드 
- 개발자 센터 내 서비스를 사용하기 위해서는 개발 프로젝트를 대신하여 시스템 연동을 위한 어플리케이션 등록이 필요 
- 어플리케이션이 등록된 이후 개발자 센터 메뉴에서 프로젝트에 맞게 어플리케이션을 설정하고, 서비스 연계 활용이 가능. 

## 2. SSAFY 어플리케이션 등록 
- 연동하여 사용하고자 하는 경우 교육 운영자에게 본인의 팀 프로젝트에 대해 어플리케이션 등록 신청을 합니다. 
- 교육 운영자는 내부 승인 단계를 거쳐 SSAFY GIT에 어플리케이션 등록 후 결과를 알림 

### 3. SSAFY 어플리케이션 확인 

어플리케이션이 SSAFY GIT에 등록이 완료 되었다면 다음과 같은 정보 확인가능 

- OpenAPI Key와 SSO 연동을 위한 Id, Secret 정보를 확인 및 복사가능 
- SSAFY 로그인 서비스는 PCWEB / MOBILEWEB 등의 웹서비스 환경에서 지원 

### 4. 어플리케이션 설정 

#### 4.1 기본설정 
- 어플리케이션 도메인 
- 어플리케이션 실행 환경 
  - DEV : 개발 실행 환경(로컬 개발 또는 EC2 개발 환경 )
  - STG : 검증 실행 환경 (SSAFY SUPER APP 실행 환경 내 배포된 어플리케이션 )
  - PRD는 운영 실행환경을 의미하며 실제 교육생 프로젝트가 SSAFY GIT과 연동하여 운영환경에서 서비스하기에 적합하다고 판단되는 경우 운영 시스템으로 전환 후 운영자가 상태를 변경하게 되며, 교육생이 개발로 설정 할수 없는 옵션 

#### 4.2 어플리케이션 서비스 설정 -SSAFY 로그인 
- SSAFY 로그인 설정은 개발자 센터 -> 내 어플리케이션 -> 서비스 설정 -> SSAFY 로그인 에서 가능 
- 설정 가능한 항목은 다음과 같음 
  - 클라이언트 설정 
  - Redirect URL 
  - 개인정보 동의 설정 
- 클라이언트 설정은 아래와 같음. 
  - 초기 상태는 SSO 클라이언트가 발급되지 않은 상태로 발급 버튼을 클릭하여 어플리케이션의 클라이언트 발급 
  - 외부 유출 우려 되는 경우 재발급 가능 
- Redirect URL 설정은 아래와 같음. 
  - Rediect URL 설정 버튼을 클릭하면 URI 입력 팝업이 출력 
  - 본인 프로젝트 실행 환경에 맞는 URI 정보 입력(최대 5개)
  - 개인 로컬 PC에서 실행하는 경우면 http://localhost:8080/sso/providers/ssafy/callback/를 입력합니다. 
  - 원격 실행 환경이면서 도메인이 할당되지 않은 환경이라면 http://00.00.00.00:8080/sso/providers/ssafy/callback와 같이 IP 기준으로 
  - 도메인이 할당 된 환경이라면 https://baseproject.ssafyapp.com/sso/providers/ssafy/callback 과 같은 형태로 입력 
  - /sso ~ 이하는 개발자 센터에서 제공하는 베이스 프로젝트를 기준으로 제공한 예시 이므로 각 프로젝트 내 알맞은 Redirect URL로 입력 
  - Redirect URI 설정 완료 후 "미리보기" 클릭시 인증코드 발급 미리보기 팝업이 출력 
  - 테스트용 콜백 명령어를 복사 & 실행하여 실행중인 프로젝트와 Redirect URI 통신 테스트가 가능 

#### 4.3 어플리케이션 서비스 설정 -Open API 
- SSAFY open API 설정은 개발자센터 -> 내 어플리케이션 -> 서비스 설정 -> Open API 에서 가능 
- 설정 가능 항목은 아래와 같음 
  - Open API Key 
  - 기능 설정 
- Open API Key 설정은 아래와 같음. 
  - 초기 상태는 미 사용 형태로 , 사용 신청 버튼을 클릭하여 어플리케이션의 open API Key 발급 
  - 외부 유출 우려시 재발급 가능 


