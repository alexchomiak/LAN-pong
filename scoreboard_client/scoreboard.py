# * ------ 
# * File: /scoreboard.py
# * File Created: Saturday, 23rd November 2019 5:29:52 pm
# * Author: Alex Chomiak 
# * 
# * Last Modified: Saturday, 23rd November 2019 5:47:11 pm
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

scoreboard_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scoreboard_socket.connect((ip,int(port)))

# * State variables
connected = True
score = "0-0"

class Listener(threading.Thread):
  def __init__(self):
    super(Listener,self).__init__()
  def run(self):
    global score
    while(True):
      # * Get Data 
      data = scoreboard_socket.recv(1024)
      
      # * If Invalid data, break listener loop
      if not data: 
        break
        
      # * Decode data string
      score = data.decode('utf-8')
      
 
    connected = False

# * Initialize and start listener
listener = Listener()
listener.start()

def get_score(): # * Sends request to get score
  if not connected: score = "0-0"
  else: scoreboard_socket.send(("x").encode()) # * Send arbitrary packet

# ** Dummy Code **
increment = 10
while(connected):
  # * Score will be populated by Listener
  get_score() # * Sends request for score from server

  # * Print Score
  print(score)

  # * Implement GPIO code for display here *******
  time.sleep(.05)