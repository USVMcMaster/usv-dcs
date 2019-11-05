import os
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id='capstone-1554124676827',
    topic='usv_data')

# Topic already created
# publisher.create_topic(topic_name)
publisher.publish(topic_name, b'Published message 2')