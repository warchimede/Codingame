import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# tx: Thor's X position
# ty: Thor's Y position
light_x, light_y, tx, ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    ns = ""
    if ty < light_y:
        ns = "S"
        ty += 1
    elif ty > light_y:
        ns = "N"
        ty -= 1
    
    ew = ""
    if tx < light_x:
        ew = "E"
        tx += 1
    elif tx > light_x:
        ew = "W"
        tx -= 1

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(f"{ns}{ew}")
