#!/usr/bin/env python3

import requests
import os

url = 'http://localhost/upload/'
path = os.getcwd() + '/supplier-data/images/'

only_jpeg = []

for file in os.listdir(path):
  name, ext = os.path.splitext(file)
  if ext == '.jpeg':
    only_jpeg.append(os.path.join(path,file))

for jpeg in only_jpeg:
  with open(jpeg, 'rb') as opened:
    r = requests.post(url, files={'file': opened})


