### BLE (Bluetooth Low Energy)?

-   Bluetooth 4.0 부터 도입됨.
-   BLE system은 저전력으로 한번에 극히 작은 데이터를 전송.
-   기존 bluetooth classic과 비슷한 무선 통신을 할 수 있으면서, 기존의 문제이던 전력 소모량 줄임.
-   블루투스 두 기간의 단거리 네트워크 피코넷

#### 동작 방식에 의한 구분

-   Advertise(=Broadcast) Mode
    단방향 데이터 전송.
    일 대 다 방식.
    작은양의 data를 보낼 때.
    Signal을 일방적으로 계속 보냄.

    -   Advertiser(=broadcaster) : signal을 보내는 기기
    -   Observer : advertiser가 보내는 packet을 듣기 위해 주기적으로 scanning 하는 기기

-   Connection Mode
    양방향 데이터 전송.
    일 대 일 방식.
    Advertising으로만 데이터를 주고 받기에는 data양이 많은 경우.
    디바이스간 Channel hopping 규칙을 정해놓고 통신을 하기 떄문에 Advertise Mode보다 보안성 높음

    -   Central : Connection Advertising Signal을 주기적으로 Scan하다가, 적절한 디바이스에 연결을 요청
    -   Peripheral : Connection을 맺고 나면 Central 디바이스가 지정한 timing에 맞추어 channel을 같이 hopping 하며 주기적으로 데이터를 교환

### BLE 프로토콜 스택

#### GATT (Generic Attribute Profile)

-   GATT는 오직 데이터의 포맷 및 전달에 대해서만 처리한다.
-   데이터를 교환하기 위해서는 UUID가 필요하다.

#### GAP (Generic Access Profile)

-   GAP 역할은 크게 Broadcaster, Observer, Peripheral, Central로 나뉨.
