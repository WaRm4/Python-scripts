#********************************
#   Created by Killian Meunier  *
#           09/01/2022          *
#********************************

import tkinter as tk
from tkinter import filedialog
import os
import time

# Tkinter window
root = tk.Tk()
root.withdraw()

# Open a file dialog to chose files
files = filedialog.askopenfilenames()

for file in files:
    print("Working on", file, "...")

    # Get extension and folder of each files
    extension = os.path.splitext(file)[1]
    folder = os.path.dirname(file)

    # Get the creation date of the file as a "human understandable time"
    float_time = os.path.getctime(str(file))
    human_time = time.strftime('%Y-%m-%d_%Hh-%Mm-%Ss', time.localtime(float_time))

    new_name = "/" + human_time 
    rnd = ""
    i = 0
    # While the name is already taken chose a new one (increment variable)
    while os.path.isfile(folder + new_name + rnd + extension):
        i = i+1
        rnd = "(" + str(i) + ")"

    # Rename the file
    os.rename(file, folder + new_name + rnd + extension)

print("Done !")
