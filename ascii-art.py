import sys
import string

l = int(input())
h = int(input())
t = input().lower()
rows = [input() for _ in range(h)]
answer = ["" for _ in range(h)]

for letter in t:
  index = string.ascii_lowercase.find(letter)
  if index == -1: index = len(string.ascii_lowercase)
  index *= l
  for i in range(h):
    answer[i] = answer[i] + rows[i][index:index+l]

for i in range(h):
  print(answer[i])