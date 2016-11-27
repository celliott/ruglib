#!/usr/bin/python

import json, os
from ruglib import RugSub

module_name = "worker_{}".format(os.getenv('MODULE'))
module = __import__(module_name)

print("{} loaded!".format(module_name))

topic = os.getenv('TOPIC', 'main')
zmq_address = "tcp://{zmq_host}:{zmq_port}".format(
  zmq_host=os.getenv('ZMQ_HOST', '172.17.0.1'),
  zmq_port=os.getenv('ZMQ_PORT', 5570))

rugsub = RugSub(address=zmq_address)

def _get_data(topic):
  try:
    msg = rugsub.subscribe(topic=topic)
    data = msg.split(' ', 1)[1]
    return json.loads(data)
  except:
    return {} 

if __name__ == "__main__":
  while True:
    try:
      payload = _get_data(topic)
      eval("module.{method}({data})".format(
        method=payload.keys()[0],
        data=payload.values()[0]))
    except:
      continue
