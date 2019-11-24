# * ------
# * File: /scoreboard.py
# * File Created: Saturday, 23rd November 2019 5:26:41 pm
# * Author: Alex Chomiak
# *
# * Last Modified: Sunday, 24th November 2019 2:20:04 am
# * Modified By: Alex Chomiak
# *
# * Author Github: https://github.com/alexchomiak
# * ------

import socket
import threading
from pong import player1,player2

# * Scoreboard Class (Scoreboard Server to send out scoreboard data)
class Scoreboard(threading.Thread):
  def __init__(self, port):
    # * Initialize Class
    super(Scoreboard,self).__init__()

    # * Set port of Scoreboard
    self.port = port

    # * Intialize Socket
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # * Bind socket to port
    self.sock.bind(('', port))

    # * Start listening for connection
    self.sock.listen(1)



  def run(self):
    while(True):
      # * Print prompt waiting for player to connect
      print("Waiting for scoreboard client to connect...")

      # * Wait for connection...
      conn, addr = self.sock.accept()

      # * Print connection Established
      print("Connected Scoreboard Client", addr)
      connected = True
      # * Connection Loop
      while(connected):
        try:
            # * Read incoming packets from client
            data = conn.recv(1024)

            # ! If data invalid, exit loop
            if not data:
              connected = False

            # * Construct score string
            score_str = f"{player1.score}-{player2.score}"

            # * Send back score string
            conn.sendall(score_str.encode())
        except:
            print("Scoreboard Connection lost!!!")
            connected = False
    conn.close()


