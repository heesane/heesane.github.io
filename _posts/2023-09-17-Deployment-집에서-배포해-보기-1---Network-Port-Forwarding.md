---
title: "[Deployment] 집에서 배포해 보기 (1) - Network Port Forwarding"
author: heesang
platform: 
date: 2023-09-17 14:42:54 +0900
categories: [Backend/Deployment, 모뎀, 배포, 포트포워딩, 홈네트워크]
tags: ["Backend/Deployment", "모뎀", "배포", "포트포워딩", "홈네트워크"]
toc: true
comments: true
---
<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="650" data-origin-height="350">
<span
data-url="https://blog.kakaocdn.net/dn/HsFCY/btsufZD6DZG/0qkk3a03lmkkkEQ61ECJ41/img.jpg"
data-lightbox="lightbox" data-alt="제발 되라"><img
src="https://blog.kakaocdn.net/dn/HsFCY/btsufZD6DZG/0qkk3a03lmkkkEQ61ECJ41/img.jpg"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FHsFCY%2FbtsufZD6DZG%2F0qkk3a03lmkkkEQ61ECJ41%2Fimg.jpg"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="650" data-origin-height="350" /></span>
<figcaption>제발 되라</figcaption>
</figure>

## 소개 {#소개 ke-size="size26"}

개발자에게 있어서 배포란, 자신이 만든 프로젝트를 인터넷에 공개하여
타인이 자신의 프로젝트를 사용하고 볼 수 있게 하는 것이라고 생각하면 될
것이다. 그런데 배포를 할려고 보면, 내 돈을 가져갈 생각밖에 없는 악마같은
AWS, Digital Ocean, CloudFlare.. 등등이 있다. 얘네들이 컴퓨터를 빌려주고
Linux기반으로 돌아가는 서버 컴퓨터에 SSH 원격 접속을 통해서 배포를 하게
된다. 그런데 여기서 발생하는 비용들이 때로는 비싸다고 느껴질 때! 바로
집에서 Port Forwarding을 통해서 배포를 할 수있다!!!

 

## How to 배포? {#how-to-배포 ke-size="size26"}

우선, 대한민국에 살면서 3사 통신사 인터넷을 사용하고 있는 집이라면
단전함 안에 모뎀이 들어 있을 것이다.

이 모뎀이 통신 3사같은 ISP(Internet Service Provider)가 제공하는
인터넷을 중계해주고, LAN선을 공유기에 연결해서 Wi-Fi를 사용하는 식으로
홈 네트워크가 구성되어 있을 것이다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="596" data-origin-height="345">
<span
data-url="https://blog.kakaocdn.net/dn/bfFqxS/btst5ORXBDO/rtdjVlIA9L5k41lR6vqVqk/img.png"
data-lightbox="lightbox" data-alt="홈 네트워크 예시"><img
src="https://blog.kakaocdn.net/dn/bfFqxS/btst5ORXBDO/rtdjVlIA9L5k41lR6vqVqk/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbfFqxS%2Fbtst5ORXBDO%2FrtdjVlIA9L5k41lR6vqVqk%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="596" data-origin-height="345" /></span>
<figcaption>홈 네트워크 예시</figcaption>
</figure>

위의 그림을 보면 이해하기 쉬울 거라고 생각한다. ISP를 통해 들어오는
인터넷을 모뎀을 통해 공유기로 전달하고, 무선 Wi-Fi를 사용해서 인터넷을
사용한다. 들어올 때 거치는 것을 보면 모뎀과 공유기를 거쳐서 인터넷이
들어오게 되는데 이런 것을 게이트 웨이라고 한다. 우리가 스마트 폰을
통해서 인터넷을 사용하는 것은 위 그림의 반대 순서라고 생각하면 될
것이다. 그렇다면 우리가 거실에 있는 공유기를 통해서 배포를 할려고하면
어떻게 해야할 까?

바로 포트 포워딩(Port Forwarding)이다!

 

## How to 포트 포워딩? {#how-to-포트-포워딩 ke-size="size26"}

모뎀 밑에 있는 WAN MAC 주소 끝자리 6개의 번호가 웹페이지에서 비밀번호로
사용하게 된다. 나중에 다시 모뎀을 확인하기에는 번거로우니까, 휴대폰에
저장해두는 것을 추천한다.

 

다음으로, WINDOW 기준 CMD 창에 \"ipconfig\"를 입력하면 여러 IP와
게이트웨이 등등 네트워크관련 정보들이 보이는데, SKT 기준으로
192.168.55.1을 통해 웹 페이지에 접근할 수 있다. 만약 다른 통신사
인터넷를 사용하고 있다면, 무선 LAN 어댑터 또는 유선 인터넷 IP를
확인해보면 알 수 있다. 또는 구글링을 통해서 알아 낼 수 있다!

------------------------------------------------------------------------

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="504" data-origin-height="419">
<span
data-url="https://blog.kakaocdn.net/dn/A3Egd/btsubLAkAuR/sgff8RLuotvOjZNQvEP5K0/img.png"
data-lightbox="lightbox" data-alt="SKT 로그인 화면"><img
src="https://blog.kakaocdn.net/dn/A3Egd/btsubLAkAuR/sgff8RLuotvOjZNQvEP5K0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FA3Egd%2FbtsubLAkAuR%2Fsgff8RLuotvOjZNQvEP5K0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="504" data-origin-height="419" /></span>
<figcaption>SKT 로그인 화면</figcaption>
</figure>

------------------------------------------------------------------------

ID는 [admin]{style="background-color: #ffc9af;"}, PASSWORD는 [\"이전에
말했던 6자리 번호 + \_admin\"]{style="background-color: #ffc9af;"} 로
접근하게 되면 다음과 같은 화면을 볼 수 있다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="797" data-origin-height="369">
<span
data-url="https://blog.kakaocdn.net/dn/c5C0s5/btsuelugL2D/unmIqoiDk7ufnaFJ98IOuK/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/c5C0s5/btsuelugL2D/unmIqoiDk7ufnaFJ98IOuK/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc5C0s5%2FbtsuelugL2D%2FunmIqoiDk7ufnaFJ98IOuK%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="797" data-origin-height="369" /></span>
</figure>

------------------------------------------------------------------------

네트워크 화면에서는 해당 컴퓨터의 사설 IP를 확인할 수 있다. 이후의
포트포워딩일 된 이후에 프론트엔드 서버나, 백엔드 서버를 실행하고 해당
IP + 해당 PORT로 접근하면 화면을 볼 수 있을 것이다.

 

NAT 에서는 포트포워딩, DMZ(DeMillitary Zone), VPN 같은 것을 설정할 수
있는데, 지금 해보려고 하는 것을 포트포워딩이니, 해당 메뉴로 이동하면
다음 화면을 볼 수 있을 것이다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="749" data-origin-height="262">
<span
data-url="https://blog.kakaocdn.net/dn/cpIp12/btsuqzLH3Yk/xY6y2vjD2EQksrmUwa9L9K/img.png"
data-lightbox="lightbox" data-alt="NAT로 이동!"><img
src="https://blog.kakaocdn.net/dn/cpIp12/btsuqzLH3Yk/xY6y2vjD2EQksrmUwa9L9K/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcpIp12%2FbtsuqzLH3Yk%2FxY6y2vjD2EQksrmUwa9L9K%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="749" data-origin-height="262" /></span>
<figcaption>NAT로 이동!</figcaption>
</figure>

------------------------------------------------------------------------

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="763" data-origin-height="221">
<span
data-url="https://blog.kakaocdn.net/dn/mZKmP/btst865EtTt/mf5jIIiYyY0LvLTHh1Mdr0/img.png"
data-lightbox="lightbox" data-alt="드디어 등장한 포트 포워딩"><img
src="https://blog.kakaocdn.net/dn/mZKmP/btst865EtTt/mf5jIIiYyY0LvLTHh1Mdr0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmZKmP%2Fbtst865EtTt%2Fmf5jIIiYyY0LvLTHh1Mdr0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="763" data-origin-height="221" /></span>
<figcaption>드디어 등장한 포트 포워딩</figcaption>
</figure>

로컬 IP는 처음에 확인한 IPv4 주소, 포트 범위는 포트포워딩 하고자 하는
포트, 로컬포트도 동일하게 설정하고 추가를 누르면, 모뎀에서의
포트포워딩이 완료된 것이다!!

 

여기까지 배포를 위한 포트 포워딩에 대해서 작성했는데, 위의 내용는
데스크탑에 유선 LAN 선을 통한 인터넷사용 기준으로 작성되었다. 만약
Wi-Fi를 통해서 노트북에서 포트 포워딩을 진행하고 싶으면, 위의 과정을 1번
더 진행해야 홈 네트워크에서 포트 포워딩이 된 것을 확인할 수 있을 것이다.

 

하지만, 여기까지 했다고 해서 완료된 것이 아니다. PC나 네트워트에서의
방화벽 설정을 추가적으로 해주어야 실제로 되는 것을 확인할 수 있으니,
다음편에 이어서 작성할 예정이다.
