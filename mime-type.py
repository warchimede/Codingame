import sys
import math

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mime_dict = {}
unknown = "UNKNOWN"

for i in range(n):
  # ext: file extension
  # mt: MIME type.
  ext, mt = input().split()
  mime_dict[ext.lower()] = mt

for i in range(q):
  fname = input().lower()  # One file name per line.
  if fname.find(".") == -1:
    print(unknown)
    continue
    
  ext = fname.split(".").pop()
  if ext in mime_dict.keys():
    print(mime_dict[ext])
  else:
    print(unknown)