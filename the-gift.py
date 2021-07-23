import sys
import math

def split(price: int, budgets: [int]):
  participations = []
  left_to_pay = price
  n = len(budgets)
  for i in range(n):
    avg = int(math.floor(left_to_pay/(n - i)))
    part = min(budgets[i], avg)
    participations.append(part)
    left_to_pay -= part

  for i in range(n):
    print(participations[i])

n = int(input())
c = int(input())
budgets = []
for i in range(n):
  budgets.append(int(input()))

if sum(budgets) < c:
  print("IMPOSSIBLE")
else:
  budgets.sort()
  split(c, budgets)