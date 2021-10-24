#********************************
#   Created by Killian Meunier  *
#           24/10/2021          *
#********************************

import mouse
import keyboard
import time

# Key to quit the script
escape_key = "esc"
# Key to start clicking
start_key = "page up"
# Key to stop clicking without exiting the script
stop_key = "page down"
# Delay between each click in seconds
delay = 0.001
# Boolean to know if we're clicking or not 
play = False

while not keyboard.is_pressed(escape_key):

    if keyboard.is_pressed(start_key):
        play = True

    while play and (not keyboard.is_pressed(escape_key)):
        mouse.click()
        time.sleep(delay)

        if keyboard.is_pressed(stop_key):
            play = False