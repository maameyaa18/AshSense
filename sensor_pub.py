import paho.mqtt.client as paho
import time
import json
import Adafruit_DHT


sensor = Adafruit_DHT.DHT11
pin = 17




def on_connect(client,userdata,rc):
    print(rc)

def on_publish(client,userdata,mid):
    print(mid)


topic = 'se_sensors'    
client = paho.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.username_pw_set('tkdnvfhi', '1ooMI9KT_dZV')  
client.connect('m24.cloudmqtt.com', 13726)

client.loop_start()
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        my_json = {'temperature': temperature, 'humidity': humidity}
        (rc,mid) = client.publish(topic, json.dumps(my_json), qos=1, retain=True)
        time.sleep(3)

    else:
        print('Failed to get reading. Try again!')
        
        
