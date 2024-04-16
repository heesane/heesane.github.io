---
title: "[Deployment] Docker 개념"
author: heesang
platform: 
date: 2023-09-03 16:35:30 +0900
categories: [Backend/Deployment, docker]
tags: ["Backend/Deployment", "docker"]
toc: true
comments: true
---
<figure class="imageblock widthContent"
data-ke-mobilestyle="widthOrigin" data-filename="blob"
data-origin-width="600" data-origin-height="350">
<span
data-url="https://blog.kakaocdn.net/dn/bv5Q67/btssN1LW85H/rme14ViSYYIIpvmcADnTA1/img.png"
data-lightbox="lightbox" data-alt="아주 귀여운 고래, Docker"><img
src="https://blog.kakaocdn.net/dn/bv5Q67/btssN1LW85H/rme14ViSYYIIpvmcADnTA1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbv5Q67%2FbtssN1LW85H%2Frme14ViSYYIIpvmcADnTA1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-filename="blob" data-origin-width="600"
data-origin-height="350" /></span>
<figcaption>아주 귀여운 고래, Docker</figcaption>
</figure>

## 귀엽긴 한데, Docker가 뭐야? {#귀엽긴-한데-docker가-뭐야 ke-size="size26"}

Docker는 컨테이너 기반의 오픈소스 가상화 플랫폼인데, 이렇게 설명하면
어려우니까 쉽게 말해서, 내가 작성한 코드, 내가 사용한 라이브러리,
의존성들을 하나의 패키지로 묶어서 소프트웨어를 일관되게 실행할 수 있게
해 줍니다!

Docker를 통해서 다른 팀원들이나, 다른 사랑과의 코드 공유 중에 발생하는
\"내 컴퓨터에서는 잘 돌아가는 데 왜\...\" 같은 문제를 예방할 수
있습니다.

## 사용하는 이유 {#사용하는-이유 ke-size="size26"}

처음에 개발을 시작할 때, 많은 사람들이 개발 환경을 구성하다가 수많은
오류를 맞이하게 됩니다. 그만큼 초기의 개발 세팅을 굉장히 중요하고,
어려운 일입니다. 이후에 개발이 조금 익숙해지면, 초기세팅은 어렵지
않지만, 배포 환경에 따른 종속성 문제를 맞이하게 됩니다. 특히, Java언어와
SpringBoot 프레임워크와 같은 초기 라이브러리 세팅이 중요한 프로젝트를
다룰 경우, 더욱 중요하고, 어려운 문제가 될 수 있습니다. 이러한 문제들을
Docker를 통해서 해결할 수 있습니다.

 

또한, Docker 내부에 Container를 여러 개 생성해서 하나의 프로젝트를
지지하는 

## Container와 Image {#container와-image ke-size="size26"}

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1262" data-origin-height="662">
<span
data-url="https://blog.kakaocdn.net/dn/yzR2z/btss3VvRLsv/T6K3SzYYi4u7UKhnXw0851/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/yzR2z/btss3VvRLsv/T6K3SzYYi4u7UKhnXw0851/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FyzR2z%2Fbtss3VvRLsv%2FT6K3SzYYi4u7UKhnXw0851%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1262" data-origin-height="662" /></span>
</figure>

위의 그림들을 보면 Containers와 Images라는 것이 Docke_Host 내부에
존재하게 되는데, Docker_Host는 Docker 프로그램 자체이고, 사용자가 CLI로
docker build\..., docker pull\..., docker run\... 과 같은 명령어를
입력하게 되면, Docker_Host에서는 해당 명령어를 Docker daemon으로
해석하여, 만약 사용자가 기존에 저장되어 있는 Image를 가져오려고 하면
Docker Hub에서 해당 이미지를 가져오고, 만약 사용자가 직접 만들 Image인
경우, Image를 만들기 위해 Dockerfile들을 기반으로 Image를 생산하게 된다.

``` {#code_1693768549459 .bash ke-language="bash" ke-type="codeblock"}
docker images
```

만약에, 어떤 명령어를 사용해서 Image를 만들거나, 가져왔다면 위의
명령어를 통해서 현재 자신이 갖고 있는 Image들과 버전에 대한 정보를
확인할 수 있다. 

 

그다음으로 Image를 기반으로 Container를 실행하게 되는데, 이 컨테이너는
사용자 OS와 분리되어 있는 환경을 가지고 있어서, Windows에서 Linux 환경을
세팅하는 식으로 사용할 수 있다.
