# * ------
# * File: /client.py
# * File Created: Friday, 22nd November 2019 6:07:29 pm
# * Author: Alex Chomiak
# *
# * Last Modified: Friday, 22nd November 2019 7:05:14 pm
# * Modified By: Tyler Lyczak
# *
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

print("Connecting client...")
print("Port:",port)
print("IP:", ip)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip,int(port)))
connected = True


class Listener(threading.Thread):
  def __init__(self):
    super(Listener,self).__init__()
  def run(self):
    global playerX
    while(True):
      data = client_socket.recv(1024)
      playerX = int(data)
      print("Current player X Coordinate", int(data))
      if not data:
        break
    connected = False

listener = Listener()
listener.start()

playerX = -1

def send_increment(val): # * Use this function to send increment to game
  if not connected: return
  client_socket.sendall(str(val).encode())


# * Implement GPIO code here *******

# ** Dummy Code **
increment = 10
while(connected):
  buttonStateRight = GPIO.input(rightButton)
  buttonStateLeft = GPIO.input(leftButton)

  if buttonStateRight == False:
      send_increment(increment)

  if buttonStateLeft == False:
      send_increment((-1)*increment)
  time.sleep(.05)
