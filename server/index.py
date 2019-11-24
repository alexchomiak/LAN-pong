# * ------ 
# * File: /index.py
# * File Created: Sunday, 27th October 2019 4:50:54 pm
# * Author: Alex Chomiak 
# * 
# * Last Modified: Saturday, 23rd November 2019 5:31:03 pm
# * Modified By: Alex Chomiak 
# * 
# * Author Github: https://github.com/alexchomiak
# * ------ 

import threading
import time
from pong import player1, player2, start
from controller import Controller
from scoreboard import Scoreboard

# * Initialize and Start Scoreboard Server
scoreboard = Scoreboard(10000)
scoreboard.start()

# * Initialize Player Controllers
controller1 = Controller(player1,10001)
controller2 = Controller(player2,10002)

# * Start Controllers
controller1.start()
controller2.start()

# * Start PyGame Instance of Pong
start()

