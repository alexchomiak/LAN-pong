# * ------ 
# * File: /client.py
# * File Created: Friday, 22nd November 2019 6:07:29 pm
# * Author: Alex Chomiak 
# * 
# * Last Modified: Saturday, 23rd November 2019 11:49:15 pm
# * Modified By: Alex Chomiak 
# * 
# * Author Github: https://github.com/alexchomiak
# * ------ 

import sys
import socket
import threading
import time
port = sys.argv[1]
ip = sys.argv[2] if (len(sys.argv) > 2) else '127.0.0.1'

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
  if playerX == 0: increment = -increment
  if playerX > 500: increment = -increment
  print("Player at X:",playerX)
  send_increment(increment)
  time.sleep(.05)