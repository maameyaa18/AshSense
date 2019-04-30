#Software Engineering Final Project
#Maame Yaa Osei, Maame Efua Boham, Molife Chaplain and Ariel Woode
#Raspbery Pi Sensor Reading

#Importing relevant libraries

import paho.mqtt.client as paho     #Paho MQTT Client to publish sensor data.
import time                         # Time to introduce lag.
import json                         # Json to convert sensor reading to json object.
import Adafruit_DHT                 # Adafruit DHT library to retrieve sensor information.


sensor = Adafruit_DHT.DHT11         #Initializing sensor type
pin = 17                            #Initializing GPIO pin number



'''
The functions below are executed on connection to Cloud MQTT
and publishing a message successfully.
'''
def on_connect(client,userdata,rc):
    print(rc)

def on_publish(client,userdata,mid):
    print(mid)

'''
Initializing MQTT variables and connections.
'''
topic = 'se_sensors'    
client = paho.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.username_pw_set('tkdnvfhi', '1ooMI9KT_dZV')  
client.connect('m24.cloudmqtt.com', 13726)
client.loop_start()

'''
LOop to read information from sensor and oublish to Cloud MQQT broker
as a json with a lag of 3 seconds.
'''
while True:
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        my_json = {'temperature': temperature, 'humidity': humidity}
        (rc,mid) = client.publish(topic, json.dumps(my_json), qos=1, retain=True)
        time.sleep(3)
    else:
        print('Failed to get reading. Try again!')
        
        
