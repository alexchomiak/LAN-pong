# * ------ 
# * File: /controller.py
# * File Created: Friday, 22nd November 2019 5:51:22 pm
# * Author: Alex Chomiak 
# * 
# * Last Modified: Friday, 22nd November 2019 6:54:07 pm
# * Modified By: Alex Chomiak 
# * 
# * Author Github: https://github.com/alexchomiak
# * ------ 

import socket
import threading
class Controller(threading.Thread):
  def __init__(self, player, port):
    super(Controller,self).__init__()
    self.port = port
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.bind(('', port))
    self.sock.listen(2)

    self.player = player
    

  def run(self):
    print("Waiting for", self.player.name , "to connect...")
    self.player.setX(50)
    conn, addr = self.sock.accept()
    
    print(conn,"CONNECTED")

    while(True):
      data = conn.recv(1024)
      print("Moving", self.player.name, int(data),"units.")
      self.player.setX(self.player.x + int(data))
      if not data:
        break
      conn.sendall(str(self.player.x).encode())

      

    