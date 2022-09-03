
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/gabrielkotaniZUP/kafka-with-python/tree/main/new-service/templates/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/gabrielkotaniZUP/kafka-with-python/tree/main/new-service/templates/README.pt-br.md)


# New-Service
Quickly setup a local environment to test Kafka. The service creates a `Kafka broker`, `Zookeper` and `Kafdrop` automatically, and can be accessed via a web browser.

## Services:
+ `Kafka` : Built on top of the *confluentinc/cp-kafka* image.
+ `Zookeeper` : Built on top of the *confluentinc/cp-zookeeper* image.
+ `Kafdrop` : Built on top of the *obsidiandynamics/kafdrop* image.

## Ports:
+ `Kafka`
    - External port: 9092
    - Internal port: 29092
+ `Zookeeper` : port: 2181
+ `Kafdrop` : port: 19000

## Quick-start:
### Start the services
```shell
docker compose up -d
```
### Check that the instances are running
```shell
docker compose ps
```
### Access the browser
Open the browser and access http://localhost:19000

### Start the listener

By default this will be listening to the topic: {{topic_name}}
```shell
python3 -u consumer.py 
```

### Send a message
Use producer.py to send your first message
```shell
python3 -u producer.py 
```
### Change the message

```python

if __name__ == '__main__':
    SERVER = 'localhost:9092'   # This is the Kafka server
    TOPIC = '{{topic_name}}'    # We need to specify the topic
    message = {'foo': 'bar'}    # Kafka accepts serializables or bytes

    main(SERVER, TOPIC, message)

```
