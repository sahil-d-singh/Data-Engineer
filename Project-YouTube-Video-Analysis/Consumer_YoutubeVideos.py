from kafka import KafkaConsumer
import json
from json import loads


if __name__ == "__main__":
    consumer = KafkaConsumer(
        "USvideos_clean_data1",
        bootstrap_servers='192.168.81.131:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a",
    )
    print("starting the consumer")

    for msg in consumer:
        print("Video_Data = {}".format(json.loads(msg.value)))