from awscrt import io, mqtt
from awsiot import mqtt_connection_builder
from mqtt.topics.device_topic import *
import time as t
import json

ENDPOINT = "a3k7c4p9l0tvfc-ats.iot.ap-northeast-2.amazonaws.com"
CLIENT_ID = "SangwonClientID"
PATH_TO_CERT = "../key/d02945ed1b-certificate.pem.crt"
PATH_TO_KEY = "../key/d02945ed1b-private.pem.key"
PATH_TO_ROOT = "../key/root-ca.pem"

def mqtt_init():
    # Spin up resources
    event_loop_group = io.EventLoopGroup(1) # An event-loop is a thread for doing async work.
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver) # Handles creation and setup of client socket connections.
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=ENDPOINT,
            cert_filepath=PATH_TO_CERT,
            pri_key_filepath=PATH_TO_KEY,
            client_bootstrap=client_bootstrap,
            ca_filepath=PATH_TO_ROOT,
            client_id=CLIENT_ID,
            clean_session=False, # True이면 서버는 다시 연결할 때마다 세션 동안 만든 모든 구독을 지움.
            keep_alive_secs=6 # CONNECT 패킷을 보낼 활성 값(초)입니다.
            )
    # Make the connect() call
    connect_future = mqtt_connection.connect()
    # Future.result() waits until a result is available
    connect_future.result()
    print("Connected!")
    return mqtt_connection

# Publish message to server desired number of times.
def mqtt_subscribe(mqtt_connection,message):
    RANGE = 3
    MESSAGE = message

    for i in range (RANGE):
        mqtt_connection.publish(topic=TEMPERATURE_TOPIC, payload=json.dumps(MESSAGE), qos=mqtt.QoS.AT_LEAST_ONCE)
        print("Published: '" + json.dumps(MESSAGE))
        t.sleep(0.1)

    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()