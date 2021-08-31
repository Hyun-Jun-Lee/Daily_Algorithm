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


    

