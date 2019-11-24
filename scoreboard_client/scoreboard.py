# * ------ 
# * File: /scoreboard.py
# * File Created: Sunday, 24th November 2019 1:01:32 am
# * Author: Alex Chomiak 
# * 
# * Last Modified: Sunday, 24th November 2019 4:30:39 am
# * Modified By: Alex Chomiak 
# * 
# * Author Github: https://github.com/alexchomiak
# * ------ 


import sys
import socket
import threading
import time
import Adafruit_CharLCD as LCD
connected = False

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

# * Score String
score = "0-0"

scoreboard_socket = {}

class Listener(threading.Thread):
  def __init__(self):
    super(Listener,self).__init__()
  def run(self):
    global score
    while(True):
      try:
        # * Get Data
        data = scoreboard_socket.recv(1024)

        # * If Invalid data, break listener loop
        if not data:
          break

        # * Decode data string
        score = data.decode('utf-8')
      except:
        print("Closing Connection")
        scoreboard_socket.close()
        connected = False
        break



def get_score(): # * Sends request to get score
  global connected
  if not connected: score = "0-0"
  else: 
    try:
      scoreboard_socket.send(("x").encode()) # * Send arbitrary packet
    except:
      print("Error retrieving score")
      connected = False
oldScore = ""

while(True):
  print("Connecting client...")
  print("Port:",port)
  print("IP:", ip)
  try:
    scoreboard_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scoreboard_socket.connect((ip,int(port)))
  except:
    print("Connection Cannot Be Established... Trying Again...")
    time.sleep(5)
    
  # * State variables
  connected = True
  
  print("Connected to pong server...")
  
  # * Initialize and start listener
  listener = Listener()
  listener.start()

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
