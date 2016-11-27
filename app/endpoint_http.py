#!/usr/bin/python

import endpoint, json, os, flask
from flask import Flask, request

app = Flask(__name__)

@app.route("/<topic>/<method>", methods=['POST', 'GET'])
def topic(topic, method):
  if request.method == "POST":  
    payload = {
      str(method): str(request.get_json())}
    results = endpoint.publish(topic, payload)
  return flask.jsonify(**results)

if __name__ == "__main__":
  app.run(host='0.0.0.0')
