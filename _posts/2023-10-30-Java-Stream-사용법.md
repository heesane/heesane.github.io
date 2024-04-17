---
title: "[Java] Stream 사용법"
author: heesang
platform: 
date: 2023-10-30 01:51:07 +0900
categories: [Lang, Java, Stream, 고수처럼보이기, 반복문줄이기, 스트림, 우아한테크코스, 자바, 프리코스]
tags: ["Lang", "Java", "Stream", "고수처럼보이기", "반복문줄이기", "스트림", "우아한테크코스", "자바", "프리코스"]
toc: true
comments: true
---
<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="778" data-origin-height="461">
<span
data-url="https://blog.kakaocdn.net/dn/bNSmNZ/btszlJ4EVFf/nC5JgKRTBbKTQmYtsNMVh0/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/bNSmNZ/btszlJ4EVFf/nC5JgKRTBbKTQmYtsNMVh0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbNSmNZ%2FbtszlJ4EVFf%2FnC5JgKRTBbKTQmYtsNMVh0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="778" data-origin-height="461" width="611"
height="362" /></span>
</figure>

우아한 테크코스 프리코스를 진행할 때, 반복문과 조건문을 너무 많이 써서
어떤 방법이 좋을까 찾아보던 중에 Stream을 찾아서 공부하게 되었다.

------------------------------------------------------------------------

## Stream정의와 장점 {#stream정의와-장점 style="text-align: left;" ke-size="size26"}

JDK 8부터 지원되기 시작한 API 중 하나이다. **Stream**은 **Collection
내부에 저장된 원소들을 하나씩 꺼내서 처리할 수 있는 코드패턴**이다.
또한, **Lambda 식을 통해서 반복문을 간결**하게 표현할 수 있다는 장점이
존재하고, 내부 구조에 선언된 반복자를 통해서 **병렬처리가 쉽다**는
장점이 있다.  

## 기존의 반복과의 비교 {#기존의-반복과의-비교 style="text-align: left;" ke-size="size26"}

### for문을 통한 반복문 {#for문을-통한-반복문 style="text-align: left;" ke-size="size23"}

``` {.java ke-type="codeblock" ke-language="java"}
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // 리스트 내부의 원소 중 "c"만 출력하라.

        ArrayList example_list = new ArrayList(Arrays.asList("a", "b", "c", "d", "e"));

        for(int i =0; i
```

기존의 For문을 통한 반복문은 단순한 로직을 구현하는데도 많은
Indentation을 차지하는 것을 볼 수 있다. 만약 더 복잡한 조건과 반복을
사용하게 된다면 나중에는 왼쪽의 브래킷이 굉장히 많아질 것이다.

###   {#section style="text-align: left;" ke-size="size23"}

### Stream 사용 {#stream-사용 style="text-align: left;" ke-size="size23"}

``` {.java ke-type="codeblock" ke-language="java"}
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // 리스트 내부의 원소 중 "c"만 출력하라.

        ArrayList example_list = new ArrayList(Arrays.asList("a", "b", "c", "d", "e"));

        example_list.stream()
                .filter("c"::equals)
                .forEach(System.out::println);
    }
}
```

기존의 반복문에 비해 굉장히 간결한 코드로 동일한 동작을 수행할 수 있다..

------------------------------------------------------------------------

위에서는 기존의 반복문과의 차이를 알아봤으니까, 이번에는 사용법에 대해서
알아볼 것이다.

## Stream 사용법 {#stream-사용법 style="text-align: left;" ke-size="size26"}

Stream을 어디에 적용하는지에 따라서 다른 형식으로 사용을 해야 한다.
Stream을 사용하는 형식에는 다양한 형식이 존재하지만, 자주 사용하게 될 것
같은 Collection과 Array, Primitive만 살펴보고 넘어가겠다.  

#### 1. Collection {#collection style="text-align: left;" ke-size="size20"}

위에서 했던 예제가 Collection에서 Stream을 사용하는 방법이었다.

``` {.java ke-type="codeblock" ke-language="java"}
ArrayList example_list = new ArrayList(Arrays.asList("a", "b", "c", "d", "e"));
Stream example_stream = example_list.stream();
```

#### 2. Array {#array style="text-align: left;" ke-size="size20"}

Collection뿐만 아니라, Array에서도 Stream을 자주 사용한다.

``` {.java ke-type="codeblock" ke-language="java"}
String[] array = "a,b,c,d,e".split(",");
Stream stream1 = Arrays.stream(array);
Stream stream2 = Arrays.stream(array, 1, 3);
```

 

#### 3. Primitive {#primitive style="text-align: left;" ke-size="size20"}

Primitive는 기본 타입에 대한 이야기이다. Java에서는 Primitive 타입에
대해서는 오토 박싱과 언박싱이 발생한다. int형 변수를 처리할 때,
내부적으로 Integer 타입으로 오토 박싱하여 처리하는 경우가 있는데 이런
경우에 변환하는 과정 중 오버헤드가 발생해서 처리 속도가 떨어질 수 있다.
이로 인해 Stream에서도 int와 Integer 각각 Stream을 사용하는 방법이
존재한다.

``` {.java ke-type="codeblock" ke-language="java"}
// int -> 오토 박싱 수행 X
IntStream intStream = IntStream.range(1,90);

// Integer
Stream stream = IntStream.range(1,90).boxed();
```

Generic을 사용하기 위해서 Stream stream의 경우는 .boxed()가 필요하다.

------------------------------------------------------------------------

### 데이터 가공 {#데이터-가공 style="text-align: left;" ke-size="size23"}

이제 스트림을 통해서 데이터를 추출했으면, 그 데이터에 어떠한 작업을
거쳐서 사용해야 하기 때문에 어떤 메서드들을 통해서 데이터를 가공할 수
있는지 알아보겠다.  

#### Filter {#filter style="text-align: left;" ke-size="size20"}

Filter는 스트림에서 추출되는 데이터에서 특정 패턴을 파악하거나, 특정
데이터를 필터링하는 메서드다.

``` {.java ke-type="codeblock" ke-language="java"}
ArrayList example_list = new ArrayList(Arrays.asList("a", "b", "c", "d", "e"));

Stream example_stream = example_list.stream();

example_stream.filter(s -> s.equals("c")).forEach(System.out::println);

// 출력 예시
c
```

filter 메서드는 람다 식을 입력으로 받아 Boolean 값을 리턴하게 된다.
이때, 리턴하는 값이 true라면 다음으로 넘어가고, 아니라면 무시된다.  

### Map {#map style="text-align: left;" ke-size="size23"}

Map() 메서드는 스트림에서 추출되는 데이터에 변형하여 Stream을 반환한다.

``` {.java ke-type="codeblock" ke-language="java"}
Stream stream = IntStream.range(1,100).boxed();
stream.filter(s -> s % 10 == 0)
    .map(s -> s * 6)
    .forEach(System.out::println);
    
// 출력 예시
60
120
180
240
300
360
420
480
540
```

#### Sorted {#sorted style="text-align: left;" ke-size="size20"}

Sorted() 메서드는 기본적으로는 오름차순으로 내부의 원소를 정렬한다.
옵션으로 내림차순으로 설정할 수 있다.

``` {.java ke-type="codeblock" ke-language="java"}
Stream stream = new Random().ints(1, 100).limit(10).boxed();

//오름차순
stream.sorted().forEach(System.out::println);

//내림차순
stream.sorted(Comparator.reverseOrder()).forEach(System.out::println);
```

#### peek {#peek style="text-align: left;" ke-size="size20"}

peek는 map과 유사하게 스트림 내부의 원소들에 대해서 람다 함수를 처리할
수 있다. 차이점은 map()은 스트림을 반환하지만 peek는 그냥 적용하기만
한다.

``` {.java ke-type="codeblock" ke-language="java"}
Stream stream = new Random().ints(1, 100).limit(10).boxed();
stream.peek(System.out::println).sorted(Comparator.reverseOrder()).forEach(System.out::println);

// 출력
원본 : 29,57,45,45,17,16,65,61,58,6
정렬 : 65,61,58,57,45,45,29,17,16,6
```

내부의 원소들은 System.out의 네임 스페이스의 println을 사용해서 10개의
랜덤 Int 원소를 출력하고, 해당 원소들을 내림차순으로 정렬하고 다시
출력하는 예시다.  

### 데이터 결과 {#데이터-결과 style="text-align: left;" ke-size="size23"}

#### Collect {#collect style="text-align: left;" ke-size="size20"}

Java에서 Stream을 사용하는 주된 이유는 기존의 배열 또는 데이터에
함수들을 적용하고 다시 원래의 타입으로 변환하기 위해서 사용하게 된다.
Collector 내부에 선언된 자료형으로 스트림을 추출할 수 있다. 예를 들면,
toList, toSet, toString과 같은 것들이 존재한다.

``` {.java ke-type="codeblock" ke-language="java"}
Stream stream = new Random().ints(1, 100).limit(10).boxed();
List Int_List = stream.filter(s -> s % 2 == 0).collect(Collectors.toList());
System.out.println("Even Numbers: " + Int_List);

// 예시
Even Numbers: [32, 56, 32, 12, 50, 56]
```

####   {#section-1 style="text-align: left;" ke-size="size20"}

#### forEach {#foreach style="text-align: left;" ke-size="size20"}

스트림에서 추출되는 값에 대해서 어떤 함수를 적용하고 싶을 때 forEach를
사용한다. forEach 메서드는 특정 값을 리턴하지는 않는다.

``` {.java ke-type="codeblock" ke-language="java"}
Stream stream = new Random().ints(1, 100).limit(10).boxed();
stream.filter(s -> s % 2 == 0).collect(Collectors.toList()).forEach(System.out::println);

//출력
24,68,34,78
```

------------------------------------------------------------------------

 
