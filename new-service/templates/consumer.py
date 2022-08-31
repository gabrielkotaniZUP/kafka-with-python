from kafka import KafkaConsumer
import logging
import time


def run(topic):

    logging.info(f"Attempting to listen to {topic}")
    consumer = KafkaConsumer(topic)

    logging.info(f"Listening to  {topic}")
    for msg in consumer:
        logging.info(msg)

if __name__=='__main__':
    topic = '{{topic_name}}'
    logging.info("Running Consumer")

    run(topic)