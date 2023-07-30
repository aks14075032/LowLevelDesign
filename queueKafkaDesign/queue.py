from queueKafkaDesign.topic import Topic


class Queue:
    def __init__(self):
        self.topics = {}

    def create_topic(self, topic_name):
        if topic_name not in self.topics:
            self.topics[topic_name] = Topic(topic_name)

    def get_topic(self, topic_name):
        return self.topics.get(topic_name)

    def publish(self, topic_name, message):
        topic = self.topics.get(topic_name)
        if topic:
            topic.add_message(message)

    def subscribe(self, topic_name, consumer):
        topic = self.get_topic(topic_name)
        if topic:
            topic.messages.reverse()
            for message in topic.messages:
                consumer.consume_message(topic_name, message)

    def consume(self, consumer, topic_name):
        consumer.subscribe_topic(topic_name)
