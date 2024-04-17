---
title: "[Springboot] 로그인 구현 & JWT (1) - JWT 개념"
author: heesang
platform: 
date: 2023-11-09 17:34:13 +0900
categories: [Backend/Framework, claim, Header, jsonwebtoken, JWT, Payload, SpringBoot]
tags: ["Backend/Framework", "claim", "Header", "jsonwebtoken", "JWT", "Payload", "SpringBoot"]
toc: true
comments: true
---
<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="750" data-origin-height="343">
<span
data-url="https://blog.kakaocdn.net/dn/mL96Q/btsz1R8TGnB/nxrkKnQvDq8F5xSFypR1n0/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/mL96Q/btsz1R8TGnB/nxrkKnQvDq8F5xSFypR1n0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmL96Q%2Fbtsz1R8TGnB%2FnxrkKnQvDq8F5xSFypR1n0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="750" data-origin-height="343" /></span>
</figure>

프로젝트를 진행하다 보면, 필요에 의해서 로그인 기능을 구현해야할 때가
찾아온다.

로그인 기능을 구현하는 방법에는 Session을 이용하는 방식, Cookie를
이용하는 방식, Token을 이용하는 방식이 존재하는데, 이번 포스팅에서는
JWT의 개념에 대해서 알아보고 다음 포스팅에서 Login 기능을 구현할
예정이다.

------------------------------------------------------------------------

## JWT(Json Web Token) {#jwtjson-web-token ke-size="size26"}

JWT란 Json Web Token의 약자로 Json 형식을 사용하여 사용자의 정보를
저장하는 Claim 기반의 Web Token이다. 

JWT는 Token 자체를 정보로 사용하는 Self-Contained 방식으로 정보를
안전하게 전달한다.

 

### JWT의 구조 {#jwt의-구조 ke-size="size23"}

Header, Payload, Signature로 이루어져있으며, Json 형태인 각 부분은
Base64Url로 인코딩 되어있다.

또한, 각 부분들을 이어주기 위해서 각 부분 뒤에는 . 구분자를 통해
구분한다. 

 

### Header {#header ke-size="size23"}

Header에는 JWT 토큰의 alg, typ가 존재한다.

alg는 어떤 알고리즘을 사용하여 Hash 처리와 서명 및 토큰 검증에 사용할
것인지 지정하는 것이다.

typ은 토큰의 타입을 지정한다. 여기서는 typ은 JWT이다

 

### Payload {#payload ke-size="size23"}

Payload에는 토큰에서 사용할 정보의 조각인 Claim이 담겨있다.

Claim은 크게 3가지의 부분으로 나뉘어져 있으며, Registered Claim, Public
Claim, Private Claim으로 구성된다.

#### Registered Claim {#registered-claim ke-size="size20"}

토큰 정보를 표현하기 위해 이미 정해진 종류의 데이터들로, 선택적으로
작성이 가능하다.

또한 Json 형식으로 저장되기때문에, key와 value의 쌍으로 이뤄져있는데,
key는 JWT의 간결성을 위해서 길이 3의 String으로 설정한다.

 

#### Public Claim {#public-claim ke-size="size20"}

사용자 정의 클레임으로, 공개용 정보를 위해 사용된다.  

충돌방지를 위해서 URI 포맷을 사용한다.

#### Private Claim {#private-claim ke-size="size20"}

사용자 정의 클레임으로, 서버와 클라이언트 사이에 임의로 지정한 정보를 저장한다

### Example {#example ke-size="size23"}

[eyJhbGciOiJIUzI1NiJ9]{style="background-color: #f3c000;"}.[eyJFbWFpbCI6InRlZXMzMzU5QGdtYWlsLmNvbSIsImlhdCI6MTY5OTUxODQ4MSwiZXhwIjoxNjk5NjA0ODgxfQ]{style="background-color: #99cefa;"}.[VwdR5fAQFk1DD2ZfEfK3_5FZt0kPuOW8gMryWeZ55B0]{style="background-color: #c1bef9;"}

 

dot(.) 을 기준으로 Header, Payload, Signature로 구성된 Example JWT
Token이다.

 

------------------------------------------------------------------------

 
