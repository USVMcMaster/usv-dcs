import os
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id='capstone-1554124676827',
    topic='usv_data')

subscriber = pubsub_v1.SubscriberClient()
subscription_name = 'projects/{project_id}/topics/{sub}'.format(
    project_id='capstone-1554124676827',
    sub='usv_data_subscriber')

subscriber.create_subscription(name=subscription_name, topic=topic_name)

def callback(message):
    print(message.data)
    message.ack()

future = subscriber.subscribe(subscription_name, callback)

try:
    future.result()
except KeyboardInterrupt:
    future.cancel()