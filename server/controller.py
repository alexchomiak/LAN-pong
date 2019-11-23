# * ------ 
# * File: /controller.py
# * File Created: Friday, 22nd November 2019 5:51:22 pm
# * Author: Alex Chomiak 
# * 
# * Last Modified: Saturday, 23rd November 2019 5:31:39 pm
# * Modified By: Alex Chomiak 
# * 
# * Author Github: https://github.com/alexchomiak
# * ------ 

import socket
import threading


# * Controller Class (Controller Server for each player)
class Controller(threading.Thread):
  def __init__(self, player, port):
    # * Initialize Class
    super(Controller,self).__init__()

    # * Set Controllers Player
    self.player = player
    
    # * Set port of controller
    self.port = port

    # * Intialize Socket
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # * Bind socket to port
    self.sock.bind(('', port))

    # * Start listening for connections
    self.sock.listen(1)



  def run(self):
    # * Print prompt waiting for player to connect
    print("Waiting for", self.player.name , "to connect...")

    # * Wait for connection...
    conn, addr = self.sock.accept()
    
    # * Print connection Established
    print("Connected", addr)

    # * Update that player is connect
    self.player.connected = True

    # * Connection Loop
    while(True):
      # * Read incoming packets from client
      data = conn.recv(1024)

      # ! If data invalid, exit loop
      if not data:
        break

      # * Set player X coordinate based off increment
      self.player.setX(self.player.x + int(data))
   
      # * Send back updated X coordinate to client      
      conn.sendall(str(self.player.x).encode())

      

    