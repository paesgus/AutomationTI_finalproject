#!/usr/bin/env python3

import requests
import os
import json

path = '/home/student-00-ceab51a4388c/supplier-data/descriptions/'

for f in os.listdir(path):
  print('fazendo o upload de '+f)
  n, e = os.path.splitext(f)
  with open(os.path.join(path,f),  'r') as content:
    list = [x.strip() for x in content]
    dict = {"name": list[0], "weight": int(list[1][:-3]), "description": list[2], "image_name": n+'.jpeg'}
    response = requests.post('http://34.123.99.244/fruits/', json = dict, verify = False)
    print(response)

