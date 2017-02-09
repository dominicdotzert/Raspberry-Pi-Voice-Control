import os
from random import randint
from subprocess import Popen

def play():
    folder_path = "/home/pi/Videos/Bob Ross/"
    files = os.listdir(folder_path)
    rand_vid = folder_path + files[randint(0, len(files)-1)]
    omxp = Popen(['omxplayer', '-b', rand_vid])

if __name__ == "__main__":
    play()
