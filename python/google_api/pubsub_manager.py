import os
from google.cloud import pubsub_v1

def callback(message):
    print(message.data)
    message.ack()

if __name__ == "__main__":
    project_id='capstone-1554124676827'
    topic_name='usv_data'

    publisher = pubsub_v1.PublisherClient()
    project_path = publisher.project_path(project_id)
    topic_path = publisher.topic_path(project_id, topic_name)

    for topic in publisher.list_topics(project_path):
        print(topic)

    subscription_name ='usv_data_subscriber'
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    future = subscriber.subscribe(subscription_path, callback)

    try:
        future.result()
    except KeyboardInterrupt:
        future.cancel()