#!/usr/bin/python

import json, os


def capitalize(data):
  _log(data['text'], data['text'].capitalize())

def upper(data):
  _log(data['text'], data['text'].upper())

def lower(data):
  _log(data['text'], data['text'].lower())
  
def title(data):
  _log(data['text'], data['text'].title())

def _log(original, text):
  print("[In] {text}".format(text=original))
  print("[Out] {text}".format(text=text)
