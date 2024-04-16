---
title: "[Deployment] 집에서 배포해보기 (2)- 인바운드 규칙과 방화벽 설정"
author: heesang
platform: 
date: 2023-09-21 01:06:16 +0900
categories: [Backend/Deployment]
tags: ["Backend/Deployment"]
toc: true
comments: true
---
:::: {ke-type="moreLess" text-more="더보기" text-less="닫기"}
[더보기]{.btn-toggle-moreless}

::: moreless-content
집에서 배포해보기 (1)편에서 공유기 및 모뎀 관련 설정을 진행하니까 안보신
분들은 보고 오세요!!
:::
::::

이번 글에서는 지난 글에 이어서 인바운드 규칙과 방화벽을 설정해 볼
예정입니다.

공유기와 모뎀이 모두 포트포워딩이 되어 있다는 가정하에 글을 작성합니다.

 

우선, 인바운드 규칙에 대해서 알아 보겠습니다.

## 인바운드 규칙이란? {#인바운드-규칙이란 ke-size="size26"}

다른 컴퓨터 또는 네트워크에서 자신의 컴퓨터로 네트워크 데이터가 들어올
수 있도록 규칙을 정하는 것을 \"인바운드 규칙\"이라고 합니다.

------------------------------------------------------------------------

인바운드 규칙이 있으면, 아웃 바운드 규칙도 있겠죠?

## 아웃바운드 규칙은? {#아웃바운드-규칙은 ke-size="size26"}

자신의 컴퓨터에서 네트워크 데이터가 다른 컴퓨터 혹은 네트워크로 나갈 수
있도록 규칙을 정의하는 것을 \"아웃바운드 규칙\"이라고 합니다

------------------------------------------------------------------------

이렇게, 네트워크에서 데이터가 향하는 방향에 따라서 규칙을 정해줘야
한다는 것을 알게 되었으니, 이번에는 직접해보면서 익히는 게 좋겠죠?

우선! WINDOW 기준으로, \"방화벽 및 네트워크\" 설정에 진입합니다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-filename="Screenshot 2023-09-19 at 00.48.55.JPG"
data-origin-width="890" data-origin-height="653">
<span
data-url="https://blog.kakaocdn.net/dn/zSau8/btsut4zbJUK/12tSfl1R2zkTz6jxzVRVX1/img.jpg"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/zSau8/btsut4zbJUK/12tSfl1R2zkTz6jxzVRVX1/img.jpg"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FzSau8%2Fbtsut4zbJUK%2F12tSfl1R2zkTz6jxzVRVX1%2Fimg.jpg"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-filename="Screenshot 2023-09-19 at 00.48.55.JPG"
data-origin-width="890" data-origin-height="653" /></span>
</figure>

고급 설정으로 들어가 줍니다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1045" data-origin-height="742">
<span
data-url="https://blog.kakaocdn.net/dn/c07o6S/btsuJcWW3s0/1Z9iI6gFPhkqZjQe39snI0/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/c07o6S/btsuJcWW3s0/1Z9iI6gFPhkqZjQe39snI0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc07o6S%2FbtsuJcWW3s0%2F1Z9iI6gFPhkqZjQe39snI0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1045" data-origin-height="742" /></span>
</figure>

왼쪽 메뉴부분에 위에서 알아봤던 \"인바운드 규칙\"과\"아웃바운드 규칙\"
메뉴가 보이는 것을 확인할 수 있습니다.

아웃바운드는 자신의 네트워크에서 어떤 포트만 외부 네트워크에 접근할 것
인지 정하는 것이기에, 이번에는 아웃바운드 설정은 건들지 않고, 인바운드
규칙 설정만 진행하겠습니다. 이어서 인바운드로 들어가겠습니다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="697" data-origin-height="285">
<span
data-url="https://blog.kakaocdn.net/dn/ZoKep/btsuekQEEa9/pLbS6f4sxfQz5gfgx0rRhk/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/ZoKep/btsuekQEEa9/pLbS6f4sxfQz5gfgx0rRhk/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FZoKep%2FbtsuekQEEa9%2FpLbS6f4sxfQz5gfgx0rRhk%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="697" data-origin-height="285" /></span>
</figure>

인바운드 규칙에서 새 규칙을 누르게 되면, 

 

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="773" data-origin-height="349">
<span
data-url="https://blog.kakaocdn.net/dn/zVKrf/btsuG3e0GSx/RdyZKJnV518KAdDDhiYLi1/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/zVKrf/btsuG3e0GSx/RdyZKJnV518KAdDDhiYLi1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FzVKrf%2FbtsuG3e0GSx%2FRdyZKJnV518KAdDDhiYLi1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="773" data-origin-height="349" /></span>
</figure>

위와 같은 설정으로 넘어가게 됩니다.

규칙 종류에서는 어떤 인바운드 규칙을 설정할 것인지 정하게 되고,
포트포워딩을 설정할 예정이니까 포트를 선택하고 다음으로 넘어가겠습니다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="808" data-origin-height="393">
<span
data-url="https://blog.kakaocdn.net/dn/cMQ3iR/btsuAsTRaBT/f1IrKTF5MmKe9GhzVaDys1/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/cMQ3iR/btsuAsTRaBT/f1IrKTF5MmKe9GhzVaDys1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcMQ3iR%2FbtsuAsTRaBT%2Ff1IrKTF5MmKe9GhzVaDys1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="808" data-origin-height="393" /></span>
</figure>

어떤 통신을 사용하여 포트와 네트워크에 적용시킬 것인지에 대한 설정하는
화면으로 넘어왔는데, HTTP 통신을 통해 배포를 하고 싶어서 포트포워딩을
하고 있으니까 규칙은 TCP로, 포트는 API 문서를 보여주기 좋은 8000번
port로 설정해보겠습니다.

그 다음으로 작업, 프로필, 이름같은 경우는 중요한 부분은 아니니
넘어가도록 하겠습니다.

 

이렇게 포트 포워딩을 완료한 상태에서 간단하게 배포가 잘 되었는지를
확인해 보겠습니다.

FastAPI로 빠르게 \"Hello World!\"만 띄어보겠습니다.

우선 FastAPI 라이브러리를 설치하고, FastAPI를 실행시켜줄 비동기 웹
서버가 필요하므로 다음과 같은 명령어를 통해 필요한 라이브러리를 설치해
줍니다.

``` {#code_1695224877946 style="background-color: #f8f8f8; color: #383a42; text-align: start;" ke-language="python" ke-type="codeblock"}
# main.py
pip install fastapi uvicorn
```

위의 명령어를 통해서 설치가 완료되었다면, 아래와 같이 코드를 입력합니다.

``` {#code_1695224663146 style="background-color: #f8f8f8; color: #383a42; text-align: start;" ke-language="python" ke-type="codeblock"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def mainpage():
    return "Hello World!"
```

그 다음에 터미널 창에 uvicorn main:app \--reload \--port 8000 명령어를
입력 해 보겠습니다.

간단하게 명령어를 설명해 보자면,

uvicorn : 비동기 방식으로 웹 서버를 운영하는데 \~

main:app : main.py 코드 안에 있는 app 이라는 FastAPI() 객체를\~

\--reload : 파일이 변동되면 자동으로 새로고침하고 \~

\--port 8000 : 8000번 포트를 통해서\~

라는 뜻입니다. 8000번 포트를 통해서 Hello World!가 출력 되겠죠? 실행해
보겠습니다.

http://IP:PORT로 접속하면 됩니다!

<figure class="imageblock alignLeft" data-ke-mobilestyle="widthOrigin"
data-origin-width="183" data-origin-height="72">
<span
data-url="https://blog.kakaocdn.net/dn/endDJ2/btsuSmF8kQs/8DtwnFKHQu8Kb3YbzEjDX1/img.png"
data-lightbox="lightbox" data-alt="Hello World!"><img
src="https://blog.kakaocdn.net/dn/endDJ2/btsuSmF8kQs/8DtwnFKHQu8Kb3YbzEjDX1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FendDJ2%2FbtsuSmF8kQs%2F8DtwnFKHQu8Kb3YbzEjDX1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="183" data-origin-height="72" /></span>
<figcaption>Hello World!</figcaption>
</figure>

이제 배포가 되어 있는 것을 두 눈으로도 확인 할 수 있습니다.

 

저번 글을 통해서 집에서 홈 네트워크를 구성하고, 포트 포워딩을 통해서
배포할 준비를 했으며,

이번 글을 통해 실제 배포를 하고, 휴대폰, 다른 데스크탑, 노트북에서
접속이 되는 것을 확인할 수 있었습니다.

 
