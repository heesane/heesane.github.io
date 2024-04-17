---
title: "[Java] equals가 안돼요... 어떻게 해야하나요?"
author: heesang
platform: 
date: 2023-10-25 01:54:01 +0900
categories: [Lang, equals, hashCode, Java, Object, override, precourse, WOOWA, 문법]
tags: ["Lang", "equals", "hashCode", "Java", "Object", "override", "precourse", "WOOWA", "문법"]
toc: true
comments: true
---
<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="778" data-origin-height="461">
<span
data-url="https://blog.kakaocdn.net/dn/bt6L1V/btsy7ghoai3/dvkCO2rgDxoLZne35AqIR1/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/bt6L1V/btsy7ghoai3/dvkCO2rgDxoLZne35AqIR1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbt6L1V%2Fbtsy7ghoai3%2FdvkCO2rgDxoLZne35AqIR1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="778" data-origin-height="461" /></span>
</figure>

이번에 우아한 형제들에서 진행하는 우아한 테크코스 프리코스에 참여하게
됐다.

프리코스를 진행하면서, 자연스럽게 객체를 비교할 때 equals() 메서드를
사용했었다.

하지만, 같은 멤버 변수를 가지는 같은 객체끼리의 비교에서 false를
반환하는 것에 대해서 의문이 들어 공부한 내용이다.

 

> 우선, 객체를 만들기 위해서 \"testEquals\"라는 클래스를 선언했다.

``` {#code_1698153593059 .java ke-language="java" ke-type="codeblock"}
public class testEquals{
    private final String name;

    public testEquals(String name){
            this.name = name;
    }
}
```

 

> 다음으로, main에서 2개의 객체를 선언하고 equals() 를 통해서 비교해
> 보겠다.

``` {#code_1698153700505 .java ke-language="java" ke-type="codeblock"}
public static void main(String[] args) {

        testEquals test1 = new testEquals("test");
        testEquals test2 = new testEquals("test");

        System.out.println(test1.equals(test2));

}
```

 

예상하기로는, 두 개의 객체 모두 name이라는 멤버 변수에 test라는 동일한
값이 들어갔으므로, true라는 반환 값이 나올 것이다.

 

> But, 예상과는 다른 결과\...

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="535" data-origin-height="251">
<span
data-url="https://blog.kakaocdn.net/dn/dKcUVA/btsy8aBcc2k/kgtXEpqkytquPUpTCeV1d1/img.png"
data-lightbox="lightbox" data-alt="false...."><img
src="https://blog.kakaocdn.net/dn/dKcUVA/btsy8aBcc2k/kgtXEpqkytquPUpTCeV1d1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdKcUVA%2Fbtsy8aBcc2k%2FkgtXEpqkytquPUpTCeV1d1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="535" data-origin-height="251" /></span>
<figcaption>false....</figcaption>
</figure>

하지만 실행 결과는 false로 출력되었다.

------------------------------------------------------------------------

이유는 **[*두 객체의 주소 값이 다르기
때문*]{style="background-color: #c0d1e7;"}**이다!

즉, **equals() 메서드는 주소 값이 다른 객체는 서로 다른 객체로 판단하기
때문이다**.

Java에서는 new를 통해서 class 객체를 생성할 때, 각각 다른 주소를
할당받기 때문에, 다른 객체로 판단하게 되는 것이다.

 

하지만, 객체가 아닌 단순 String 타입의 변수끼리 equals를 하면 어떻게
될까?

``` {#code_1698154599630 .java ke-language="java" ke-type="codeblock"}
public class Main {

    public static void main(String[] args) {
        String test1 = "test";
        String test2 = "test";

        System.out.println(test1.equals(test2));
    }
}
```

위의 코드처럼 아주 단순하게만 코드를 작성하고 실행해보자.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="338" data-origin-height="142">
<span
data-url="https://blog.kakaocdn.net/dn/zzeXl/btsy8rCFbOK/Mfkgu565IpHvw6TlMKR1Kk/img.png"
data-lightbox="lightbox" data-alt="이거는 true가 나온다."><img
src="https://blog.kakaocdn.net/dn/zzeXl/btsy8rCFbOK/Mfkgu565IpHvw6TlMKR1Kk/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FzzeXl%2Fbtsy8rCFbOK%2FMfkgu565IpHvw6TlMKR1Kk%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="338" data-origin-height="142" /></span>
<figcaption>이거는 true가 나온다.</figcaption>
</figure>

예상처럼 true가 나오는 것을 확인할 수 있었다.

------------------------------------------------------------------------

결론은 두 객체가 같은지 파악하기 위해서는 클래스 내부에 equals 메서드를
**재정의** 해야 한다.

 

``` {#code_1698155647293 .java ke-language="java" ke-type="codeblock"}
public class testEquals {
    private String name;

    public testEquals(String name){
        this.name = name;
    }
    @Override
    public boolean equals(Object obj){
        if (obj == null) return false;
        if (!(obj instanceof testEquals)) return false;
        if (obj == this) return true;
        testEquals test = (testEquals) obj;
        return this.name.equals(test.name) && this.name == test.name;
    }
}
```

equals 메서드를 재정의 한 후에 다시 실행시켜 보면 true가 나오는 것을
확인할 수 있다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="808" data-origin-height="203">
<span
data-url="https://blog.kakaocdn.net/dn/QK0NP/btsy7gaDlYx/qRT1LqkffJ9LVIWpwBPBK0/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/QK0NP/btsy7gaDlYx/qRT1LqkffJ9LVIWpwBPBK0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQK0NP%2Fbtsy7gaDlYx%2FqRT1LqkffJ9LVIWpwBPBK0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="808" data-origin-height="203" /></span>
</figure>

------------------------------------------------------------------------

## equals() 메서드 {#equals-메서드 ke-size="size26"}

> equals 메서드를 **재정의 하지 않는다면**, 클래스의 인스턴스는 **자기
> 자신과만 동일할 수 있다!!\
> **

equals에 대해서 자세히 알아보기 위해서 equals()에 ctrl + 클릭을 통해
내부 라이브러리 코드를 보자.

``` {#code_1698155951891 .java ke-language="java" ke-type="codeblock"}
//in Object.java
public boolean equals(Object obj) {
        return (this == obj);
}
```

기존의 false의 결과 값이 나오는 equals 메서드를 살펴보면, Object obj가
자기 자신인지에 대해서만 판단하여 return 하는 것을 확인할 수 있다. 

 

### 그렇다면, 언제 equals를 재정의해야 하나요? {#그렇다면-언제-equals를-재정의해야-하나요 ke-size="size23"}

1.  논리적 동치성을 확인할 때, **상위 클래스의 equals**가 논리적
    동치성을 비교하도록 재정의 되어 있지 않을 때
2.  값을 갖는 Class일 때 -\> Integer, String\... etc
3.  객체가 같은 것이 아니라, 객체의 속성이 동일한 지 파악하고 싶을 때

> 여기서 논리적 동치성이란,\
> 두 가지 다른 것들이 동등한 결과를 나타내거나 동일한 논리적 상태를
> 나타내는 경우에 사용되는 개념

------------------------------------------------------------------------

### equals 메서드 정의를 잘하는 방법도 있나요? {#equals-메서드-정의를-잘하는-방법도-있나요 ke-size="size23"}

물론입니다.

1.  == 연산자를 통해 입력으로 들어온 클래스가 자기 자신을 참조했는지
    확인
2.  instanceof 연산자를 통해 입력으로 들어온 클래스가 자신의 클래스와
    동일한지 파악
3.  입력된 객체를 자신의 클래스로 형 변환
4.  비교를 필요로 하는 필드들이 모두 일치하는지 하나씩 확인
5.  **equals 메서드를 재정의할 때 hashCode도 반드시 재정의한다.**

------------------------------------------------------------------------

## HashCode {#hashcode ke-size="size26"}

HashCode는 객체를 식별하는 Integer 값이다. 객체가 가지고 있는 데이터를
어떤 알고리즘을 통해서 계산된 정수 값을 HashCode라고 할 수 있다.

``` {#code_1698159602923 .java ke-language="java" ke-type="codeblock"}
// in String.java
public int hashCode() {
    int h = hash;
    if (h == 0 && value.length > 0) {
        char val[] = value;

        for (int i = 0; i < value.length; i++) {
            h = 31 * h + val[i];
        }
        hash = h;
    }
    return h;
}
```

내부적으로 hashCode는 위와 같이 정의되어 있다. 

for loop 문을 통해서 [s\[0\]\*31\^(n-1) + s\[1\]\*31\^(n-2) + \... +
s\[n-1\] 으로 계산되어 return
한다.]{style="color: #242729; text-align: left;"}

 

### HashCode를 사용하는 이유 {#hashcode를-사용하는-이유 ke-size="size23"}

hashcode를 사용하는 많은 이유 중에 하나는, 객체를 비교할 때 드는 비용을
낮추기 위해서이다.

Java에서는 2개의 객체를 동일한지 비교하기 위해서 equals() 메서드를
사용하는데, 여러 객체를 비교할 때, equals()를 사용하게 되면 Integer에
비해서 많은 시간이 소모되게 된다.

하지만 hashcode는 Integer이므로, equals()를 사용하는 것보다는 빠르게
비교할 수 있습니다.

**-\> 속도의 이점과 객체를 비교하기 위해서!**

------------------------------------------------------------------------

### HashCode 규약 {#hashcode-규약 ke-size="size23"}

1\. equals를 통한 객체 비교에서 **객체의 정보가 변하지 않았다면,
HashCode는 항상 동일한 값을 갖는다.**

2\. **Object1.equals(Object2)가 true인 경우, 두 객체의 HashCode는
동일하다.**

3\. 하지만, **두 객체가 동일하다고 판단했더라도, 객체의 HashCode는 다를
수 있다.** -\> **해시 충돌**

 

3번째 규약에서 발생하는 동일 값을 가진 객체가 서로 다른 해시 값을 갖게
될 수 있는데, HashMap의 key 값으로 객체를 사용하는 경우 문제가 발생한다.

 

> \
> If you are planning to use a class as Hash table key,\
> then you must override both equals() and hashCode() methods.

``` {#code_1698165722013 .java ke-language="java" ke-type="codeblock"}
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map testMap = new HashMap<>();
        testMap.put(new testEquals("test1"),"1");
        testMap.put(new testEquals("test2"),"2");
        testMap.put(new testEquals("test3"),"3");

        String outputEquals = testMap.get(new testEquals("test1"));
        System.out.println(outputEquals);
    }
}
```

우선 위와 같이 HashMap의 Key로 testEquals 객체를 사용하고, get을 통한
outputEquals의 데이터는 \"1\"일 것이다.

 

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="220" data-origin-height="108">
<span
data-url="https://blog.kakaocdn.net/dn/o5Jcv/btsy3fKx3Sz/NVQVqCOWONcxh6AeiweJbK/img.png"
data-lightbox="lightbox" data-alt="null"><img
src="https://blog.kakaocdn.net/dn/o5Jcv/btsy3fKx3Sz/NVQVqCOWONcxh6AeiweJbK/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fo5Jcv%2Fbtsy3fKx3Sz%2FNVQVqCOWONcxh6AeiweJbK%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="220" data-origin-height="108" /></span>
<figcaption>null</figcaption>
</figure>

하지만 실행 결과는 null로 나오게 된다. 아마 테스트 코드를 작성하고
실행해 본다면 NPE(Null Point Exception)이 발생하게 될 것이다.

 

이런 결과 값이 나오게 되는 이유는 testEquals의 객체에 대한 해시 값을
testMap 객체에서 찾을 수 없기 때문이다.

그렇다면 위와 같은 출력을 방지하기 위해서는 어떻게 해야 할까?

 

## HashCode 재정의 {#hashcode-재정의 ke-size="size26"}

바로 이전에 했던 equals() 메서드를 재정의 했던 것처럼 HashCode() 또한
재정의를 해줘야 할 것이다.

재정의의 위치는 testEquals 객체에서 재정의하면 될 것이다.

``` {#code_1698166091106 .java ke-language="java" ke-type="codeblock"}
@Override
public int hashCode(){
    return this.name.hashCode();
}
```

이름의 hashcode를 반환하게 한다면, 다른 객체의 name 멤버와 비교할 때
동일하다면, 동일한 값의 hash 코드가 반환하게 될 것이므로, equals를
사용할 때 문제가 발생하지 않게 된다.

------------------------------------------------------------------------

이번 우아한 테크코스 프리코스 1주 차 프로젝트를 진행할 때, 객체를
HashMap의 Key로 사용을 했었는데, 분명히 로직에 문제가 없음에도 테스트
코드를 통과하지 못하는 것을 계기로 공부하게 되었다.

 

## Ref. {#ref. ke-size="size26"}

[https://velog.io/@sonypark/Java-equals-hascode-%EB%A9%94%EC%84%9C%EB%93%9C%EB%8A%94-%EC%96%B8%EC%A0%9C-%EC%9E%AC%EC%A0%95%EC%9D%98%ED%95%B4%EC%95%BC-%ED%95%A0%EA%B9%8C](https://velog.io/@sonypark/Java-equals-hascode-%EB%A9%94%EC%84%9C%EB%93%9C%EB%8A%94-%EC%96%B8%EC%A0%9C-%EC%9E%AC%EC%A0%95%EC%9D%98%ED%95%B4%EC%95%BC-%ED%95%A0%EA%B9%8C "[Java] equals() & hashcode() 메서드는 언제 재정의해야 할까?"){target="_blank"
rel="noopener"}

<figure id="og_1698241490005" contenteditable="false"
data-ke-type="opengraph" data-ke-align="alignCenter"
data-og-type="article"
data-og-title="[Java] equals() &amp; hashcode() 메서드는 언제 재정의해야 할까?"
data-og-description="예를 들어, 아래와 같이 값이 Menu 클래스가 있다고 하자.두 개의 Menu객체(friedChicken, friedChicken2)는 name과 price가 서로 같은 객체 지닌다. 위 테스트 코드를 실행한 결과는 다음과 같다.테스트가 실"
data-og-host="velog.io"
data-og-source-url="https://velog.io/@sonypark/Java-equals-hascode-%EB%A9%94%EC%84%9C%EB%93%9C%EB%8A%94-%EC%96%B8%EC%A0%9C-%EC%9E%AC%EC%A0%95%EC%9D%98%ED%95%B4%EC%95%BC-%ED%95%A0%EA%B9%8C"
data-og-url="https://velog.io/@sonypark/Java-equals-hascode-메서드는-언제-재정의해야-할까"
data-og-image="https://scrap.kakaocdn.net/dn/buqJsX/hyUlu5Rlq1/EUaNRaWNRxhvaBAKU0peO1/img.png?width=269&amp;height=188&amp;face=0_0_269_188,https://scrap.kakaocdn.net/dn/pzmzY/hyUj9112tR/8FAnMz4eZkIBXo4jFAsdI0/img.png?width=269&amp;height=188&amp;face=0_0_269_188,https://scrap.kakaocdn.net/dn/ULS1D/hyUkmmMpMn/L4wlTL9JisxwAGCQKXC7PK/img.png?width=2108&amp;height=544&amp;face=0_0_2108_544">
<a
href="https://velog.io/@sonypark/Java-equals-hascode-%EB%A9%94%EC%84%9C%EB%93%9C%EB%8A%94-%EC%96%B8%EC%A0%9C-%EC%9E%AC%EC%A0%95%EC%9D%98%ED%95%B4%EC%95%BC-%ED%95%A0%EA%B9%8C"
target="_blank" rel="noopener"
data-source-url="https://velog.io/@sonypark/Java-equals-hascode-%EB%A9%94%EC%84%9C%EB%93%9C%EB%8A%94-%EC%96%B8%EC%A0%9C-%EC%9E%AC%EC%A0%95%EC%9D%98%ED%95%B4%EC%95%BC-%ED%95%A0%EA%B9%8C"></a>
<div class="og-image"
style="background-image: url(&#39;https://scrap.kakaocdn.net/dn/buqJsX/hyUlu5Rlq1/EUaNRaWNRxhvaBAKU0peO1/img.png?width=269&amp;height=188&amp;face=0_0_269_188,https://scrap.kakaocdn.net/dn/pzmzY/hyUj9112tR/8FAnMz4eZkIBXo4jFAsdI0/img.png?width=269&amp;height=188&amp;face=0_0_269_188,https://scrap.kakaocdn.net/dn/ULS1D/hyUkmmMpMn/L4wlTL9JisxwAGCQKXC7PK/img.png?width=2108&amp;height=544&amp;face=0_0_2108_544&#39;);">
 
</div>
<div class="og-text">
<p>[Java] equals() &amp; hashcode() 메서드는 언제 재정의해야 할까?</p>
<p>예를 들어, 아래와 같이 값이 Menu 클래스가 있다고 하자.두 개의
Menu객체(friedChicken, friedChicken2)는 name과 price가 서로 같은 객체
지닌다. 위 테스트 코드를 실행한 결과는 다음과 같다.테스트가 실</p>
<p>velog.io</p>
</div>
</figure>

<https://codechacha.com/ko/java-hashcode/>

<figure id="og_1698241492231" contenteditable="false"
data-ke-type="opengraph" data-ke-align="alignCenter"
data-og-type="website"
data-og-title="Java - hashCode(), 사용하는 이유? 구현 방법?"
data-og-description="Hashcode는 객체를 식별하는 Integer 값입니다. Java에서 객체의 hashcode를 계산할 때 `hashCode()` 메소드를 호출하면 됩니다. Hashcode를 사용하는 이유 중에 하나는, 객체를 비교할 때 드는 비용을 낮추기 "
data-og-host="codechacha.com"
data-og-source-url="https://codechacha.com/ko/java-hashcode/"
data-og-url="https://codechacha.com/ko/java-hashcode/"
data-og-image="https://scrap.kakaocdn.net/dn/bXGF3y/hyUkj4FihE/lFjqcuo7ddBGF14spngjxK/img.png?width=192&amp;height=192&amp;face=0_0_192_192">
<a href="https://codechacha.com/ko/java-hashcode/" target="_blank"
rel="noopener"
data-source-url="https://codechacha.com/ko/java-hashcode/"></a>
<div class="og-image"
style="background-image: url(&#39;https://scrap.kakaocdn.net/dn/bXGF3y/hyUkj4FihE/lFjqcuo7ddBGF14spngjxK/img.png?width=192&amp;height=192&amp;face=0_0_192_192&#39;);">
 
</div>
<div class="og-text">
<p>Java - hashCode(), 사용하는 이유? 구현 방법?</p>
<p>Hashcode는 객체를 식별하는 Integer 값입니다. Java에서 객체의
hashcode를 계산할 때 `hashCode()` 메소드를 호출하면 됩니다. Hashcode를
사용하는 이유 중에 하나는, 객체를 비교할 때 드는 비용을 낮추기</p>
<p>codechacha.com</p>
</div>
</figure>
