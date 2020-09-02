#!/usr/bin/env python3

import eg
import shutil
import psutil
import socket

def check_disk_usage(disk):
  disk_usage = shutil.disk_usage(disk)
  free = (disk_usage.free / disk_usage.total) * 100
  return free > 20

def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  return usage < 80

def check_memory():
  memory = psutil.virtual_memory()[1] / 10**6
  return memory > 500

def check_localhost():
  print(socket.gethostbyname(socket.gethostname()))
  if socket.gethostbyname(socket.gethostname()) == '127.0.0.1':
    return True
  else:
    return False

if not check_disk_usage('/') or not check_cpu_usage() or not check_memory() or not check_localhost():
  print("shit")
else:
  print('ok')


