from queueKafkaDesign.queue import Queue
from queueKafkaDesign.consumer import Consumer
from queueKafkaDesign.producer import Producer

queue = Queue()

# Create topics
queue.create_topic("topic1")
queue.create_topic("topic2")

# Create producers and consumers
producer1 = Producer("producer1", queue)
producer2 = Producer("producer2", queue)
consumer1 = Consumer("consumer1")
consumer2 = Consumer("consumer2")
consumer3 = Consumer("consumer3")
consumer4 = Consumer("consumer4")
consumer5 = Consumer("consumer5")

# Subscriptions
producer1.subscribe_topic("topic1")
producer2.subscribe_topic("topic1")
consumer1.subscribe_topic("topic1")
consumer2.subscribe_topic("topic1")
consumer3.subscribe_topic("topic1")
consumer4.subscribe_topic("topic1")
consumer1.subscribe_topic("topic2")
consumer3.subscribe_topic("topic2")
consumer4.subscribe_topic("topic2")

# Publish messages
producer1.publish_message("topic1", "Message 1")
producer1.publish_message("topic1", "Message 2")
producer2.publish_message("topic1", "Message 3")
producer1.publish_message("topic2", "Message 4")
producer2.publish_message("topic2", "Message 5")

# Subscribe consumers to topics and consume messages
queue.subscribe("topic1", consumer1)
queue.subscribe("topic1", consumer2)
queue.subscribe("topic1", consumer3)
queue.subscribe("topic1", consumer4)
queue.subscribe("topic1", consumer5)
queue.subscribe("topic2", consumer1)
queue.subscribe("topic2", consumer3)
queue.subscribe("topic2", consumer4)