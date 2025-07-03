import os
import time
import story
from story.Prologue import prologue, startGame
from story.ORVI import introScene

os.system("clear")
time.sleep(1)
prologue()
start = startGame()
if start == True:
    introScene()
else:
    print("Aw okay, you can always come back if you change your mind.")