import boto3
import json
from datetime import datetime
import calendar
import random
import time

my_stream_name = 'StreamData'

kinesis_client = boto3.client('kinesis', region_name='us-east-1')

def put_to_stream(iotValue, iotName):
    payload = {
                'iotValue': str(iotValue),
                'iotName' : str(iotName),
              }

    print(payload)

    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(payload),
                        PartitionKey=iotName)

while True:
    iotName = 'DemoSensor'
    iotValue = random.randint(80, 110)


    put_to_stream(iotValue, iotName)

    # wait for 5 second
    time.sleep(2)