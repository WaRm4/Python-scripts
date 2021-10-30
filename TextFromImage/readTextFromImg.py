#********************************
#   Created by Killian Meunier  *
#           30/10/2021          *
#********************************

from pytesseract import *   
from os import listdir, mkdir
from os.path import exists, abspath
import re

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'                   

# Source directory
srcDir = "./src/"
# Output directory
outDir = "./out"
# Regular expression to select files
regex = "(.*bmp)|(.*png)|(.*jpg)"
# every file in srcDir that respect the regular expression
files = [f for f in listdir(srcDir) if re.search(regex, f) != None]

print(files)
if not exists(outDir):
    mkdir(outDir)

print("Starting conversion...\n(of all image files located in " + abspath(srcDir) + "\n")

if len(files) > 0:
    for f in files:
        print("Processing " + f + "...")
        result = pytesseract.image_to_string(srcDir + f)
        outFile = open(outDir + "/" + f.rsplit('.')[0] + ".txt", "w")
        outFile.write(result)
        outFile.close()

    print("Done !")

else:
    print("There are no image files in " + abspath(srcDir))

input("Press any key to terminate the program")