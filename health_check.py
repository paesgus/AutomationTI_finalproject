#!/usr/bin/env python3

import shutil
import psutil
import socket
import report_email
import time
import os

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
  #print(socket.gethostbyname('localhost'))
  if socket.gethostbyname('localhost') == '127.0.0.1':
    return True
  else:
    return False


def alert(error):
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = error
  body = "Please check your system and resolve the issue as soon as possible."
  message = report_email.generate(sender, receiver, subject, body, '')
  report_email.send(message)


def main():

  while True:
    if not check_disk_usage('/'):
      alert('Error - Available disk space is less than 20%')
    if not check_cpu_usage():
      alert('Error - CPU usage is over 80%')
    if not check_memory():
      alert('Error - Available memory is less than 500MB')
    if not check_localhost():
      alert('Error - localhost cannot be resolved to 127.0.0.1')

    time.sleep(60)


if __name__ == "__main__":
  main()


