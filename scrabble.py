import sys
import math

def possible_words(letters: str, words: [str]) -> [str]:
  possible_words = []
  for word in words:
    if len(word) > 7: continue # word is too long
    is_possible = True
    lets = letters
    for letter in word:
      if letter not in lets:
        is_possible = False
        break
      lets = lets.replace(letter, "", 1) # to avoid using same letter several times
    if is_possible: possible_words.append(word)
  return possible_words

def score_for_letter(letter: str) -> int:
  if len(letter) != 1: return 0
  if letter in "eaionrtlsu": return 1
  if letter in "dg": return 2
  if letter in "bcmp": return 3
  if letter in "fhvwy": return 4
  if letter == "k": return 5
  if letter in "jx": return 8
  if letter in "qz": return 10

def score_for_word(word: str) -> int:
  score = 0
  for letter in word:
    score += score_for_letter(letter)
  return score

n = int(input())
words = []
for i in range(n): words.append(input())
letters = input()
words = possible_words(letters, words)
best_word = ""
for word in words:
  if score_for_word(best_word) < score_for_word(word): best_word = word
print(best_word)
