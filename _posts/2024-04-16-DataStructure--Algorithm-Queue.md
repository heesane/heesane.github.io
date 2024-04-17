---
title: "[DataStructure & Algorithm] Queue"
author: heesang
platform: 
date: 2024-04-16 22:03:05 +0900
categories: [DataStructure Algorithm, Algorithm, datastructure, queue, 메서드, 선언, 알고리즘, 자료구조, 자바, 큐]
tags: ["DataStructure Algorithm", "Algorithm", "datastructure", "queue", "메서드", "선언", "알고리즘", "자료구조", "자바", "큐"]
toc: true
comments: true
---
<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="898" data-origin-height="251">
<span
data-url="https://blog.kakaocdn.net/dn/donIdT/btsGGOdfWyf/5o5thkDEmKJvIcxcfLJITk/img.png"
data-lightbox="lightbox" data-alt="자료구조 및 알고리즘"><img
src="https://blog.kakaocdn.net/dn/donIdT/btsGGOdfWyf/5o5thkDEmKJvIcxcfLJITk/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdonIdT%2FbtsGGOdfWyf%2F5o5thkDEmKJvIcxcfLJITk%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="898" data-origin-height="251" /></span>
<figcaption>자료구조 및 알고리즘</figcaption>
</figure>

------------------------------------------------------------------------

## 개요 - Queue란? {#개요---queue란 ke-size="size26"}

Queue의 사전적 의미는 어떤 것을 기다리는 사람, 차 등의 줄 또는 줄을 서서
기다리는 것을 의미한다.

이처럼 줄을 지어서 순서대로 처리되는 자료구조가 Queue라고 한다. 큐는
LIFO 구조를 사용하는 Stack과는 다르게 FIFO(First In First Out)의 구조를
가지는 자료구조이다.

 

FIFO는 가장 먼저 들어오는 데이터가 가장 먼저 나가는 구조를 의미한다. 

 

자료구조의 맨 뒤에 데이터가 들어오는 것을 Enqueue, 맨 앞에서 데이터가
나가는 것을 Dequeue라고 한다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1095" data-origin-height="504">
<span
data-url="https://blog.kakaocdn.net/dn/bqKZKs/btsGG6Ltsgw/O1E96Rx6mFSMMowqnByWk1/img.png"
data-lightbox="lightbox" data-alt="Queue"><img
src="https://blog.kakaocdn.net/dn/bqKZKs/btsGG6Ltsgw/O1E96Rx6mFSMMowqnByWk1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbqKZKs%2FbtsGG6Ltsgw%2FO1E96Rx6mFSMMowqnByWk1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1095" data-origin-height="504" width="593"
height="273" /></span>
<figcaption>Queue</figcaption>
</figure>

------------------------------------------------------------------------

## 특징 {#특징 ke-size="size26"}

-   FIFO 구조를 갖는다 : 가장 먼저 들어온 데이터가 가장 먼저 밖으로
    나가게된다.
-   큐의 앞쪽을 front, 큐의 뒤쪽을 rear로 정한다.
    -   Front에서는 Dequeue의 기능을, Rear에서는 Enqueue 기능을
        수행한다.
-   그래프의 BFS(너비 우선 탐색)에서 사용된다
-   컴퓨터의 버퍼에서 사용된다. 키보드입력을 큐를 사용해서 처리한다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="476" data-origin-height="230">
<span
data-url="https://blog.kakaocdn.net/dn/beUfzJ/btsGH4lYafb/7tkkIE3we2HrU9lTb1Rax1/img.png"
data-lightbox="lightbox" data-alt="enqueue"><img
src="https://blog.kakaocdn.net/dn/beUfzJ/btsGH4lYafb/7tkkIE3we2HrU9lTb1Rax1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbeUfzJ%2FbtsGH4lYafb%2F7tkkIE3we2HrU9lTb1Rax1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="476" data-origin-height="230" /></span>
<figcaption>enqueue</figcaption>
</figure>

 

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="436" data-origin-height="258">
<span
data-url="https://blog.kakaocdn.net/dn/6nnS1/btsGFhAvSqy/cvet6VAA92n2kenQcXuk21/img.png"
data-lightbox="lightbox" data-alt="dequeue"><img
src="https://blog.kakaocdn.net/dn/6nnS1/btsGFhAvSqy/cvet6VAA92n2kenQcXuk21/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F6nnS1%2FbtsGFhAvSqy%2Fcvet6VAA92n2kenQcXuk21%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="436" data-origin-height="258" /></span>
<figcaption>dequeue</figcaption>
</figure>

------------------------------------------------------------------------

## 구현 {#구현 ke-size="size26"}

Integer 부분만 바꾸면 해당 Type의 Queue를 선언하게 된다.

Queue는 LinkedList나 ArrayDeque를 통해서 구현하게 된다.

 

> Q. 왜 Stack이랑은 다르게 new Queue\<\>();는 안되나요?

 

A. Queue는 자바에서는 Interface로 선언되어 있어서, new Queue\<\>()를
사용하려면, 해당 인터페이스 내부에 선언된 모든 메서드들을
오버라이딩해야할 필요가 있습니다.

하지만 LinkedList와 ArrayDeque에는 해당 내용들이 모두 오버라이딩 되어
있어, 아래와 같은 방식으로 코드를 작성하면 됩니다.

 

``` {#code_1713271474923 .java ke-language="java" ke-type="codeblock"}
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;

class Main{
    public static void main(String[] args) {
        Queue integerQueue = new LinkedList<>();
        Queue integerQueue2 = new ArrayDeque<>();

        integerQueue.add(1);
        integerQueue.add(2);
        integerQueue.add(3);

        integerQueue2.add(1);
        integerQueue2.add(2);
        integerQueue2.add(3);

        System.out.println("integerQueue = " + integerQueue);
        System.out.println("integerQueue2 = " + integerQueue2);

    }
}
// integerQueue = [1, 2, 3]
// integerQueue2 = [1, 2, 3]
```

------------------------------------------------------------------------

## 메서드 {#메서드 ke-size="size26"}

-   데이터 삽입
    -   offer(value), add(value) 메서드 안에 큐의 원소 타입에 맞게
        원소를 넣으면 삽입됩니다.
        -   offer(value)는 성공하면 true, 실패하면 false
        -   add(value)는 성공하면 true, 실패하면 IllegalStateException를
            던집니다.
-   데이터 제거
    -   poll(),remove() 메서드을 통해 Queue의 front 부분의 데이터를
        추출하고 해당 데이터를 리턴합니다.
        -   poll()은 데이터를 반환하지만, remove()는 그냥 삭제만 합니다.
-   데이터 조회
    -   peek(), element()를 사용해서 front 부분에 존재하는 데이터를
        반환합니다.
        -   peek은 큐가 비어있을 경우, null을 반환합니다.
        -   element는 큐가 비어있을 경우, NoSuchElementException를
            던집니다.
-   큐 상태 조회
    -   isEmpty()는 큐가 비어있는 경우, true. 아닌경우, false를
        반환합니다.
    -   contain(value)는 value가 있는 경우 true, 아닌경우 false를
        반환합니다.

------------------------------------------------------------------------

## 응용 {#응용 ke-size="size26"}

-   BFS : 그래프나 트리 구조에서 너비 우선 탐색(BFS)을 수행할 때 큐를
    사용하여 각 노드를 순서대로 탐색합니다.
-   [작업 스케줄링 큐
    :여러]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[작업이]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[동시에]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[실행되어야]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[할]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[때]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[,
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[큐를]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[사용하여]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[작업을]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[순서대로]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[처리하도록]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[스케줄을]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[관리할]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[수]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[
    ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}[있습니다.]{style="font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Apple SD Gothic Neo', Arial, sans-serif; letter-spacing: 0px;"}
    -   추후에 따로 다룰 메세지 큐도 여기에 해당됩니다.
-   웹 서버의 요청 처리 :웹 서버가 도착하는 HTTP 요청을 처리할 때 큐를
    사용하여 요청을 순차적으로 처리합니다. 이는 서버가 한 번에 하나의
    요청을 처리하고 다음 요청으로 넘어가는 순서를 유지하는 데 도움이
    됩니다.

 
