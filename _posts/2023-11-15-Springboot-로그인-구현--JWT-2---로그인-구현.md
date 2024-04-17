---
title: "[Springboot] 로그인 구현 & JWT (2) - 로그인 구현"
author: heesang
platform: 
date: 2023-11-15 01:05:13 +0900
categories: [Backend/Framework, dependencies, JWT, Login, security, SpringBoot, SpringSecurity, token, 로그인 구현]
tags: ["Backend/Framework", "dependencies", "JWT", "Login", "security", "SpringBoot", "SpringSecurity", "token", "로그인 구현"]
toc: true
comments: true
---
<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="750" data-origin-height="343">
<span
data-url="https://blog.kakaocdn.net/dn/Dxp4y/btsAjiR84P1/YmjKFDcrl9XTxxncQTLJX1/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/Dxp4y/btsAjiR84P1/YmjKFDcrl9XTxxncQTLJX1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FDxp4y%2FbtsAjiR84P1%2FYmjKFDcrl9XTxxncQTLJX1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="750" data-origin-height="343" /></span>
</figure>

지난 포스팅에서 JWT의 개념에 대해서 알아봤으니까 이번 포스팅에서는 JWT
방식을 채택해서 로그인 기능을 구현할 예정이다.

 

## Dependencies {#dependencies ke-size="size26"}

``` {#code_1699972326179 .java ke-language="java" ke-type="codeblock"}
// Spring Security
implementation 'org.springframework.boot:spring-boot-starter-security'
testImplementation 'org.springframework.security:spring-security-test'

// JWT Token
implementation 'io.jsonwebtoken:jjwt:0.9.1'
```

 

\'org.springframework.boot:spring-boot-starter-security\' : Springboot에
Security 설정을 하기 위해서 필요한 디펜던시

\'io.jsonwebtoken:jjwt:0.9.1\' : JWT Token을 사용하기 위한 디펜던시

 

Security는 매우 광범위하고, 나같은 초보는 이해하기가 힘들기때문에 너무
Security에 관심두지 말고 천천히 공부하는게 좋을 것같다. Security에서는
Session, Cookie같은 다른 암호화 방식을 통해서 구현을 할 수도 있고, API에
접근할 때, 권한을 요청한다던지 토큰을 요구하도록 설계할 수 있다. 자세한
내용은 미래의 포스팅에서 다루도록 하겠다.

 

------------------------------------------------------------------------

## Config {#config ke-size="size26"}

Springboot에서 Bean을 등록하는 방법은 2가지가 존재한다. 첫 번째로는
Component Scan을 통해서 Bean을 등록하는 방법. 두 번째로는
Configuration을 통해서 Bean을 등록하게 된다. 주로 Config에서는
Configuration과 Bean 어노테이션을 사용해서 Bean을 등록하고 스프링
컨테이너를 통해서 관리하게 된다.

 

JWT를 사용하기 위해서는 2가지의 Config 파일이 필요한데, 첫 번째로는
유저의 정보를 encode하기 위한 BCryptConfig.

두번째로는 Springboot Security를 설정하기 위한 Config 파일이 필요하다.

 

### BCryptConfig {#bcryptconfig ke-size="size23"}

``` {#code_1699973708357 .java ke-language="java" ke-type="codeblock"}
package unknown.backend.dev.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

@Configuration
public class BCryptConfig {
    @Bean
    public BCryptPasswordEncoder bCryptPasswordEncoder(){
        return new BCryptPasswordEncoder();
    }
}
```

 

BCryptConfig는 위처럼 설정한다.

추후에 Join이나 Register와 같은 Service를 개발할 때, 유저의 Password를
Encode해서 저장한다.

------------------------------------------------------------------------

### SecurityConfig {#securityconfig ke-size="size23"}

``` {#code_1699973883637 .java ke-language="java" ke-type="codeblock"}
@Configuration
@EnableWebSecurity
@RequiredArgsConstructor
public class SecurityConfig {

    private final UserService userService;
    private static String secretKey;
    @Autowired
    public SecurityConfig(@Value("${custom.jwt.secret}") String secretKey, UserRepository userRepository, EntityManager em, BCryptPasswordEncoder encoder) {
        this.userService = new UserService(userRepository, em, encoder);
        this.secretKey = secretKey;
    }
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity httpSecurity) throws Exception {
        return httpSecurity
                .httpBasic().disable()
                .csrf().disable()
                .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
                .and()
                .addFilterBefore(new JwtTokenFilter(userService, secretKey), UsernamePasswordAuthenticationFilter.class)
                .authorizeRequests()
                .antMatchers("/api/v1/chat/room/enter").authenticated()
                .antMatchers("/jwt-login/info").authenticated()
                .and().build();
    }
}
```

 

SecurityConfig는 위와 같이 설정한다.

Token 방식은 Session이 필요하지 않으므로, STATELESS로 설정하였다.

다음으로 Filter를 적용하기 전에 JWT  Token Filter를 거친 이후에 Filter에
가도록 설정하였다.

그 아래는 권한을 필요로 하는 요청에 관한 내용이다.

/api/v1/chat/room/enter 라는 API를 호출하기 위해서는 HTTP Header의
Authorization에 JWT Token을 전달해야만 접근이 가능하다 라는 것을
의미한다.

 

------------------------------------------------------------------------

### JWT Token Filter {#jwt-token-filter ke-size="size23"}

``` {#code_1699975594673 .java ke-language="java" ke-type="codeblock"}
// OncePerRequestFilter : 매번 들어갈 때 마다 체크 해주는 필터
@RequiredArgsConstructor
public class JwtTokenFilter extends OncePerRequestFilter {

    private final UserService userService;
    private final String secretKey;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        String authorizationHeader = request.getHeader(HttpHeaders.AUTHORIZATION);

        // Header의 Authorization 값이 비어있으면 => Jwt Token을 전송하지 않음 => 로그인 하지 않음
        if(authorizationHeader == null) {
            filterChain.doFilter(request, response);
            return;
        }

        // Header의 Authorization 값이 'Bearer '로 시작하지 않으면 => 잘못된 토큰
        if(!authorizationHeader.startsWith("Bearer ")) {
            filterChain.doFilter(request, response);
            return;
        }

        // 전송받은 값에서 'Bearer ' 뒷부분(Jwt Token) 추출
        String token = authorizationHeader.split(" ")[1];
        System.out.println("token = " + token);
        // 전송받은 Jwt Token이 만료되었으면 => 다음 필터 진행(인증 X)
        if(JwtTokenUtil.isExpired(token, this.secretKey)) {
            filterChain.doFilter(request, response);
            return;
        }

        // Jwt Token에서 loginId 추출
        String Email = JwtTokenUtil.getLoginId(token, secretKey);
        System.out.println("Email = " + Email);
        // 추출한 loginId로 User 찾아오기
        User loginUser = userService.getLoginUserByEmail(Email);
        System.out.println("loginUser = " + loginUser);
        // loginUser 정보로 UsernamePasswordAuthenticationToken 발급
        UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(loginUser.getEmail(), null, List.of(new SimpleGrantedAuthority(loginUser.getRole().name())));
        authenticationToken.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));

        // 권한 부여
        SecurityContextHolder.getContext().setAuthentication(authenticationToken);
        filterChain.doFilter(request, response);
    }
}
```

 

위에서 언급했듯이 authrized된 API를 호출하기 위해서는 HTTP Header에
JWT를 넣어야한다.

위의 코드는 서버로 요청된 HTTP 요청의 Header를 추출한 다음,
Authorization이 없거나, Bearer로 시작하지 않는다면 Exception을 뱉게
된다.

정상적으로 헤더에 토큰이 들어있는 경우, 해당 토큰에 권한을 부여하게
된다.

------------------------------------------------------------------------

### JWT Token Util {#jwt-token-util ke-size="size23"}

``` {#code_1699975884114 .java ke-language="java" ke-type="codeblock"}
public class JwtTokenUtil {

    // JWT Token 발급
    public static String createToken(String Email, String key, long expireTimeMs) {
        // Claim = Jwt Token에 들어갈 정보
        // Claim에 loginId를 넣어 줌으로써 나중에 loginId를 꺼낼 수 있음
        Claims claims = Jwts.claims();
        claims.put("Email", Email);

        return Jwts.builder()
                .setClaims(claims)
                .setIssuedAt(new Date(System.currentTimeMillis()))
                .setExpiration(new Date(System.currentTimeMillis() + expireTimeMs))
                .signWith(SignatureAlgorithm.HS256, key)
                .compact();
    }

    // Claims에서 loginEmail 꺼내기
    public static String getLoginEmail(String token, String secretKey) {
        return extractClaims(token, secretKey).get("Email").toString();
    }

    // 발급된 Token이 만료 시간이 지났는지 체크
    public static boolean isExpired(String token, String secretKey) {
        Date expiredDate = extractClaims(token, secretKey).getExpiration();
        // Token의 만료 날짜가 지금보다 이전인지 check
        return expiredDate.before(new Date());
    }

    // SecretKey를 사용해 Token Parsing
    private static Claims extractClaims(String token, String secretKey) {
        return Jwts.parser().setSigningKey(secretKey).parseClaimsJws(token).getBody();
    }
}
```

 

이전 포스팅에서 언급했던 내용이다.

Claims에 들어가야할 내용들을 정의하고 JWT를 만들기 위한 코드이다.

추가적으로 Token에 들어있는 Expiration과 발행 시간을 비교하여 만료된
토큰인지 파악하고

LoginEmail을 추출, Token과 Secret Key를 통해 Parsing하는 메서드를
정의하였다.

 

------------------------------------------------------------------------

### RegisterRequestDTO {#registerrequestdto ke-size="size23"}

유저의 구조는 단순하게 Email과 Password의 구조라고 하자.

``` {#code_1699976323223 .java ke-language="java" ke-type="codeblock"}
@Getter
@Setter
@Builder
public class RegisterRequest {
    @ApiModelProperty(example = "유저 이름")
    private final String username;
    @ApiModelProperty(example = "유저 비밀번호")
    private final String password;
    @ApiModelProperty(example = "유저 비밀번호 확인")
    private final String passwordConfirm;
    @ApiModelProperty(example = "유저 이메일")
    private final String email;

    public User toEntity(String encodedPassword) {
        return User.builder()
                .username(username)
                .password(encodedPassword)
                .email(email)
                .build();
    }
}
```

 

위와 같은 RegistereRequest를 통해서 UserService로 전달하고,
password부분은 이전에 선언하였던 BCryptEncoder를 통해서 Encode된
형식으로 DateBase에 저장하도록 설계하였다.

### UserService - Register {#userservice---register ke-size="size23"}

``` {#code_1699976402551 .java ke-language="java" ke-type="codeblock"}
public void registerUser(RegisterRequest registerRequest) {
        // 이메일 중복 확인
        userRepository.save(registerRequest.toEntity(encoder.encode(registerRequest.getPassword())));
    }
```

 

------------------------------------------------------------------------

### UserService - Login {#userservice---login ke-size="size23"}

``` {#code_1699976457899 .java ke-language="java" ke-type="codeblock"}
public User login(LoginRequest loginRequest) {
        Optional optionalUser = userRepository.findByEmail(loginRequest.getLoginEmail());
        if (optionalUser.isEmpty()) {
            return null;
        }
        User user = optionalUser.get();
        if (!encoder.matches(loginRequest.getPassword(), user.getPassword())) {
            return null;
        }
        return user;
    }
```

``` {#code_1699976520409 .java ke-language="java" ke-type="codeblock"}
public class LoginRequest {
    private String loginEmail;
    private String password;

}
```

 

아래의 코드블럭같이 Email과 Password을 입력받아서 DTO를 통해서 login
함수를 호출한다.

UserRepository에 선언한 findByEmail을 통해서 해당 이메일을 갖고있는
유저를 파악하고 Optional을 통해서 NPE를 방지한다. isEmpty() 인 경우,
null을 반환한다.

 

다음으로, encoder의 matches 메서드를 사용해서 입력받은 password와
사용자가 입력한 password를 비교하여 동일하다면 user를 반환하도록
설계하였다.

------------------------------------------------------------------------

 

여기까지 했다면, 구현은 완료한 것이다.

다음으로는 Postman을 통해서 Test를 할 예정이다

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="1165" data-origin-height="430">
<span
data-url="https://blog.kakaocdn.net/dn/AsMj2/btsAjURVMJm/uDKjmWMiA3GfraMW47UDp1/img.png"
data-lightbox="lightbox" data-alt="Postman"><img
src="https://blog.kakaocdn.net/dn/AsMj2/btsAjURVMJm/uDKjmWMiA3GfraMW47UDp1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FAsMj2%2FbtsAjURVMJm%2FuDKjmWMiA3GfraMW47UDp1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="1165" data-origin-height="430" /></span>
<figcaption>Postman</figcaption>
</figure>

 

위와 같은 화면에서 테스트를 진행 할 예정인데, 기존의 register API를
사용해서 회원 가입을 한 이후이다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="397" data-origin-height="147">
<span
data-url="https://blog.kakaocdn.net/dn/LSo3B/btsAmyVb8dl/kCpFTk3Ebq0zNnFvEfvJv0/img.png"
data-lightbox="lightbox" data-alt="LoginRequestDTO"><img
src="https://blog.kakaocdn.net/dn/LSo3B/btsAmyVb8dl/kCpFTk3Ebq0zNnFvEfvJv0/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLSo3B%2FbtsAmyVb8dl%2FkCpFTk3Ebq0zNnFvEfvJv0%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="397" data-origin-height="147" /></span>
<figcaption>LoginRequestDTO</figcaption>
</figure>

이전에 설명했던 LoginRequestDTO와 같이 loginEmail과 password를 입력하고
/api/v1/users/login의 경로로 POST를 실행한다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="870" data-origin-height="243">
<span
data-url="https://blog.kakaocdn.net/dn/4Zknu/btsAmFfFwZr/8C6JlP8Kl3wqMK7jc2BHJ1/img.png"
data-lightbox="lightbox" data-alt="JWT Token"><img
src="https://blog.kakaocdn.net/dn/4Zknu/btsAmFfFwZr/8C6JlP8Kl3wqMK7jc2BHJ1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F4Zknu%2FbtsAmFfFwZr%2F8C6JlP8Kl3wqMK7jc2BHJ1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="870" data-origin-height="243" /></span>
<figcaption>JWT Token</figcaption>
</figure>

이제 /jwt-login/info로 Token을 헤더에 담아서 GET요청을 해보겠다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="766" data-origin-height="376">
<span
data-url="https://blog.kakaocdn.net/dn/ppmmg/btsAm4e9CjX/hyl3cDNEik5w71yFwZMzt1/img.png"
data-lightbox="lightbox" data-alt="Header에 Token 삽입"><img
src="https://blog.kakaocdn.net/dn/ppmmg/btsAm4e9CjX/hyl3cDNEik5w71yFwZMzt1/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fppmmg%2FbtsAm4e9CjX%2Fhyl3cDNEik5w71yFwZMzt1%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="766" data-origin-height="376" /></span>
<figcaption>Header에 Token 삽입</figcaption>
</figure>

반드시 헤더에 Authorization을 추가하고 JWT Token을 넣어주어야 한다.

또 하나 주의해야할 것은 토큰을 입력할 때, \"Bearer \" 이라는 접두어를
포함해야한다는 것이다.

이를 지키지 않으면 오류가 발생할 수 있으니, 만약 오류가 발생한다면
토큰을 제대로 입력했는지 확인한다.

 

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin"
data-origin-width="297" data-origin-height="97">
<span
data-url="https://blog.kakaocdn.net/dn/9aNmO/btsAeBy8VFR/fsgnpySlbNaj1C4hKWkUkK/img.png"
data-lightbox="lightbox"><img
src="https://blog.kakaocdn.net/dn/9aNmO/btsAeBy8VFR/fsgnpySlbNaj1C4hKWkUkK/img.png"
srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F9aNmO%2FbtsAeBy8VFR%2FfsgnpySlbNaj1C4hKWkUkK%2Fimg.png"
onerror="this.onerror=null; this.src=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;; this.srcset=&#39;//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png&#39;;"
data-origin-width="297" data-origin-height="97" /></span>
</figure>

GET 요청을 전달해보면, 서버쪽으로 요청이 제대로 전달되어서 유저의 정보가
보여지는 것을 확인할 수 있다.

 

------------------------------------------------------------------------

이전에 개인적으로 JWT를 시도한 적이 있었는데, 당시에는 처참하게 실패를
했던 경험이 있다. 그 당시에는 Security를 정확하게 이해하려 노력했었고
결국은 수 많은 오류때문에 포기했었었다. 이번에는 나에게 필요한 부분만
구현하여 API가 정상적으로 동작하는 것을 확인할 수 있었고 과정에서 많은
것들을 알고 공부할 수 있었던 시간이 되었다.
