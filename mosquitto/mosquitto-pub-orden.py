import random
import time
import json 

from paho.mqtt import client as mqtt_client


broker = '127.0.0.1'
port = 1883
topic = "compras/orden"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = {
            'id': msg_count,
            'user_email': 'neider.smith1@gmail.com',
            'product': 'Televisor 55',
            'quantity': 1
        }
        result = client.publish(topic, json.dumps(msg))
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
"""

    """
if __name__ == '__main__':
    run()