import grpc

from .client import Client

import sandglass_pb2_grpc as sg_grpc
import sandglass_pb2 as sg_pb

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