import grpc

import sandglass_pb2_grpc as sg_grpc
import sandglass_pb2 as sg_pb

class Client(object):
  
  def __init__(self, address):
    self._channel = grpc.insecure_channel(address)
    self.client = sg_grpc.BrokerServiceStub(self._channel)

  def create_topic(self, params):
    return self.client.CreateTopic(params)

  def list_partitions(self, topic):
    return self.client.GetTopic(
      sg_pb.GetTopicParams(name = topic))

  def produce_message(self, topic, partition, msg):
    return self.client.Produce(sg_pb.ProduceMessageRequest(
        topic = topic, 
        partition = partition, 
        messages = msg))

  def new_consumer(self, topic, partition, group, name):
    return Consumer(self.client, topic, partition, group, name)

  def close(self):
    return self._channel.close()


class Consumer(object):

  def __init__(self, client, topic, partition, group, name):
    self._client = client
    self._topic = topic
    self._partition = partition
    self._group = group
    self._name = name

  def consume(self):
	  return self._client.client.ConsumeFromGroup(
      sg_pb.ConsumeFromGroupRequest(
        topic = self._topic,
        partition = self._partition,
        consumerGroupName = self._group,
        consumerName = self._name))

  def acknowledge(self, msgs):
	  return self._client.client.Acknowledge(
      sg_pb.MarkRequest(
        topic = self._topic,
        partition = self._partition,
        consumerGroup = self._group,
        consumerName = self._name,
        offsets = msgs.offsets))  

  def not_acknowledge(self, msgs):
	  return self._client.client.NotAcknowledge(
      sg_pb.MarkRequest(
        topic = self._topic,
        partition = self._partition,
        consumerGroupName = self._group,
        consumerName = self._name,
        offsets = msgs.offsets))
