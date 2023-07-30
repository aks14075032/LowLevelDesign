class Producer:
    def __init__(self, producer_id, queue):
        self.producer_id = producer_id
        self.subscribed_topics = []
        self.queue = queue

    def publish_message(self, topic_name, message):
        self.queue.publish(topic_name, message)

    def subscribe_topic(self, topic_name):
        self.subscribed_topics.append(topic_name)
        self.queue.subscribe(topic_name, self)
