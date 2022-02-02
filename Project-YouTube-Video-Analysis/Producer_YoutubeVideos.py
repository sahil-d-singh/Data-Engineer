from kafka import KafkaProducer
import json
import time
import pandas as pd
import numpy as np
from json import dumps

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.bool_):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

KAFKA_TOPIC_NAME_CONS = "USvideos_clean_data1"

Transaction_Data=pd.read_csv("USvideos_clean.csv")

def json_serializer(data):
    return json.dumps(data,cls=NpEncoder).encode("utf-8")

if __name__ == "__main__":
    print("Kafka Producer Application Started ... ")

    producer = KafkaProducer(bootstrap_servers=['192.168.81.131:9092'],
                             value_serializer=json_serializer)

    message = None

    if 1==1:
        for i in range(80000):
            message={}
            message["video_id"] = Transaction_Data['video_id'][i]
            message["trending_date"] = Transaction_Data['trending_date'][i]
            message["title"] = Transaction_Data['title'][i]
            message["channel_title"] = Transaction_Data['channel_title'][i]
            message["category_id"] = Transaction_Data['category_id'][i]
            message["publish_time"] = Transaction_Data['publish_time'][i]
            message["tags"] = Transaction_Data['tags'][i]
            message["views"] = Transaction_Data['views'][i]
            message["likes"] = Transaction_Data['likes'][i]
            message["dislikes"] = Transaction_Data['dislikes'][i]
            message["comment_count"] = Transaction_Data['comment_count'][i]
            message["thumbnail_link"] = Transaction_Data['thumbnail_link'][i]
            message["comments_disabled"] = Transaction_Data['comments_disabled'][i]
            message["ratings_disabled"] = Transaction_Data['ratings_disabled'][i]
            message["video_error_or_removed"] = Transaction_Data['video_error_or_removed'][i]
            message["description"] = Transaction_Data['description'][i]


            print("Message to be sent: ", message)
            time.sleep(5)
            producer.send(KAFKA_TOPIC_NAME_CONS, message)
            time.sleep(1)
    else:
        print("END")

