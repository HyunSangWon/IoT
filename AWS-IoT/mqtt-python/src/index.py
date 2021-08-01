from mqtt.mqtt_init import mqtt_init,mqtt_subscribe

mqtt_connection = mqtt_init()
message = {'temperature': 50, 'humidity' : 80, 'barometer' : 1013, 'wind': {'velocity' : 22, 'bearing' :255}}
mqtt_subscribe(mqtt_connection,message)