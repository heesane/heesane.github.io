---
title: "[Springboot] Springboot에서 Redis를 사용해보자!"
author: heesang
platform: 
date: 2023-10-15 01:04:33 +0900
categories: [Backend/Framework, API, config, redis, redisTemplate, SpringBoot, test]
tags: ["Backend/Framework", "API", "config", "redis", "redisTemplate", "SpringBoot", "test"]
toc: true
comments: true
---
<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="750" data-origin-height="343">
<span
data-url="https://blog.kakaocdn.net/dn/HO2Pp/btsyn0glStJ/5cW65U7JtGBffB2IK2Kg0k/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/HO2Pp/btsyn0glStJ/5cW65U7JtGBffB2IK2Kg0k/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FHO2Pp%2Fbtsyn0glStJ%2F5cW65U7JtGBffB2IK2Kg0k%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="750" data-origin-height="343" /></span>
</figure>

이전에도 잠깐 Redis에 관한 글을 작성했었는데, 우연히도 이번 프로젝트에서
Redis를 사용할 일이 생겨서 구현해보는 김에 작성해 본다.

------------------------------------------------------------------------

우선 디펜던시부터 추가해 보자!

<figure class="imageblock widthContent"
data-ke-mobilestyle="widthOrigin" data-origin-width="627"
data-origin-height="62">
<span
data-url="https://blog.kakaocdn.net/dn/cHKYYH/btsytK4h6OQ/YPefS6NJTNotLxUm8QYpl0/img.png"
data-lightbox="lightbox" data-alt="spring-boot-starter-data-redis"><img
src="https://blog.kakaocdn.net/dn/cHKYYH/btsytK4h6OQ/YPefS6NJTNotLxUm8QYpl0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcHKYYH%2FbtsytK4h6OQ%2FYPefS6NJTNotLxUm8QYpl0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="627" data-origin-height="62" /></span>
<figcaption>spring-boot-starter-data-redis</figcaption>
</figure>

 

Springboot에서 Redis를 사용할 때,
[SpringRedisRepository]{style="background-color: #9feec3;"},
[SpringRedisTemplate]{style="background-color: #9feec3;"} 이렇게 2가지의
방식이 존재하는데, 이번에는 SpringRedisTemplate를 사용해서 Redis를
사용할 예정이다.

 

// [application.properties]{style="background-color: #9feec3;"}

Redis에 접속하기 위한 IP, PORT, PASSWORD, DATABASE를 작성한다.

<figure class="imageblock alignLeft" data-ke-mobilestyle="widthOrigin"
data-origin-width="339" data-origin-height="136">
<span
data-url="https://blog.kakaocdn.net/dn/bsb78C/btsyuaIqyB6/tihkbrzNATkLYl2NOazTt0/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/bsb78C/btsyuaIqyB6/tihkbrzNATkLYl2NOazTt0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbsb78C%2FbtsyuaIqyB6%2FtihkbrzNATkLYl2NOazTt0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="339" data-origin-height="136" /></span>
</figure>

 

// [RedisConfig.java ]{style="background-color: #9feec3;"}

Redis에 접속하기 위한 정보와, 어떤 Serializer를 사용할 것인지 설정한다.

<figure class="imageblock alignLeft" data-ke-mobilestyle="widthOrigin"
data-origin-width="419" data-origin-height="330">
<span
data-url="https://blog.kakaocdn.net/dn/MkZmt/btsyukj2tby/cUqKFiBHaVmkoahj46uTG1/img.png"
data-lightbox="lightbox" data-alt="속성 정의"><img
src="https://blog.kakaocdn.net/dn/MkZmt/btsyukj2tby/cUqKFiBHaVmkoahj46uTG1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FMkZmt%2Fbtsyukj2tby%2FcUqKFiBHaVmkoahj46uTG1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="419" data-origin-height="330" /></span>
<figcaption>속성 정의</figcaption>
</figure>

RedisConfig로 이름을 설정하고, Springboot에서 config로 인식할 수 있게
\@Configuration 어노테이션을 추가한다.

<figure class="imageblock alignLeft" data-ke-mobilestyle="widthOrigin"
data-origin-width="432" data-origin-height="290">
<span
data-url="https://blog.kakaocdn.net/dn/bJoofN/btsys6fGPtZ/8Ent8Uv89cShuOcdpCKN91/img.png"
data-lightbox="lightbox" data-alt="설정"><img
src="https://blog.kakaocdn.net/dn/bJoofN/btsys6fGPtZ/8Ent8Uv89cShuOcdpCKN91/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbJoofN%2Fbtsys6fGPtZ%2F8Ent8Uv89cShuOcdpCKN91%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="432" data-origin-height="290" /></span>
<figcaption>설정</figcaption>
</figure>

일반 생성자를 정의하는데, 여기서 \@Value를 통해서 직접적으로 값을 넣지
않고, applcation.properties에 정의되어 있는 값을 주입한다. 참고로 이런
값들이 Github에 올라가게 되면 보안적으로 취약할 수 있으니 주의하자.

 

<figure class="imageblock alignLeft" data-ke-mobilestyle="widthOrigin"
data-origin-width="670" data-origin-height="310">
<span
data-url="https://blog.kakaocdn.net/dn/cQ3TkO/btsyuEo0Um9/fcKqcQx4uIrdrH9eC4TF20/img.png"
data-lightbox="lightbox" data-alt="기본 설정"><img
src="https://blog.kakaocdn.net/dn/cQ3TkO/btsyuEo0Um9/fcKqcQx4uIrdrH9eC4TF20/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcQ3TkO%2FbtsyuEo0Um9%2FfcKqcQx4uIrdrH9eC4TF20%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="670" data-origin-height="310" /></span>
<figcaption>기본 설정</figcaption>
</figure>

Redis와 연결하기 위한 Factory를 정의한다. 사실 로컬에서 Redis를 설치하고
연결하는 것도 좋지만, Docker를 사용해서 Redis를 실행하는 것이 좋은데,
일반적으로 Stand-Alone 방식으로 클러스터 구성이 아닌 독립적으로 Redis를
운영하기 때문에 RedisStandAloneConfiguration을 통해서 HostName, Port,
Database, Password를 설정한다.

 

Springboot에서는 Redis에 연결하는 2개의 클라이언트 라이브러리들이
존재하는데, 하나는 Jedis, 다른 하나는 Lettuce이다. 하지만 Jedis는
동기방식으로 동작하며 Blocking 이슈가 발생할 수 있다. Lettuce는
동기/비동기 방식으로 동작하며, Non-Blocking 하게 요청을 처리할 수 있다.
또한 확장성이 뛰어나다는 장점이 존재한다. 하지만 초기 설정 같은 부분이
까다롭다는 단점이 존재한다.

 

 

<figure class="imageblock alignLeft" data-ke-mobilestyle="widthOrigin"
data-origin-width="658" data-origin-height="416">
<span
data-url="https://blog.kakaocdn.net/dn/cXhOc3/btsyukxzMpD/WKu3iUNtq7lJRsbDD2Y1sK/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/cXhOc3/btsyukxzMpD/WKu3iUNtq7lJRsbDD2Y1sK/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcXhOc3%2FbtsyukxzMpD%2FWKu3iUNtq7lJRsbDD2Y1sK%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="658" data-origin-height="416" /></span>
</figure>

RedisTemplate를 사용할 때, 어떤 Serializer를 사용할 것인지 설정해주어야
하는데, 우선 Key Value 쌍과 Hash 자료구조만 사용할 예정이기 때문에
StringRedisSerializer로 설정해주었다.

 

<figure class="imageblock alignLeft" data-ke-mobilestyle="widthOrigin"
data-origin-width="603" data-origin-height="224">
<span
data-url="https://blog.kakaocdn.net/dn/bBY4VV/btsytgCorcV/TzJrm1xQYUZkpSNia0AOH1/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/bBY4VV/btsytgCorcV/TzJrm1xQYUZkpSNia0AOH1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbBY4VV%2FbtsytgCorcV%2FTzJrm1xQYUZkpSNia0AOH1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="603" data-origin-height="224" /></span>
</figure>

key value쌍만 전용으로 처리하는 stringRedisTemplate도 선언해 주었다.

 

이제 기본적인 설정이 끝났으니, 실제로 사용하기 위한 service와
controller를 정의하고 API로 만들어서 테스트해 보면 된다.

 

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1057" data-origin-height="415">
<span
data-url="https://blog.kakaocdn.net/dn/dacHim/btsysG2WcQC/eDzkhDx3eeJ402YpjJRcpk/img.png"
data-lightbox="lightbox" data-alt="RedisService"><img
src="https://blog.kakaocdn.net/dn/dacHim/btsysG2WcQC/eDzkhDx3eeJ402YpjJRcpk/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdacHim%2FbtsysG2WcQC%2FeDzkhDx3eeJ402YpjJRcpk%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1057" data-origin-height="415" /></span>
<figcaption>RedisService</figcaption>
</figure>

우서 StringRedisTemplate를 선언하고, 의존성 주입을 위한 \@Autowired를
사용하여 StringRedisTemplate에 대한 의존성을 주입한다. controller에서
사용될 saveData와 showData를 선언한다.

위의 코드에서는 set(key, value)를 통해서 값을 저장하게 되는데, 실제로
Docker를 통해서 Redis 컨테이너를 실행시킨 후에 docker exec -it redis
redis-cli를 통해서 접근한 후에 set, get 메서드를 통해서 key:value 쌍으로
데이터를 저장할 수 있다.

 

<figure class="imageblock alignLeft" data-ke-mobilestyle="widthOrigin"
data-origin-width="768" data-origin-height="536">
<span
data-url="https://blog.kakaocdn.net/dn/be47mV/btsyuhAQkZ9/Ot99nFDjEkkargzBsDH8f0/img.png"
data-lightbox="lightbox" data-alt="RedisController"><img
src="https://blog.kakaocdn.net/dn/be47mV/btsyuhAQkZ9/Ot99nFDjEkkargzBsDH8f0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbe47mV%2FbtsyuhAQkZ9%2FOt99nFDjEkkargzBsDH8f0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="768" data-origin-height="536" /></span>
<figcaption>RedisController</figcaption>
</figure>

위와 마찬가지로 의존성 주입을 위해 \@Autowired를 사용하여 RedisService에
대한 의존성을 주입한다.

\@PostMapping을 통해서 PostMethod를, \@GetMapping을 통해서 GetMethod를
간단하게 작성했다.

 

기존의 작성되어 있던 Swagger 문서를 통해서 API를 테스트해보자.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1422" data-origin-height="194">
<span
data-url="https://blog.kakaocdn.net/dn/bewUiT/btsysJyzYgX/iwiz8lIenr1D3Rr5z2ObYk/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/bewUiT/btsysJyzYgX/iwiz8lIenr1D3Rr5z2ObYk/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbewUiT%2FbtsysJyzYgX%2Fiwiz8lIenr1D3Rr5z2ObYk%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1422" data-origin-height="194" /></span>
</figure>

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1425" data-origin-height="438">
<span
data-url="https://blog.kakaocdn.net/dn/bBlnyJ/btsytrYkLAB/XG0DcZ2Hq8CKcN4cJCcmck/img.png"
data-lightbox="lightbox" data-alt="데이터 저장 API"><img
src="https://blog.kakaocdn.net/dn/bBlnyJ/btsytrYkLAB/XG0DcZ2Hq8CKcN4cJCcmck/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbBlnyJ%2FbtsytrYkLAB%2FXG0DcZ2Hq8CKcN4cJCcmck%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1425" data-origin-height="438" /></span>
<figcaption>데이터 저장 API</figcaption>
</figure>

key에 name, value에는 heesang을 저장한다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="721" data-origin-height="762">
<span
data-url="https://blog.kakaocdn.net/dn/lPelB/btsyueD7Rw2/8ak3vggxtvMkIzJVEtTFCK/img.png"
data-lightbox="lightbox" data-alt="POST Method /redis/save"><img
src="https://blog.kakaocdn.net/dn/lPelB/btsyueD7Rw2/8ak3vggxtvMkIzJVEtTFCK/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlPelB%2FbtsyueD7Rw2%2F8ak3vggxtvMkIzJVEtTFCK%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="721" data-origin-height="762" /></span>
<figcaption>POST Method /redis/save</figcaption>
</figure>

다음엔 name이라는 key로 접근해서 value 값을 읽어본다.

 

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="788" data-origin-height="786">
<span
data-url="https://blog.kakaocdn.net/dn/bpjCeH/btsyrzJOroF/1pBDhWqhCOgLNIweF9b9iK/img.png"
data-lightbox="lightbox" data-alt="GET Method /redis/show"><img
src="https://blog.kakaocdn.net/dn/bpjCeH/btsyrzJOroF/1pBDhWqhCOgLNIweF9b9iK/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbpjCeH%2FbtsyrzJOroF%2F1pBDhWqhCOgLNIweF9b9iK%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="788" data-origin-height="786" /></span>
<figcaption>GET Method /redis/show</figcaption>
</figure>

name이라는 key로 저장되어 있는 heesang이라는 value를 가져온 것을 확인할
수 있다.

------------------------------------------------------------------------

이렇게 간단하게 Redis 디펜던시를 추가하고 RedisConfig, RedisTemplate를
통한 데이터 저장 및 조회에 대해서 다뤄보았다.

Github Link :
[https://github.com/heesane](https://github.com/heesane){target="_blank"
rel="noopener"}

<figure id="og_1697301172782" contenteditable="false"
data-ke-type="opengraph" data-ke-align="alignCenter"
data-og-type="profile" data-og-title="heesane - Overview"
data-og-description="heesane has 16 repositories available. Follow their code on GitHub."
data-og-host="github.com"
data-og-source-url="https://github.com/heesane"
data-og-url="https://github.com/heesane"
data-og-image="https://scrap.kakaocdn.net/dn/Ah7Rn/hyT9FhblTl/SMi623GQsFJQ9HgAyjjXLK/img.jpg?width=460&amp;height=460&amp;face=107_129_265_301">
<a href="https://github.com/heesane" target="_blank" rel="noopener"
data-source-url="https://github.com/heesane"></a>
<div class="og-image"
style="background-image: url(&#39;https://scrap.kakaocdn.net/dn/Ah7Rn/hyT9FhblTl/SMi623GQsFJQ9HgAyjjXLK/img.jpg?width=460&amp;height=460&amp;face=107_129_265_301&#39;);">
 
</div>
<div class="og-text">
<p>heesane - Overview</p>
<p>heesane has 16 repositories available. Follow their code on
GitHub.</p>
<p>github.com</p>
</div>
</figure>

 
