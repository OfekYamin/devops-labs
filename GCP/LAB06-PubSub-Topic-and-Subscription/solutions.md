# LAB06 - Pub/Sub Topic and Subscription - Solutions

This document provides solutions to the TODOs in the `pubsub_script.py` script.

## Solution: Initialize the publisher client and create the topic path

```python
# Initialize the publisher client
publisher = pubsub_v1.PublisherClient()

# Create the topic path using project_id and topic_id
topic_path = publisher.topic_path(project_id, topic_id)

# Create the topic and print confirmation message
topic = publisher.create_topic(request={"name": topic_path})
print(f"Topic created: {topic_path}")
```

## Solution: Initialize the subscriber client and create the subscription

```python
# Initialize the subscriber client
subscriber = pubsub_v1.SubscriberClient()

# Create the subscription path
subscription_path = subscriber.subscription_path(project_id, subscription_id)

# Create the subscription that listens to the topic
# and print confirmation message
subscription = subscriber.create_subscription(
    request={"name": subscription_path, "topic": topic_path}
)
print(f"Subscription created: {subscription_path}")
```

## Solution: Publish messages to a topic

```python
# Initialize the publisher client
publisher = pubsub_v1.PublisherClient()

# Get the topic path
topic_path = publisher.topic_path(project_id, topic_id)

# Publish each message in the list
for message in messages:
    # Encode the message as bytes
    message_data = message.encode("utf-8")
    
    # Publish the message and get the message ID
    future = publisher.publish(topic_path, data=message_data)
    message_id = future.result()
    print(f"Published message ID: {message_id}")
```

## Solution: Pull and acknowledge messages

```python
# Initialize the subscriber client
subscriber = pubsub_v1.SubscriberClient()

# Get the subscription path
subscription_path = subscriber.subscription_path(project_id, subscription_id)

# Pull messages from the subscription
response = subscriber.pull(
    request={"subscription": subscription_path, "max_messages": max_messages}
)

# Process each received message
received_messages = response.received_messages
ack_ids = []

for received_message in received_messages:
    message = received_message.message
    message_data = message.data.decode("utf-8")
    print(f"Received message: {message_data}")
    
    # Add any message attributes
    if message.attributes:
        print("Attributes:")
        for key, value in message.attributes.items():
            print(f"  {key}: {value}")
    
    # Collect the ack ID for acknowledgement
    ack_ids.append(received_message.ack_id)

# Acknowledge the received messages
if ack_ids:
    subscriber.acknowledge(
        request={"subscription": subscription_path, "ack_ids": ack_ids}
    )
    print(f"Acknowledged {len(ack_ids)} messages")
```

## Solution: Delete topic and subscription

```python
# Initialize the clients
publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

# Get the paths
topic_path = publisher.topic_path(project_id, topic_id)
subscription_path = subscriber.subscription_path(project_id, subscription_id)

# Delete the subscription first, then the topic
subscriber.delete_subscription(request={"subscription": subscription_path})
print(f"Subscription deleted: {subscription_path}")

publisher.delete_topic(request={"topic": topic_path})
print(f"Topic deleted: {topic_path}")
```

## Running the Complete Solution

1. Set your GCP credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Run the script with basic parameters:
```bash
python pubsub_script.py --project_id=your-gcp-project-id
```

3. Run with custom topic and subscription names:
```bash
python pubsub_script.py --project_id=your-gcp-project-id --topic=custom-topic --subscription=custom-sub
```

4. Run with custom messages:
```bash
python pubsub_script.py --project_id=your-gcp-project-id --message="Hello World" --message="Another message"
```

5. Run with cleanup to delete resources after execution:
```bash
python pubsub_script.py --project_id=your-gcp-project-id --cleanup
```

## Notes

When working with Pub/Sub in production environments:

1. Consider using push subscriptions for real-time event handling
2. Implement proper error handling and retries
3. Use message attributes for metadata
4. Consider ordering keys for message sequencing when needed
5. Set appropriate message retention periods

For more information, refer to the [Google Cloud Pub/Sub documentation](https://cloud.google.com/pubsub/docs/overview). 