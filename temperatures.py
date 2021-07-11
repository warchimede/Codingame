import sys
import math

n = int(input())  # the number of temperatures to analyse
result = 0
temperature: int = None
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if (temperature is None or abs(t) < abs(temperature) or t == abs(temperature)):
        temperature = t
        result = i

print(str(result))
