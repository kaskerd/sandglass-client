import client
import sandglass_pb2 as pb

topic = pb.TopicConfig(name="futura", replicationFactor= 1, numPartitions= 6)
client = client.Client("localhost:7170")

part = client.create_topic(topic)

print(part)