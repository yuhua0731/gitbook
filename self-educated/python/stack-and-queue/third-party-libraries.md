---
description: integrate with standalone message queue brokers
---

# Third-party libraries

## RabbitMQ: `pika` <a href="#rabbitmq-pika" id="rabbitmq-pika"></a>

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 rabbitmq
```

## Redis: `redis` <a href="#redis-redis" id="redis-redis"></a>

```bash
docker run -it --rm --name redis -p 6379:6379 redis
docker exec -it redis redis-cli
# 127.0.0.1:6379>
```

## Apache Kafka: `kafka-python3` <a href="#apache-kafka-kafka-python3" id="apache-kafka-kafka-python3"></a>

### `Configuration file`

```yaml
# docker-compose.yml

version: "3"
services:
  zookeeper:
    image: 'bitnami/zookeeper:latest'
    ports:
      - '2181:2181'
    environment:
      - ALLOW_ANONYMOUS_LOGIN=yes
  kafka:
    image: 'bitnami/kafka:latest'
    ports:
      - '9092:9092'
    environment:
      - KAFKA_BROKER_ID=1
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://127.0.0.1:9092
      - KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181
      - ALLOW_PLAINTEXT_LISTENER=yes
    depends_on:
      - zookeeper
```

```sh
docker-compose up
```

