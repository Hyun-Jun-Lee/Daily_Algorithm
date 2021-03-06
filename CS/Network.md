# Network


<details>
    <summary>TCP/IP?</summary>

    - TCP/IP : 인터넷에서 표준으로 사용되는 프로토콜(통신규약)

        - Application Layer(L5)
            - 네트워크 계층과 애플리케이션 계층 프로토콜이 있는 곳이다.
            - 도메인 주소를 네트워크 주소로 변환하는 기능을 위한 DNS 지원
            - 애플리케이션 계층 패킷을 Message 라고 함.

        - Transport Layer(L4) 
            - 네트워크 계층에서 보내온 데이터를 정렬하고 오류를 수정 하여 신뢰할 수 있는 통신 확보
            - TCP/UDP 같은 프로토콜이 이 계층에 위치
            - 트랜스포트 계층 패킷을 Segment 라고 함.

        - Network Layer(L3)
            - 다른 네트워크로 데이터를 전송하는 역활을 수행, 즉 네트워크간 통신 역활!
            - 다른 네트워크와 통신하기 위해 경로를 설정하고 논리 주소를 결정하는 Router 장비 사용(경로설정)
            - 패킷은 Datagram

        - Data link Layer(L2)
            - 네트워크 기기 간 데이터 전송 및 물리주소 결정하는 역활
            - 이더넷 프로토콜 사용, Switch 같은 장비 사용
            - 패킷은 Frame

        - Physical Layer(L1)
            - 물리적 연결 및 전기신호 변환/제어 담당
            - 컴퓨터와 네트워크 장비를 물리적으로 연결

</details>


<details>
    <summary>OSI7 계층 vs TCP/IP</summary>

    - OSI 7계층은 TCP/IP 계층을 더 세분화 한 것
    - TCP/IP 에서 L1, L2 계층을 합쳐 네트워크 인터페이스 계층이라고 부르기도함
    - TCP/IP 에서 응용 계층은 OSI 에서 응용 표현 세션 계층으로 나뉘어짐
      - Application Layer : 사용자, 애플리케이션이 네트워크에 접근할 수 있도록 해주는 계층 / 인터페이스 지원, 사용자 에게 보이는 유일한 계층
      - Presentation Layer : 응용 계층으로 부터 전달, 전송하는 데이터의 인코딩 및 디코딩이 이루어지는 계층 / 응용계층에 맞춰 데이터를 변환
      - Session Layer : 응용프로세스가 통신을 관리하기 위한 방법 정의 / 네트워크상 양쪽의 연결을 관리/지속시키는 역할과 세션을 만들거나 없애는 역할을 담당하는 계층
</details>

<details>
    <summary>TCP vs UDP</summary>

    - TCP는 연결 지향형 프로토콜 / UDP는 데이터를 데이터그램 단위로 전송하는 프로토콜
    - TCP는 가상 회선을 만들어 신뢰성 보장하도록(흐름, 혼잡, 오류 제어)하는 프로토콜 / UDP는 따로 신뢰성 보장하는 절차 없어서 빠름
      - 흐름제어 : 상대방이 받을 수 있는 만큼만 데이터를 효율적으로 전송하는 것
      - 오류제어 : 데이터의 오류나 누락 없이 안전한 전송을 보장하는 것, 오류가 발생하면 재전송 수행하여 이를 보정
      - 혼잡제어 : 넽워크의 혼잡 정도에 따라 송신자가 데이터 전송량을 제어하는 것, 혼잡의 정도에 대한 판단기준은 데이터의 손실 발생 유무로 판단
    - TCP는 파일 전송과 같은 신뢰성이 중요한 서비스에 사용 / UDP는 스트리밍과 같이 연속성이 중요한 서비스에 사용

    - TCP 연결 과정 : 3 way handshake, 4 way handshake (양방향 Connection)
    - TCP segment를 제대로 수신하면 ACK, 제대로 수신 못하면 NACK
    - TCP segment에서 Header 부분에 오류를 체크하는 Checksum이 있다.

</details>

<details>
    <summary> Frame, Packet, Segment, Datagram 비교 </summary>

    - Packet : 컴퓨터간 데이터 주고 받을 때, 네트워크를 통해 전송데는 데이터 조각. 데이터의 손실 방지 및 패킷 흐름 조절을 위해 일정 단위로 잘라서 보내게됨
    각 계층에서 필요한 정보는 캡슐화 되어 전달, 수신측은 받은 패킷을 재조립하여 사용
    - Segment : Transport Layer(L4)에서 신뢰성 있는 통신을 구현하기 위한 Header를 L5의 data(message)에 붙인 것.
    - Datagram : Network Layer(L3)에서 다른 네트워크와 통신하기 위한 Header를 L4의 segment에 붙인 것.
    - Frame : Datalink Layer(L2)에서 물리적인 통신 채널을 열기 위해 Packet에 Header, Trailer을 붙임.
    Trailer는 데이터 끝에 분여서 오류 검출에 사용
</details>

<details>
    <summary>3-way-handshake 와 4-way-handshake 비교</summary>

    - 3-way-handshake : 호스트 간 데이터 전송 전에 정확한 전송을 보장하기 위해 상대 컴퓨터와 사전에 세션을 수립하는 과정

        1. Client에서 Server로 연결 요청 메시지 전송(SYN)
        2. Server 에서 SYN 요청 받고 Client에게 요청을 수락 한다는 ACK와 SYN 전송하고 ACK 응답을 기다림 (이 때 Server는 SYN_RECEIVED 상태)
        3. Client는 Server에 ACK를 보내고, 이후부터 연결 (이 때 Server는 ESTABLISHED 상태)

    - 4-way-handshake : 세션을 종료할 때 수행

        1. Client가 연결을 종료하겟다는 FIN 전송
        2. Server는 일단 확인 메세지 전송(ACK)하고, 자신의 통신이 끝날 때 까지 기다림 (TIME_WAIT 상태)
        3. Server가 통신이 끝났으면 연결이 종료되었다고 Client에 FIN 전송
        4. Client에서 확인했다는 메세지(ACK) 전송
        (TIME_WAIT : Server에서 FIN을 전송하기 전에 전송한 패킷이 FIN보다 늦게 도착하는 상황 대비해 잉여 패킷을 기다리는 과정)

    - 용어
        - SYN(Synchronization): 연결요청, 세션을 설정하는데 사용되며 초기에 시퀀스 번호를 보낸다.
        - ACK(Acknowledgement): 보낸 시퀀스 번호에 TCP 계층에서의 길이 또는 양을 더한 것과 같은 값을 ACK에 포함하여 전송한다.
        - FIN(Finish) : 세션을 종료시키는데 사용되며 더 이상 보낸 데이터가 없음을 표시한다.
    
    - 3-way-handshake 와 4-way-handshake 차이
        - 연결 설정 과정과는 다르게 종료 과정에서는 아직 전송중인 데이터에 대한 경우를 고려해야하기 때문.
        - Client는 아직 Server로 부터 받지 못한 데이터가 있을 것을 대비하여 일정시간 동안 세션을 남기는 TIME_WAIT 상태 후, 데이터를 모두 보냇다는 FIN을 받으면 종료

</details>

<details>
    <summary>HTTP와 HTTPS 차이</summary>
    
    - HTTP : Server/Client 간 데이터를 주고받기 위한 프로토콜 / 암호화가 추가 되지 않았기 때문에 단순한 정보와 같은 작업만 처리 / 80번 포트 사용
    - HTTPS : HTTP에 암호화(공개키)가 추가된 프로토콜 /  암호화, 복호화 과정이 필요하기 때문에 HTTP에 비해 느리고 인증서 발급 등을 위한 비용 발생 / 443번 포트
</details>

<details>
    <summary>HTTP GET과 POST 메서드 비교</summary>
    
    - GET : Client에서 Server로 어떠한 정보를 요청할 때 사용되는 메서드
        - GET 요청은 캐시가 가능
        - GET 요청은 브라우저에 히스토리가 남음
        - GET 요청은 길이제한
    
    - POST : Client에서 Server로 리소스를 생성 및 업데이트하기 위해 데이터를 보낼 때 사용
        - 전송할 데이터를 HTTP body 부분에 담아서 보냄(GET에서 URL의 파라미터로 보냈던 name1=value1&name2=value2가 body에 담겨 보내진다 생각하면 됨)
        - POST로 데이터를 전송할 때 길이 제한이 따로 없어 용량이 큰 데이터를 보낼 때 사용하거나 GET처럼 데이터가 외부적으로 드러나는 건 아니라서 보안이 필요한 부분에 많이 사용

    - 차이점
        - 사용 목적 : GET은 데이터 요청, POST는 새로 생성 및 업데이트
        - body 유무 : GET은 HTML 메세지에 body X, POST는 데이터를 담아 보내기 때문에 당연히 body O
        - 멱등성(idempotent) : GET은 멱등, POST는 X
        - 멱등성(idempotent)? : 여러번 적용하더라도 결과가 달라지지 않는 성질
</details>

<details>
    <summary>Cookie & Session</summary>
    
    - Cookie
        - 쿠키는 클라이언트(브라우저) 로컬에 저장되는 키와 값이 들어있는 작은 데이터 파일
        - 사용자 인증이 유효한 시간을 명시 할 수 있고, 유효 시간이 정해지면 브라우저가 종료되어도 인증이 유지됨
        - 동작 방식
            1. 클라이언트가 페이지를 요청
            2. 서버에서 쿠키 생성
            3. HTTP Header에 쿠키 포함 시켜 응답
            4. 브라우저가 종료되어도 쿠키 만료 기간이 있다면 클라이언트에서 보관
            5. 같은 요청 할 경우 HTTP Header에 쿠키를 함께 보냄
            6. 서버에서 쿠키를 읽어 이전 상태 정보를 변경해야 할 때, 쿠키 업데이트하여 변경된 쿠키를 HTTP Header에 포함시켜 응답
    
    - Session
        - 쿠키를 기반, but 브라우저에 저장하는 쿠키와 달리 세션은 서버에서 관리
        - 서버에서는 클라이언트를 구분하기 위해 세션 ID 부여, 웹 브라우저가 서버에 접속시 종료할 때 까지 인증상태 유지
        - 사용자에 대한 정보를 서버에 두기 때문에 쿠키보다 보안에 좋지만, 사용자가 많아질수록 서버 메모리를 많이 차지
        - 동작방식
            1. 클라이언트가 서버에 접속 시 세션 ID 발급
            2. 클라이언트는 세션 ID에 대해 쿠키를 사용해서 저장
            3. 클라이언트는 서버에 요청 할 때, 이 쿠키의 세션 ID를 서버에 전달하여 사용
            4. 서버는 세션 ID를 받아서 세션에 있는 클라이언트 정보 가져옴
            5. 클라이언트에 응답
    
    - 차이점
        - 쿠키는 브라우저 저장, 세션은 서버
        - 쿠키는 보안에 취약, 세션은 쿠키를 이용해 세션 ID만으로 구분하기 때문에 good
        - 쿠키는 브라우저 종료해도 남을수 있음, 세션은 브라우저 종료되면 삭제됨
</details>

<details>
    <summary>DNS?</summary>
    
    - 도메인에 연결된 서버의 주소를 찾아주는 역할
        - IP는 사람이 이해하고 기억하기 어렵기 때문에 이를 위해서 각 ip에 부여한 이름이 도메인
        ex> 주소창에 도메인(google.com) 입력 -> 도메인에 연결된 네임서버(DNS)에 서버 IP 요청
    
    - NSlookup 
        - DNS 서버로 부터 여러가지 정보를 얻을 수 있는 명령어
        - 한번 가져온 주소는 DNS Server에 저장하고, 호스트 요청시 그 안에서 request
</details>

<details>
    <summary> RESTful </summary>
    
    - REST API : URI로 Resource를 명시하고, HTTP Method를 통해 해당 Resource에 대한 CRUD를 적용하는 것
        - 클라이언트가 직접 데이터베이스에 접속해서 Resource를 변경하는 것은 매위 위험하기 때문에 REST API 사용
        - 장점 : HTTP 인프라를 그대로 사용하므로 REST API위한 별도 인프라 구축 X / HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능
        - 단점 : 표준이 없음 / HTTP Method 형태가 제한적

    
    
    - RESTful : REST API를 활용하여 개발되는 서비스
    
    | 메서드 | 역할                                                    |
    | :----: | :------------------------------------------------------ |
    |  GET   | 데이터를 조회한다.                                      |
    |  POST  | 데이터를 등록한다. 인증 작업을 거칠 때 사용하기도 한다. |
    | DELETE | 데이터를 삭제한다.                                      |
    |  PUT   | 데이터를 새 정보로 통째로 업데이트할 때 사용한다.       |
    | PATCH  | 데이터의 특정 필드를 수정할 때 사용한다.                |
   
</details>

<details>
    <summary>CORS</summary>
    
    - 교차 출처 리소스 공유(Cross-Origin Resource Sharing, CORS)
        - 출처가 서로 다른 도메인간에 자원을 공유하는 것 / 대부분의 브라우저에서는 이를 기본적으로 차단하며, 서버측에서 헤더를 통해서 사용가능한 자원을 알려줌 
        - 출처(Origin) = Protocal + Host + Port ( ex) 'https://github.com' location.origin 명령어로 출처 확인)
    
        - Preflight request : 서버에 예비 요청을 보내서 안전한지 판단한 후 본 요청을 보내는 방법, . OPTIONS 메서드로 요청하며 CORS를 허용하는지 확인 후 CORS가 허용된 웹서버라면 사용 가능한 리소스를 헤더에 담아 응답
    
</details>







