#********************************
#   Created by Killian Meunier  *
#           30/10/2021          *
#********************************

from pytesseract import *   
from os import listdir, mkdir
from os.path import exists, abspath
import re
import threading

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'                   

# Source directory
srcDir = "./src/"
# Output directory
outDir = "./out"
# Regular expression to select files
regex = "(.*bmp)|(.*png)|(.*jpg)"
# Every file in srcDir that respect the regular expression
files = [f for f in listdir(srcDir) if re.search(regex, f) != None]

if not exists(outDir):
    mkdir(outDir)

# Converting the file "fi" and writing the result
def job(fi):
    print("Processing " + fi + "...\n")
    result = pytesseract.image_to_string(srcDir + fi)
    outFile = open(outDir + "/" + fi.rsplit('.')[0] + ".txt", "w")
    outFile.write(result)
    outFile.close()

print("Starting conversion...\n(of all image files located in " + abspath(srcDir) + "\n")

threads = []
if len(files) > 0:
    for f in files:
        t = threading.Thread(target=job, args=(f,))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()
        
    print("Done !")

else:
    print("There are no image files in " + abspath(srcDir))

input("Press any key to terminate the program")