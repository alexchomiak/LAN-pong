# * ------ 
# * File: /index.py
# * File Created: Sunday, 27th October 2019 4:50:54 pm
# * Author: Alex Chomiak 
# * 
# * Last Modified: Friday, 22nd November 2019 8:33:37 pm
# * Modified By: Alex Chomiak 
# * 
# * Author Github: https://github.com/alexchomiak
# * ------ 
import threading
import time
from pong import player1, player2, start
from controller import Controller

# * Initialize Player Controllers
controller1 = Controller(player1,10001)
controller1.start()

controller2 = Controller(player2,10002)
controller2.start()

# * Start PyGame Instance of Pong
start()

