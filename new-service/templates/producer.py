from kafka import KafkaProducer
import json

def main(server, topic, message):

    serializer = None
    if isinstance(message, dict) :serializer=lambda v: json.dumps(v).encode('utf-8')

    producer = KafkaProducer(
        bootstrap_servers=server,
        value_serializer=serializer
    )
    
    producer.send(topic, message)


if __name__ == '__main__':
    SERVER = 'localhost:9092'
    TOPIC = '{{topic_name}}'
    message = {'foo': 'bar'}

    main(SERVER, TOPIC, message)