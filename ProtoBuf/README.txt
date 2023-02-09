ProtoBuf ?
프로토 버퍼는 구글에서 개발하고 오픈소스로 공개한, 직렬화 데이타 구조(Serialized Data Structure).
다양한 언어(Java, Python, Go...)를 지원하며 특히 직렬화 속도가 빠르고 직렬화된 파일의 크기도 작아서 Apache Avro 파일 포맷과 함께 많이 사용됨.

ProtoBuf 특징
1. 프로토콜 버퍼는 하나의 파일에 최대 64M까지 지원
2. JSON 파일을 프로토콜 버퍼 파일 포맷으로 전환이 가능하고, 반대로 프로토콜 버퍼 파일도 JSON으로 전환이 가능

마치며
클라이언트(모바일)에서 서버로 HTTP/JSON 과 같은 REST API를 구현할 때, 
전송 전 JSON을 프로토콜 버퍼 포맷으로 직렬화해서, 전체적인 패킷 양을 줄여서 전송하고, 서버에서는 받은 후에, 다시 JSON으로 풀어서 사용하는 구조를 취할 수 있다. 사실 이게 바로 gRPC(google Remote Procedure Calls) 구조이다.
API 게이트웨이를 백앤드 서버 전면에 배치해놓고, 프로토콜 버퍼로 들어온 메세지 바디를 JSON으로 변환해서 백앤드 API 서버에 넘겨주는 식의 구현이 가능하다.

참고 문헌
- https://developers.google.com/protocol-buffers/docs/proto (데이터 구조)
- https://bcho.tistory.com/1182 (조대협 기술블로그)