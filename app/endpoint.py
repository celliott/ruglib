#!/usr/bin/python

import json, os
from ruglib import RugPub

zmq_address = "tcp://{zmq_host}:{zmq_port}".format(
  zmq_host=os.getenv('ZMQ_HOST', '*'),
  zmq_port=os.getenv('ZMQ_PORT', 5570))

rugpub = RugPub(address=zmq_address)

def publish(topic, payload):
  try:
    message = "{topic} {payload}".format(
      topic=topic,
      payload=json.dumps(payload))
    rugpub.publish(message)
    return {"status": "ok"}
  except:
    return {"status": "error"}
