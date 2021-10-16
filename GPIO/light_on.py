import RPi.GPIO as G
import time

channel = 1
G.setmode(G.BOARD)
G.setup(channel,G.OUT)

while(True):
    G.output(channel,1)