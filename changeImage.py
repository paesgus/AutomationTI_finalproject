#!/usr/bin/env python3

from PIL import Image
import sys
import os

def convImages():
  path = os.getcwd() +'/supplier-data/images/'

  for f in os.listdir(path):
    try:
      im = Image.open(os.path.join(path,f)).convert('RGB')
      n, e = os.path.splitext(f)
      outfile = n + '.jpeg'
      new_im = im.resize((600,400))
      new_im.save(os.path.join(path,outfile) , 'JPEG')
    except:
      continue


convImages()
