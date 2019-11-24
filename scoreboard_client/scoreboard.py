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
import Adafruit_CharLCD as LCD

# * Variables that store each of the LCD pins
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 4
lcd_columns = 16
lcd_rows = 2

# * Sets up the LCD with the pins connects to the Raspberry Pi
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                            lcd_columns, lcd_rows, lcd_backlight)

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

oldScore = ""
while(connected):
  # * Score will be populated by Listener
  get_score() # * Sends request for score from server

  # * Checks if the new string sent from the server is different
  if oldScore != score:
    # * Gets the index of where the '-' is in the string sent by the server
    index = score.find('-')
    # * Makes new variables of the separate scores
    p1Score, p2Score = score[:index], score[index+1:]
    print("Player 1: " + p1Score)
    print("Player 2: " + p2Score)

    # * Clears the screen
    lcd.clear()
    # * Prints Player 1's score to the screen
    lcd.set_cursor(0,0)
    lcd.message("Player 1: " + p1Score)
    # * Prints Player 1's score to the screen
    lcd.set_cursor(0,1)
    lcd.message("Player 2: " + p2Score)
    oldScore = score

  time.sleep(.05)
