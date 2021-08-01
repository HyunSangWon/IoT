### Topic 디자인

-   상위 Namespace 및 그룹 정보의 반영
    -   어플리케이션 정보, 그룹 정보
-   커뮤니케이션에 대한 주요 정보 반영
    -   thingName, uuid 정보
-   데이터 토픽과 커멘드 토픽의 분리

#### 데이터 토픽

-   구조 : dt/<namespace>/<group-id>/<thing-name>/<data-type>

#### 커멘드 토픽

-   구조 : cmd/<namespace>/<group-id>/<thing-name>/req-type
