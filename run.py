#!/usr/bin/env python3

import requests
import os
import json

path = os.getcwd() + '/supplier-data/descriptions/'
url = 'http://34.122.195.213/fruits/'

for f in os.listdir(path):
  print('fazendo o upload de '+f)
  n, e = os.path.splitext(f)
  with open(os.path.join(path,f),  'r') as content:
    list = [x.strip() for x in content]
    dict = {"name": list[0], "weight": int(list[1][:-3]), "description": list[2], "image_name": n+'.jpeg'}
    response = requests.post(url, json = dict, verify = False)
    print(response)

