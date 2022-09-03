
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/gabrielkotaniZUP/kafka-with-python/tree/main/new-service/templates/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/gabrielkotaniZUP/kafka-with-python/tree/main/new-service/templates/README.pt-br.md)


# New-Service
Crie rapidamente um ambiente local para testar o Kafka. O serviço cria o `Kafka broker`, `Zookeper` e `Kafdrop` automaticamente, sendo acess;ivel via o browser.

## Serviços:
+ `Kafka` : Construído em cima da imagem *confluentinc/cp-kafka*.
+ `Zookeeper` : Construído em cima da imagem *confluentinc/cp-zookeeper*.
+ `Kafdrop` : Construído em cima da imagem*obsidiandynamics/kafdrop*.

## Portas:
+ `Kafka`
    - Porta externa: 9092
    - Porta interna: 29092
+ `Zookeeper` : porta: 2181
+ `Kafdrop` : porta: 19000

## Quick-start:
### Inicie os serviços
```shell
docker compose up -d
```
### Confirme que as instâncias estão rodando
```shell
docker compose ps
```
### Accesse a pagina via browser
Abra um browser e acesse http://localhost:19000

### Inicie o listener

Por padrão estaremos escutando o tópico: {{topic_name}}
```shell
python3 -u consumer.py 
```

### Envie uma mensagem
Use o producer.py para enviar sua primeira mensagem
```shell
python3 -u producer.py 
```
### Mude a mensagem

```python

if __name__ == '__main__':
    SERVER = 'localhost:9092'   # Esse é o servidor do Kafka
    TOPIC = '{{topic_name}}'    # Precisamos especificar o tópico
    message = {'foo': 'bar'}    # Kafka aceita serializables ou bytes

    main(SERVER, TOPIC, message)

```
