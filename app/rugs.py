#!/usr/bin/python

import zmq, json, os

class RugPub:
  def __init__(self, address):
    context = zmq.Context()
    self.socket = context.socket(zmq.PUB)
    self.socket.bind(address)
    print("[Info] Bound to 0MQ: {address}".format(address=address))
        
  def publish(self, msg):
    try:
      self.socket.send(msg)
      print("[Info] Message sent: {msg}".format(msg=msg))
    except:
      print("[Error] Message not sent.")

class RugSub:
  def __init__(self, address):
    context = zmq.Context()
    self.socket = context.socket(zmq.SUB)
    self.socket.connect(address)
    print("[Info] Connected to: {address}".format(address=address))
      
  def subscribe(self, topic):
    self.socket.setsockopt(zmq.SUBSCRIBE, topic)
    print("[Info] Subscribed to topic: {topic}".format(topic=topic))
    try:
      return self.socket.recv()
      self.socket.close()
    except:
      self.socket.close()
      return {} 