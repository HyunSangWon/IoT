### AWS IoT Core

-   AWS IoT Core는 서버를 프로비저닝하거나 관리할 필요 없이 IoT 디바이스를 AWS 클라우드에 연결할 수 있게 해 줌.

### AWS IoT Core 특징

-   최고 최대 128KB(킬로바이트) 크기의 메시지를 송신 및 수신할 수 있음.

### AWS IoT Core Topic

-   publishing Client와 Subscribing Client간의 메세지를 주고받는 메시지 통로
-   토픽 필터
    필터 # (하위 토픽 구독)
    ex) sensor/#  
     sensor/temp  
     sensor/temp/room1  
    필터 + (연관된 토픽 구독)
    ex) sensor/+/room1  
     sensor/temp/room1  
     sensor/moisture/room1

### AWS IoT Core 규칙

-   규칙?
    IoT Core에서 Lambda,DynamoDB 등 AWS 서비스를 연결할 수 있는데 이를 규칙이라 함.
    규칙에는 쿼리문이 존재하여 쿼리문으로 1차 필터링을 하고 람다에서 2차 필터링을 하면 된다.

-   규칙 쿼리 문법 (흔히 쓰는 DB SQL문하고 같음)
    '''
    SELECT <Attribute> FROM <Topic Filter> WHERE <Condition>
    '''
-   규칙 쿼리 문법 예시 (온도가 30도 이상인 데이터만 수신)
    '''
    SELECT
    CAST(topic(2) AS DECIMAL) AS device_id,
    temperature AS reported_temperature,
    30 AS max_temperature
    FROM 'device/+/data' WHERE temperature > 30
    '''
    topic(number) 함수는 from절에서 정의한 토픽 필터 인덱스 값 호출  
    ex) device/50/data 이라는 토픽이 있다면 topic(1)은 data가 나옴.

### AWS IoT Core 요금

-   최소 요금, 의무 서비스 사용량 없음.
-   연결 시간과 메시징 으로 요금을 부과.
-   연결 요금
    0.096 USD(연결 100만 분당)  
     ex) 연중무휴 24시간 연결 시 1년에 디바이스당 0.050 USD를 지불.(연결 1개 _ 0.096 USD/연결 1,000,000분 _ 525,600분/년)

-   메세징
    메시지 100만 개당 1.20 USD  
    메시지가 40억 개를 넘으면 100만 개당 0.96  
    메시지 50억 개 초과 100만 개당 0.84  
    메시지는 5KB 단위로 측정 ex) 8KB 메시지는 메시지 2개로 측정
