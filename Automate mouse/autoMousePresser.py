#********************************
#   Created by Killian Meunier  *
#           24/10/2021          *
#********************************

import mouse
import keyboard

# Key to quit the script
escape_key = "esc"
# Key to start pressing the mouse
start_key = "page up"
# Key to stop pressing the mouse without exiting the script
stop_key = "page down"

while not keyboard.is_pressed(escape_key):
    if keyboard.is_pressed(start_key):
        mouse.press()
    if keyboard.is_pressed(stop_key):
        mouse.release()
