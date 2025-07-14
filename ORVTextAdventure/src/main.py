import os
import time
from helper import Text as text
import story
from story.Prologue import prologue, startGame
from story.ORVI import introScene

text.clearScreen()
time.sleep(1)
prologue()
start = startGame()
if start == True:
    introScene()
else:
    print("Aw okay, you can always come back if you change your mind.")