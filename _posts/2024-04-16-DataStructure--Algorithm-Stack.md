---
title: "[DataStructure & Algorithm] Stack"
author: heesang
platform: 
date: 2024-04-16 21:25:41 +0900
categories: [DataStructure Algorithm, Algorithm, datastructure, 메서드, 스택, 알고리즘, 자료구조]
tags: ["DataStructure Algorithm", "Algorithm", "datastructure", "메서드", "스택", "알고리즘", "자료구조"]
toc: true
comments: true
---
<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="898" data-origin-height="251">
<span
data-url="https://blog.kakaocdn.net/dn/KU5XN/btsGGQPEH7v/lOK00iavkkjey7wwaxeIM0/img.png"
data-lightbox="lightbox" data-alt="자료구조 및 알고리즘"><img
src="https://blog.kakaocdn.net/dn/KU5XN/btsGGQPEH7v/lOK00iavkkjey7wwaxeIM0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FKU5XN%2FbtsGGQPEH7v%2FlOK00iavkkjey7wwaxeIM0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="898" data-origin-height="251" /></span>
<figcaption>자료구조 및 알고리즘</figcaption>
</figure>

------------------------------------------------------------------------

## 개요 {#개요 ke-size="size26"}

스택은 영어 그 자체로, \'쌓다\'와 같은 뜻을 가진 용어로, 어떤 것을 쌓아
올리는 형태와 같은 자료구조이다.

즉, 데이터를 입력하는 순서대로 쌓는 자료구조인 것이다.

 

실생활에서는 원통에 들어가있는 과자를 생각하면 편하다.

> [가장 위에 있는 과자는 가장 마지막에 넣은 과자이니까, 맨 위에
> 있겠지?]{style="font-family: 'Noto Serif KR';"}

 

스택은 가장 나중에 들어온 데이타가 가장 먼저 추출되는 후입선출(LIFO :
Last In First Out)구조로, 프로그래밍에서 데이터가 입력된 순서대로 처리는
되는 것이 아닌, 가장 나중에 들어온 데이터를 먼저 처리할 때 사용한다.

 

<figure class="imageblock alignLeft" data-ke-mobilestyle="widthOrigin"
data-origin-width="300" data-origin-height="216">
<span
data-url="https://blog.kakaocdn.net/dn/Cj3LU/btsGGbGuJkO/hgRxXjAJsCerb9vUIX9OUk/img.png"
data-lightbox="lightbox" data-alt="Stack"><img
src="https://blog.kakaocdn.net/dn/Cj3LU/btsGGbGuJkO/hgRxXjAJsCerb9vUIX9OUk/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FCj3LU%2FbtsGGbGuJkO%2FhgRxXjAJsCerb9vUIX9OUk%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="300" data-origin-height="216" /></span>
<figcaption>Stack</figcaption>
</figure>

------------------------------------------------------------------------

## 특징 {#특징 ke-size="size26"}

-   후입선출 구조
-   단방향 입출력 구조 : 한 방향에서만 데이터를 입력하거나
    추출하기때문에 단방향 구조이다.
-   DFS (깊이 우선 탐색)에 활용된다.
-   재귀 함수와 같은 구조를 가진다.

------------------------------------------------------------------------

## 구현 {#구현 ke-size="size26"}

java.util.Stack을 import한 후, 다음과 같은 코드를 통해서 객체를
생성한다.

꺽쇠(\<\>)안에 들어간 자료형을 가지는 스택을 선언할 수 있다.

``` {#code_1713269130178 .java ke-language="java" ke-type="codeblock"}
import java.util.Stack;

class MyStack{
    public static void main(String[] args){
        Stack testStack = new Stack<>();
        // Integer부분만 다른 타입으로 바꾸면 해당 타입을 가지는 스택이 선언된다.
    }
}
```

------------------------------------------------------------------------

## 메서드 {#메서드 ke-size="size26"}

-   값 추가
    -   push(value)를 통해서 값을 추가할 수 있다.
    -   add(value)를 통해서도 값을 추가할수 있다.
-   값 추출
    -   pop()를 통해서 스택의 최상단에 위치하는 값을 추출한다.
    -   이때, 스택에서 해당 데이터가 아예 빠지게 되므로, 유의해서
        사용한다.
-   값 조회
    -   peek()를 통해서 스택 최상단에 위치하는 값을 조회한다.
    -   pop()메서드와는 다르게 그저 조회만 한다.
-   스택 초기화
    -   clear()를 통해서 해당 스택의 모든 데이터들을 초기화할 수 있다.
-   스택 상태 조회
    -   empty()를 통해서 해당 스택에 원소가 들어있는지 확인할 수 있으며,
        boolean형식으로 반환한다.
    -   search(value)를 통해서 해당 value가 들어있는 index를 반환한다.
        존재하지 않는다면 -1을 반환한다.

------------------------------------------------------------------------

## 응용 {#응용 ke-size="size26"}

-   문자열 역순 만들기
    -   주어진 String을 앞에서부터 하나씩 넣고 pop을 하면서 새로운
        문자열을 만든다면 역순으로 문자열을 만들 수 있다
-   undo 명령어
    -   터미널에 사용자가 입력한 데이터를 스택 구조로 적용하고 undo
        명령어시, 해당 명령어를 pop하여 명령어를 취소한다.
-   괄호 검사
    -   ( \" { \[ 같은 Braket을 사용한 경우, 닫아야하는데, 이런 경우도
        스택 자료구조를 사용해서 검사할 수 있다.
-   후위 표기(Postfix Expression
