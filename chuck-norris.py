import sys
import math

def clean(input: str) -> str:
  output = input.replace("0b", "")
  if len(output) < 7:
    output = "0" + output
  return output

bin_message = "".join(map(clean, map(bin, bytearray(input(), "ascii"))))
answer = ""
current = None
for char in bin_message:
  if current is None:
    current = char
    if current == "0":
      answer += "00 0"
    else:
      answer += "0 0"
      continue

  if char == current:
    answer += "0"
  else:
    current = char
    if current == "0":
      answer += " 00 0"
    else:
      answer += " 0 0"

print(answer)
