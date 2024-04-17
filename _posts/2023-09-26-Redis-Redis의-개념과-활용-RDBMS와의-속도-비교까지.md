---
title: "[Redis] Redis의 개념과 활용, RDBMS와의 속도 비교까지"
author: heesang
platform: 
date: 2023-09-26 17:54:39 +0900
categories: [DB SQL]
tags: ["DB SQL"]
toc: true
comments: true
---
<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1200" data-origin-height="401">
<span
data-url="https://blog.kakaocdn.net/dn/cqNnhl/btsvHbRGKKB/BprwLkuGQgm4kYogR3P8A0/img.png"
data-lightbox="lightbox" data-alt="Redis"><img
src="https://blog.kakaocdn.net/dn/cqNnhl/btsvHbRGKKB/BprwLkuGQgm4kYogR3P8A0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcqNnhl%2FbtsvHbRGKKB%2FBprwLkuGQgm4kYogR3P8A0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1200" data-origin-height="401" /></span>
<figcaption>Redis</figcaption>
</figure>

> Redis는 No-SQL의 한 종류로, key 값과 value 값의 형식으로 데이터를
> 저장하는 DBMS의 한 종류입니다.\
> 이번에는 Redis의 개념과 실습을 통해서 Redis를 왜 사용하는지와 어떻게
> 사용하는지에 대해서 알아보도록 하겠습니다.

## Redis가 무엇인가? {#redis가-무엇인가 ke-size="size26"}

메모리를 사용해 Key값과 Value값을 한 쌍으로 묶어 처리하는 데이터베이스
관리 시스템입니다. Redis 데이터는 메모리에 상주하므로, 데이터 액세스의
대기시간을 낮추고 처리량을 높이게 됩니다. 기존의 DBMS에서는 Disk에
데이터를 저장하게 되는 구조로, 데이터를 조회하거나 트랜잭션을 수행할 때
약간의 시간이 소모되게 됩니다. 하지만 Redis의 경우에는 Disk보다 빠른
속도를 가지는 Memory에 데이터를 저장하는 In-Memory의 방식을 채택하여
보다 빠른 처리 속도와 효율성을 지닙니다.

------------------------------------------------------------------------

## 기존의 DBMS VS Redis {#기존의-dbms-vs-redis ke-size="size26"}

Redis에서는 기존의 RDBMS에서는 지원하지 않는 여러 자료형과 데이터 형식을
지원하는데, Hashes형태, Lists형태, Sets형태 등 다양한 자료형을
제공합니다. 또한 RDBMS에서는 SQL 문을 작성하여 DBMS를 제어하는 반면
Redis에서는 SQL문이 필요 없는 구조입니다.

또한, In-Memory구조상 DBMS보다는 훨씬 더 빠른 속도로 데이터를 처리하게
됩니다.

------------------------------------------------------------------------

## Redis의 기본 자료구조 {#redis의-기본-자료구조 ke-size="size26"}

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="877" data-origin-height="520">
<span
data-url="https://blog.kakaocdn.net/dn/crbZ8q/btsvXV0GhOO/vRKF6RRsAmAbYVyaw9S3hk/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/crbZ8q/btsvXV0GhOO/vRKF6RRsAmAbYVyaw9S3hk/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcrbZ8q%2FbtsvXV0GhOO%2FvRKF6RRsAmAbYVyaw9S3hk%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="877" data-origin-height="520" /></span>
</figure>

Redis에서는 위의 사진과 같은 자료구조를 제공하고 사용할 수 있습니다.

-   Strings : Vinary-Safe 한 기존적인 key-value 구조
-   Bitmaps, Bit field : Bit Array를 다룰 수 있는 자료구조
-   Hashes : 내부에 key-value 쌍의 구조를 하나 더 가지는 Redis의
    자료구조
-   Lists : String Element의 모음으로, 순서는 입력된 순서에 맞춰
    삽입되고 기본적으로 Linked Lists의 구조를 띄는 자료구조
-   Sets : 중복된 값들이 존재할 때, 중복을 삭제한 집합 자료구조
-   Sorted Sets : Sets 자료구조에서 순서에 맞춰 정렬한 Sets 자료구조
-   Geospatial Indexes : 2차원 평면상의 좌표를 입력하고 각 객체별로
    거리를 측정할 수 있도록 도와주는 자료구조
-   HyperLogLogs : 집합의 원소의 개수를 추정하는 방법. Set 자료구조에서
    발전된 자료구조
-   Streams : Log나 IoT와 같이 지속적으로 빠르게 발생하는 데이터를
    처리하기 위한 자료구조

------------------------------------------------------------------------

## Redis의 활용방법 {#redis의-활용방법 ke-size="size26"}

-   Caching : 데이터베이스나 파일 시스템 등의 느린 데이터 저장소에 대한
    액세스를 줄이고, 더 빠른 데이터 액세스를 위해서 데이터를 메모리에
    저장한다. 레디스를 이용한 캐싱을 웹 사이트나 애플리케이션에서
    데이터베이스 쿼리  등의 불필요한 액세스를 줄이고 빠른 응답 속도를
    제공할 수 있다.
-   Session Storage : Session이란 사용자 상태를 유지하기 위한 방법인데,
    Redis를 통해서 세션 데이터를 저장하면 다수의 서버에서 액세스 할 수
    있는 세션 데이터를 공유할 수 있으며, 확장성을 높일 수 있다.
-   MQ : 또한 메시지 큐의 역할을 수행할 수 있는데, 메시지 큐는
    비동기적인 메시지 처리를 지원하는 소프트웨어 패턴으로 Sender와
    Receiver 간의 통신을 통해 데이터 처리를 수행한다. 또한 Pub/Sub 
    기능을 통해 메시지 큐를 구현할 수 있으며, 높은 처리량과 낮은
    지연시간을 제공한다.
-   Real-Time Chat : Pub/Sub 기능을 통해서 다수의 클라이언트 간의 실시간
    메시지 전달을 할 수 있다.

------------------------------------------------------------------------

## 너가 그렇게 빨라? {#너가-그렇게-빨라 ke-size="size26"}

얼마나 빠른지 한 번 확인을 해보면 좋을 것 같으니까 로컬에서 한 번
테스트를 해보도록 하겠습니다.

 

**1. Fast API 서버를 위한 가상환경 세팅**

``` {#code_1695710196600 .python ke-language="python" ke-type="codeblock"}
python -m venv redis_test
```

가상환경을 활성화시켜 준 뒤 다음 단계에 따라서 진행하겠습니다.

------------------------------------------------------------------------

**2. docker-compose.yml 파일 작성**

``` {#code_1695710277403 .shell style="background-color: #f8f8f8; color: #383a42; text-align: start;" ke-type="codeblock" ke-language="shell"}
version: '3'
services:
  redis:
    image: redis:latest
    ports:
      - "6379:6379"
  
  postgres:
    image: postgres:latest
    environment:
      POSTGRES_PASSWORD: examplepassword
      POSTGRES_DB: exampledb
    ports:
      - "5432:5432"

  api:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - redis
      - postgres
    command: "uvicorn main:app --reload --port 8000 --host 0.0.0.0"
```

redis는 추가적인 세팅은 필요 없고, postgres는 유저의 ID, Password가
필요하고 어떤 DB를 사용할 것인지 정해줘야 하기 때문에 testdb라는 설정을
해줍니다. 이후에 docker를 실행하면 localhost:8000/docs로 가서 API를
테스트할 수 있습니다.

------------------------------------------------------------------------

**3. Dockerfile 작성**

``` {#code_1695710474282 .shell style="background-color: #f8f8f8; color: #383a42; text-align: start;" ke-type="codeblock" ke-language="shell"}
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install psycopg2-binary redis
COPY . /app
```

docker를 통해서 redis와 postgres, API 서버까지 한 번에 실행할 예정으로
API를 Build 하기 위한 Dockerfile을 작성합니다.

------------------------------------------------------------------------

**4. Fast API main.py 작성**

``` {#code_1695710554658 .python style="background-color: #f8f8f8; color: #383a42; text-align: start;" ke-type="codeblock" ke-language="python"}
import time
from functools import wraps
from typing import Callable

import psycopg2
import redis
from fastapi import FastAPI, HTTPException
from psycopg2 import sql


def timeit(func: Callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        result["elapsed_time"] = elapsed_time
        return result
    return wrapper

app = FastAPI()

redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)
postgres_conn = psycopg2.connect(
    host="postgres", user="postgres", password="examplepassword", dbname="exampledb"
)


@app.on_event("startup")
async def startup_event():
    cursor = postgres_conn.cursor()
    cursor.execute(sql.SQL("CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name VARCHAR(255))"))
    cursor.close()
    postgres_conn.commit()


@app.post("/items/redis/{name}")
@timeit
async def create_item_redis(name: str):
    redis_client.set(name, name)
    return {"name": name}


@app.get("/items/redis/{name}")
@timeit
async def read_item_redis(name: str):
    value = redis_client.get(name)
    if value is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": value}


@app.post("/items/postgres/{name}")
@timeit
async def create_item_postgres(name: str):
    cursor = postgres_conn.cursor()
    cursor.execute(sql.SQL("INSERT INTO items (name) VALUES (%s) RETURNING id"), (name,))
    id_of_new_row = cursor.fetchone()[0]
    cursor.close()
    postgres_conn.commit()
    return {"id": id_of_new_row, "name": name}


@app.get("/items/postgres/{name}")
@timeit
async def read_item_postgres(name: str):
    cursor = postgres_conn.cursor()
    cursor.execute(sql.SQL("SELECT * FROM items WHERE name=%s"), (name,))
    row = cursor.fetchone()
    cursor.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": row[0], "name": row[1]}
```

[총 4개의 API를 만들었는데, 간단하게 Redis로 추가와 조회, Postgres로
데이터 추가와 조회 기능을
구현했습니다.]{style="color: #374151;"}[\@timeit라는 Annotation을
정의하여, DBMS에서 데이터를 처리하는데 어느 정도의 시간이 걸리는지
출력하여 확인해 보겠습니다.]{style="color: #374151;"}

------------------------------------------------------------------------

**5. Docker-compose.yml으로 Docker Container 실행**

``` {#code_1695714951356 .vala style="background-color: #f8f8f8; color: #383a42; text-align: start;" ke-type="codeblock" ke-language="shell"}
# docker-compose.yml파일이 있는 경로에서..
docker-compose up -d
```

docker-compose up -d 명령어를 실행하면, docker-compose.yml 안에 설정해
둔 redis와 postgres 컨테이너들이 daemon으로 실행되게 된다. daemon이란
background에서 실행된다는 뜻이다.

``` {#code_1695715019297 .shell ke-language="shell" ke-type="codeblock"}
docker ps
```

정상적으로 실행되고 있는지 확인해 보면,

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1180" data-origin-height="83">
<span
data-url="https://blog.kakaocdn.net/dn/b6Lqa0/btsvMVus5Il/GJ0HxjovVx8KGO9QKGSKq1/img.png"
data-lightbox="lightbox" data-alt="docker ps 실행결과"><img
src="https://blog.kakaocdn.net/dn/b6Lqa0/btsvMVus5Il/GJ0HxjovVx8KGO9QKGSKq1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb6Lqa0%2FbtsvMVus5Il%2FGJ0HxjovVx8KGO9QKGSKq1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1180" data-origin-height="83" /></span>
<figcaption>docker ps 실행결과</figcaption>
</figure>

정상적으로 redis container와 postgres container, FastAPI 서버가 동작하고
있는 것을 확인할 수 있다.

------------------------------------------------------------------------

**6. Localhost:8000 접속**

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="748" data-origin-height="166">
<span
data-url="https://blog.kakaocdn.net/dn/LhTAm/btsvNOokFZo/TDugh3p0iIs7GFdBPeWz3K/img.png"
data-lightbox="lightbox" data-alt="첫 접속"><img
src="https://blog.kakaocdn.net/dn/LhTAm/btsvNOokFZo/TDugh3p0iIs7GFdBPeWz3K/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLhTAm%2FbtsvNOokFZo%2FTDugh3p0iIs7GFdBPeWz3K%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="748" data-origin-height="166" /></span>
<figcaption>첫 접속</figcaption>
</figure>

localhost:8000번에 FastAPI가 실행되면서 Not Found를 뱉는 것을 볼 수
있다.

우리가 확인하려고 하는 것은 API 테스트를 통한 시간 차이이기 때문에,
/docs로 이동한다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1438" data-origin-height="407">
<span
data-url="https://blog.kakaocdn.net/dn/caAHMs/btsvMENf1Wi/VisKGE2vkmZyRGy9AiIrJk/img.png"
data-lightbox="lightbox" data-alt="localhost:8000/docs"><img
src="https://blog.kakaocdn.net/dn/caAHMs/btsvMENf1Wi/VisKGE2vkmZyRGy9AiIrJk/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcaAHMs%2FbtsvMENf1Wi%2FVisKGE2vkmZyRGy9AiIrJk%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1438" data-origin-height="407" /></span>
<figcaption>localhost:8000/docs</figcaption>
</figure>

 /docs 라우트로 이동하면 다음과 같은 화면이 나오게 되는데, 여기서
화살표를 눌러 펼치고 

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1431" data-origin-height="292">
<span
data-url="https://blog.kakaocdn.net/dn/VvByW/btsvHenELh1/TyZ7iwtOpOnAqx9IIMIP3K/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/VvByW/btsvHenELh1/TyZ7iwtOpOnAqx9IIMIP3K/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FVvByW%2FbtsvHenELh1%2FTyZ7iwtOpOnAqx9IIMIP3K%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1431" data-origin-height="292" /></span>
</figure>

Try it out을 통해 API를 테스트할 수 있다. 

------------------------------------------------------------------------

**7. 속도비교**

우선 지금은 아무런 데이터도 존재하지 않으니까, POST 메서드를 통해서
데이터를 삽입한 이후에 데이터 처리 속도를 비교해 보면,

<figure class="imageblock floatRight" data-ke-mobilestyle="widthOrigin"
data-origin-width="313" data-origin-height="70">
<span
data-url="https://blog.kakaocdn.net/dn/UWT29/btsvM2G9O0n/lxGhHRLGbKMKekERsOewO0/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/UWT29/btsvM2G9O0n/lxGhHRLGbKMKekERsOewO0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FUWT29%2FbtsvM2G9O0n%2FlxGhHRLGbKMKekERsOewO0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="313" data-origin-height="70" width="443"
height="99" /></span>
</figure>

**Redis POST**

 

 

------------------------------------------------------------------------

<figure class="imageblock floatRight" data-ke-mobilestyle="widthOrigin"
data-origin-width="322" data-origin-height="74">
<span
data-url="https://blog.kakaocdn.net/dn/cexkKe/btsvQbQ7G9m/UcLDat1zw0b06D2WdiGejk/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/cexkKe/btsvQbQ7G9m/UcLDat1zw0b06D2WdiGejk/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcexkKe%2FbtsvQbQ7G9m%2FUcLDat1zw0b06D2WdiGejk%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="322" data-origin-height="74" width="439"
height="101" /></span>
</figure>

**Redis GET**

 

 

------------------------------------------------------------------------

<figure class="imageblock floatRight" data-ke-mobilestyle="widthOrigin"
data-origin-width="274" data-origin-height="79">
<span
data-url="https://blog.kakaocdn.net/dn/dERVsP/btsvXTa0UAD/A8F7ROopJHVg5OQrV4S9D0/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/dERVsP/btsvXTa0UAD/A8F7ROopJHVg5OQrV4S9D0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdERVsP%2FbtsvXTa0UAD%2FA8F7ROopJHVg5OQrV4S9D0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="274" data-origin-height="79" width="430"
height="124" /></span>
</figure>

**Postgres POST**

 

##   {#section ke-size="size26"}

------------------------------------------------------------------------

<figure class="imageblock floatRight" data-ke-mobilestyle="widthOrigin"
data-origin-width="295" data-origin-height="81">
<span
data-url="https://blog.kakaocdn.net/dn/bV7jIX/btsvXjVk6NG/7je2t1gkXU1otxXJP71Zh1/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/bV7jIX/btsvXjVk6NG/7je2t1gkXU1otxXJP71Zh1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbV7jIX%2FbtsvXjVk6NG%2F7je2t1gkXU1otxXJP71Zh1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="295" data-origin-height="81" width="430"
height="118" /></span>
</figure>

**Postgres GET**

 

 

 

------------------------------------------------------------------------

POST method : Redis 0.00025 sec vs Postgres 0.00385 sec      -\> 약 15배
빠른 속도

GET method : Redis 0.00033 sec vs Postgres 0.00046 sec        -\> 약
1.4배 빠른 속도 

 

이번 글에서는 Redis나 Postgre에 들어가 있는 데이터의 양이 매우 적은
케이스여서 속도의 비교가 무의미할 정도의 매우 빠른 속도를 보이지만, 적은
데이터양에서도 이러한 속도차이가 발생하는 것을 확인할 수 있었다.

프로젝트나 공모전, 사이드 프로젝트를 진행하게 된다면, 대량의 API 호출과
트래픽이 발생할 경우, MySQL 같은 전통적인 RDBMS는 트랜잭션을 잘 관리해야
사용자가 시스템을 사용할 때 불편함을 느끼지 못하는데, 이런 대량의 데이터
처리에서 Redis를 도입해서 해결해 보는 것도 좋은 케이스일 것이다.

##   {#section-1 ke-size="size26"}

##   {#section-2 ke-size="size26"}

##   {#section-3 ke-size="size26"}

##   {#section-4 ke-size="size26"}

##   {#section-5 ke-size="size26"}

##   {#section-6 ke-size="size26"}

##   {#section-7 ke-size="size26"}

##   {#section-8 ke-size="size26"}

##   {#section-9 ke-size="size26"}

##   {#section-10 ke-size="size26"}

##   {#section-11 ke-size="size26"}

## Redis 공식 문서 {#redis-공식-문서 ke-size="size26"}

[https://redis.io/docs/](https://redis.io/docs/ "Redis 공식문서"){target="_blank"
rel="noopener"}

<figure id="og_1695708790352" contenteditable="false"
data-ke-type="opengraph" data-ke-align="alignCenter"
data-og-type="website" data-og-title="Documentation"
data-og-description="Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker"
data-og-host="redis.io" data-og-source-url="https://redis.io/docs/"
data-og-url="https://redis.io/docs/" data-og-image="">
<a href="https://redis.io/docs/" target="_blank" rel="noopener"
data-source-url="https://redis.io/docs/"></a>
<div class="og-image" style="background-image: url();">
 
</div>
<div class="og-text">
<p>Documentation</p>
<p>Redis is an open source (BSD licensed), in-memory data structure
store, used as a database, cache, and message broker</p>
<p>redis.io</p>
</div>
</figure>

 
