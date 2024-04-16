---
title: "[Deployment] Docker 내부구조"
author: heesang
platform: 
date: 2023-09-07 18:23:53 +0900
categories: [Backend/Deployment]
tags: ["Backend/Deployment"]
toc: true
comments: true
---
<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="600" data-origin-height="350">
<span
data-url="https://blog.kakaocdn.net/dn/SwytR/btss3IxeZxb/AHOFtmMQUwvZC0Ll0GN8rk/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/SwytR/btss3IxeZxb/AHOFtmMQUwvZC0Ll0GN8rk/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FSwytR%2Fbtss3IxeZxb%2FAHOFtmMQUwvZC0Ll0GN8rk%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="600" data-origin-height="350" /></span>
</figure>

이전의 Docker 글에서는 간단하게 Docker의 개념에 대해서만 알아보고 간단한
명령어 1개만 해봤습니다.

이번 글에서는 Docker의 컨셉에 대해서 자세하게 알아보는 글을 적어보도록
하겠습니다.

 

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1280" data-origin-height="1177">
<span
data-url="https://blog.kakaocdn.net/dn/OxVnX/btss3XacLoB/VCor7z9HDtuKge1VOzUKkK/img.png"
data-lightbox="lightbox"
data-alt="출처 https://gayuna.github.io/docker/docker/"><img
src="https://blog.kakaocdn.net/dn/OxVnX/btss3XacLoB/VCor7z9HDtuKge1VOzUKkK/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FOxVnX%2Fbtss3XacLoB%2FVCor7z9HDtuKge1VOzUKkK%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1280" data-origin-height="1177" /></span>
<figcaption>출처 https://gayuna.github.io/docker/docker/</figcaption>
</figure>

[Docker Client]{style="background-color: #c0d1e7;"} : 사용자가 Docker
CLI 또는 Compose에 입력한 명령어를 적절한 API Payload로 변환해서
dockerd에 post 요청을 하게 된다. 이때, /var/run/docker.sock 경로에 있는
Unix socket을 통해 docker daemon의 API를 호출하게 됩니다. 만약 이러한
연결이 되어 있지 않은 경우, 다음과 같은 에러 메시지를 받게 될 것입니다.

``` {#code_1693820910254 .livecodeserver style="background-color: #f8f8f8; color: #383a42; text-align: start;" ke-language="bash" ke-type="codeblock"}
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

위 오류는 현재 docker daemon과 통신하기 위한 socket에 연결할 수 없으니,
docker daemon이 실행 중인지를 확인 해보라는 메시지였던 것입니다. Windows
운영체제를 가진 데스크톱에서 docker desktop이 종료된 상태에서 터미널에
docker 관련 명령어를 입력할 시에 발생하는 문제입니다. docker desktop을
실행시킨 이 후에 다시 시도해 보면 정상적으로 동작하는 것을 확인할 수
있습니다.

 

[Dockerd (Docker daemon)]{style="background-color: #c0d1e7;"} :
dockerd는 통신의 상대방인 도커 데몬으로, 이미지의 관리, 이미지 빌드,
REST API, 인증, 보안, 코어 네트워킹, 오케스트레이션 등의 다양한 작업을
수행합니다. Docker 프로젝트가 커지게 되면서, dockerd로는 컨테이너를
실행하지 않습니다. 대신 dockerd에서 \'container를 실행해\' 라는 명령이
들어오면, containerd를 호출하게 됩니다.

 

[containerd]{style="background-color: #c0d1e7;"} : 컨테이너 데몬으로,
dockerd에서부터 분리되어 오픈소스로 운영되고있는 컨테이너 런타임입니다.
컨테이너 데몬이 실질적으로 컨테이너를 실행하는 역할을 맡습니다.
쿠버네티스에서 만든 CRI(Container Runtime Interface)를 구현하게 됩니다.
또한, runC를 사용하여 컨테이너의 수명 주기를 관장합니다.

 

[runC]{style="background-color: #c0d1e7;"} : 실제로 컨테이너를 만드는
기술들의 집합입니다. docker에서 컨테이너 기술을 개발하게 되면서 Linux의
namespace, control group들과 같은 기술들을 많이 사용하게 되었는데,
[[이들을 하나의 low-level component로 묶고 runC라고 이름붙였다고 합니다.
오픈소스로 기부되어 하나의 standalone 프로젝트로서 플랫폼에 관계없이
container를 구현하는 기술들을 가지고 있습니다. 실질적인 컨테이너도
여기서
생성됩니다.]{style="text-align: left;"} ]{style="color: #000000;"}

 

[[containerd-shim]{style="background-color: #c0d1e7;"} : 생성된
container에 관여하게 되는 레이어입니다. runC는 컨테이너를 생성한 후
종료되는데, 이 시점부터 containered-shim 이 컨테이너의 부모 프로세스가
됩니다. 여기서 container의 STDIN/OUT을 유지하거나, deamon에게
container의 종료를 보고하는 등의 작업을 담당하게
됩니다.]{style="color: #000000;"}

 

[docker의 내부 구조를 공부하게 되면서, 당장 이해하기 어려운 부분들이
있지만 대부분의 구조들이 docker, Inc에서 벗어나 오픈소스화 되어있는 것을
알 수 있었습니다.]{style="color: #000000;"}
