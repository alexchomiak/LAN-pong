# * ------ 
# * File: /client.py
# * File Created: Sunday, 24th November 2019 1:01:32 am
# * Author: Alex Chomiak 
# * 
# * Last Modified: Sunday, 24th November 2019 2:39:15 am
# * Modified By: Alex Chomiak 
# * 
# * Author Github: https://github.com/alexchomiak
# * ------ 
# * ------
# * File: /client.py
# * Author Github: https://github.com/alexchomiak
# * ------

import sys
import socket
import threading
import time
import RPi.GPIO as GPIO

port = sys.argv[1]
ip = sys.argv[2] if (len(sys.argv) > 2) else '127.0.0.1'

GPIO.setmode(GPIO.BOARD)

leftButton = 7
rightButton = 11

GPIO.setup(rightButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(leftButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

connected = False
client_socket = {}

class Listener(threading.Thread):
  def __init__(self):
    super(Listener,self).__init__()
  def run(self):
    global playerX
    global connected
    while(True):
      try:
        data = client_socket.recv(1024)
        playerX = int(data)
        print("Current player X Coordinate", int(data))
        if not data:
          break
      except:
        connected = False
        print("Closing Connection")
        client_socket.close()
        break




playerX = -1

def send_increment(val): # * Use this function to send increment to game
  if not connected: return
  try:
    client_socket.sendall(str(val).encode())
  except:
    print("Send Error")


# * Implement GPIO code here *******

increment = 20
while(True):
  print("Connecting client...")
  print("Port:",port)
  print("IP:", ip)
  try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip,int(port)))
  except: 
    print("Connection Cannot Be Establisbed... Trying Again...")
    time.sleep(5)
  connected = True
  listener = Listener()
  listener.start()
  while(connected):
    send_increment(0)
    buttonStateRight = GPIO.input(rightButton)
    buttonStateLeft = GPIO.input(leftButton)
    if buttonStateRight == False:
      send_increment(increment)

    if buttonStateLeft == False:
      send_increment((-1)*increment)
      
    time.sleep(.05)
