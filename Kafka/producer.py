import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from pykafka import KafkaClient

from pykafka import KafkaClient

file='weatherAUS.csv'
archivo=pd.read_csv(file)
print("----------------------------")
print(archivo)
print("----------------------------")
saved_column = archivo.MinTemp
client = KafkaClient(hosts="127.0.0.1:9092")

print(client.topics)
topic = client.topics['Hello-Kafka']

with topic.get_sync_producer() as producer:
    for i in range(0,len(saved_column)):
        producer.produce(str(saved_column[i]))

