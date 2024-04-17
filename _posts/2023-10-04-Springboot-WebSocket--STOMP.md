---
title: "[Springboot] WebSocket & STOMP"
author: heesang
platform: 
date: 2023-10-04 17:08:56 +0900
categories: [Backend/Framework, Chatting, message, SpringBoot, Stomp, websocket, WS]
tags: ["Backend/Framework", "Chatting", "message", "SpringBoot", "Stomp", "websocket", "WS"]
toc: true
comments: true
---
<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="750" data-origin-height="343">
<span
data-url="https://blog.kakaocdn.net/dn/0hMFz/btswPWebkMz/PK7kxzCwlAb8SlkE8TeVPK/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/0hMFz/btswPWebkMz/PK7kxzCwlAb8SlkE8TeVPK/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F0hMFz%2FbtswPWebkMz%2FPK7kxzCwlAb8SlkE8TeVPK%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="750" data-origin-height="343" /></span>
</figure>

이번에 진행하는 프로젝트가 랜덤 채팅 관련 프로젝트인데, 이번에
WebSocket과 STOMP를 사용해서 채팅방을 구현하게 돼서, 한 번 글을 써보려고
한다. 이번 글에서는 STOMP를 사용해서 WebSocket을 구현할 예정이다.

구현에 대해서 얘기하기 전에 STOMP에 대해서 먼저 알고 가야 할 것 같다.

## STOMP란? {#stomp란 ke-size="size26"}

STOMP는 Simple Text Oriented Message Protocol의 약자로, 메시징 전송을
효율적으로 하기 위한 프로토콜로서, [Pub/Sub]{.underline} 기반으로
동작하게 된다. 메시지를 송신, 수신에 대한 처리가 명확하게 정의될 수
있다. 또한, WebSocketHandler를 직접 구현할 필요 없이 \@MessageMapping
같은 어노테이션을 사용해서 메시지 발행 시 엔드포인트를 별도로 분리해서
관리할 수 있다. 

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="539" data-origin-height="111">
<span
data-url="https://blog.kakaocdn.net/dn/emQdI7/btswgWT2p1f/McQ6hybEgnkAtL1IBsyJE1/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/emQdI7/btswgWT2p1f/McQ6hybEgnkAtL1IBsyJE1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FemQdI7%2FbtswgWT2p1f%2FMcQ6hybEgnkAtL1IBsyJE1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="539" data-origin-height="111" /></span>
</figure>

------------------------------------------------------------------------

Pub/Sub에 대해서도 알고 넘어가야, 구현할 때 버벅거리지 않을 수 있으니
간단하게 설명하자면, 신문을 구독한다고 생각하면 이해하기가 쉽다. 

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1197" data-origin-height="604">
<span
data-url="https://blog.kakaocdn.net/dn/Lxcxw/btswUV7hDm0/o9gCOG8H4WmKDsnqi2TYVk/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/Lxcxw/btswUV7hDm0/o9gCOG8H4WmKDsnqi2TYVk/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLxcxw%2FbtswUV7hDm0%2Fo9gCOG8H4WmKDsnqi2TYVk%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1197" data-origin-height="604" /></span>
</figure>

A, B, C Subscriber가 /topic/sports 라우트를 통해서 server를 구독하는
환경에서 publisher가 /pub/topic 경로로, server로 전송하게 되면,
server에서는 받은 데이터의 topic을 확인하여, 해당 topic을 구독하고 있는
구독자에게 \"Hello\"라는 데이터를 전달하게 된다.

 

신문으로 예시를 들면, Publisher는 각 신문사, Server는 배달회사,
Subscriber는 고객이라고 생각하면 이해하기 쉽다.

또한, Publisher의 역할을 수행하면서, Subscriber의 역할도 수행할 수
있는데, 채팅방의 경우 채팅을 보는 것뿐만 아니라, 채팅을 입력하여 전달할
수도 있어야 하기 때문에 이번 프로젝트에서는 subscriber도 publish의
역할을 수행하도록 해서 채팅 기능을 구현했다.

 

## 구현 {#구현 ke-size="size26"}

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="783" data-origin-height="267">
<span
data-url="https://blog.kakaocdn.net/dn/rrPtU/btsv91hyatu/zdHJBLkxN7ggi6fPhGJVdK/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/rrPtU/btsv91hyatu/zdHJBLkxN7ggi6fPhGJVdK/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FrrPtU%2Fbtsv91hyatu%2FzdHJBLkxN7ggi6fPhGJVdK%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="783" data-origin-height="267" /></span>
</figure>

Sprinboot에서는 websocket 라이브러리만 추가해도 STOMP 관련 라이브러리도
설치가 된다.

다음으로 구현해야 하는 것이 WebSocketConfig 파일이다.

``` {#code_1696403262955 .java ke-language="java" ke-type="codeblock"}
@Configuration
@EnableWebSocketMessageBroker

public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {

    @Override
    public void configureMessageBroker(MessageBrokerRegistry registry) {
        registry.enableSimpleBroker("/queue", "/topic");
        registry.setApplicationDestinationPrefixes("/app");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws/chat").setAllowedOriginPatterns("*").withSockJS();
    }
}
```

웹소켓 서버의 엔드포인트로 /ws/chat로 정의하였다.

 

클라이언트 사용자는 /queue, /topic으로 정의되어있는
registry.enableSimpleBroker를 통해 /topic/{topicname}을 통해서 topic을
구독하도록 했다. 메시지를 전송할 때는 /app/chat/message를 통해서
전달하도록 만들었다.

여기까지 코드를 작성하면, Spring Framework가 자동으로 STOMP 통신이
가능한 웹소켓 서버를 실행시켜 준다.

아래와 같이 Message Type을 지정하고 진행한다.

 

``` {#code_1696406576497 .typescript style="background-color: #f8f8f8; color: #383a42; text-align: start;" ke-type="codeblock" ke-language="java"}
package unknown.backend.dev.model;
// WebSocketChattingModel

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class ChatMessage {
    public enum MessageType {
        ENTER, TALK
    }

    // MessageType
    // JOIN, CHAT, LEAVE
    private MessageType type;

    // RoomId
    private String roomId;

    // Sender
    private String sender;

    // Content
    private String message;

}
```

``` {#code_1696406526474 .crystal style="background-color: #f8f8f8; color: #383a42; text-align: start;" ke-language="java" ke-type="codeblock"}
package unknown.backend.dev.controller;

import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.simp.SimpMessageSendingOperations;
import org.springframework.web.bind.annotation.RestController;

import lombok.RequiredArgsConstructor;
import unknown.backend.dev.model.ChatMessage;

@RestController
@RequiredArgsConstructor
public class ChatController {

    private final SimpMessageSendingOperations sendingOperations;

    @MessageMapping("/chat/message")
    public void enter(ChatMessage message) {
        if (ChatMessage.MessageType.ENTER.equals(message.getType())) {
            message.setMessage(message.getSender() + "님이 입장하였습니다.");
        }
        sendingOperations.convertAndSend("/topic/chat/room/" + message.getRoomId(), message);
    }
}
```

우선 STOMP 통신을 통해 들어오는 내용을 처리하기 위해서 ChatController를
만들어보자.

위에서 pub을 할 때, /app을 통해서 한다고 했는데, 여기서 \@MessageMapping
어노테이션을 통해서 /chat/message로 정의했다. 실제 라우팅은
/app/chat/message로 publish를 진행한다.

위의 코드의 콘셉트는 채팅방에 입장하는 부분을 컨트롤하기 때문에,
/topic/chat/name/{roomId}를 통해서 subscribe 한다.

 

 

테스트는 WebSocket을 가능하게 하는 크롬 플러그인을 사용해야 하는데,
일반적인 플러그인으로는 STOMP 통신이 불가능해서, Apic을 사용하여 STOMP
통신을 해보면 된다.

### Publisher {#publisher ke-size="size23"}

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1548" data-origin-height="570">
<span
data-url="https://blog.kakaocdn.net/dn/lXJ0w/btswJCAolHE/1xCKFkRrQzoHBO04GWPSTK/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/lXJ0w/btswJCAolHE/1xCKFkRrQzoHBO04GWPSTK/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlXJ0w%2FbtswJCAolHE%2F1xCKFkRrQzoHBO04GWPSTK%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1548" data-origin-height="570" /></span>
</figure>

### Subscriber {#subscriber ke-size="size23"}

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1557" data-origin-height="571">
<span
data-url="https://blog.kakaocdn.net/dn/cFekEp/btsw6ClQ1E9/ykzhN3VWHpR9I10RuKOOUK/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/cFekEp/btsw6ClQ1E9/ykzhN3VWHpR9I10RuKOOUK/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcFekEp%2Fbtsw6ClQ1E9%2FykzhN3VWHpR9I10RuKOOUK%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1557" data-origin-height="571" /></span>
</figure>

/ws/chat을 통해서 핸드쉐이킹을 진행하고 STOMP 프로토콜로 MessageType에
정의했던 형식으로 메시지를 보내면 Subscriber 쪽에서 메시지가 정상적으로
도착하는 것을 알 수 있다.

------------------------------------------------------------------------

 

이번 프로젝트는 랜덤 채팅 프로젝트인데, 이렇게 설계한 STOMP 프로토콜을
활용한 웹소켓 채팅을 고도화하여서 구현할 수 있을 것 같다.

 
