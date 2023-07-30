class Consumer:
    def __init__(self, consumer_id):
        self.consumer_id = consumer_id
        self.subscribed_topics = []

    def subscribe_topic(self, topic_name):
        self.subscribed_topics.append(topic_name)

    def consume_message(self, topic_name, message):
        if topic_name in self.subscribed_topics:
            print(f"Consumer {self.consumer_id} received '{message}' from topic '{topic_name}'")

