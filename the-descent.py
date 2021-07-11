import sys
import math

# game loop
while True:
    index = 0
    height = 0

    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if (mountain_h > height):
            height = mountain_h
            index = i
    
    print(index) # the index of the mountain to fire on.