import sys
import math

result = 10000000
powers = []
n = int(input())
for i in range(n):
    powers.append(int(input()))

powers.sort()

for i in range(1, len(powers)):
    diff = powers[i] - powers[i - 1]
    if diff < result:
        result = diff

print(result)