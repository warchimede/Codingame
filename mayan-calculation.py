import sys
import functools

base = 20
l, h = [int(i) for i in input().split()]
mayans = []

def get_mayan_lines(height: int, length: int) -> [[str]]:
    lines = []
    for i in range(h):
        line = input()
        numeral = [line[i*length:(i+1)*length] for i in range(base)]
        lines.append(numeral)
    return lines

def to_mayans(lines: [[str]], height: int) -> [[str]]:
    mays = []
    for i in range(base):
        comp = []
        for j in range(height):
            comp.append(lines[j][i])
        mays.append(comp)
    return mays

def get_mayan(num_lines: int, height: int) -> [[str]]:
    mayan = [[] for i in range(int(num_lines/height))]
    for i in range(num_lines):
        mayan[int(i/height)].append(input())
    return mayan

def mayan_to_int(mayan: [[str]], all_mayans: [[str]]) -> int:
    int_list = list(map(lambda m: all_mayans.index(m), mayan))
    return functools.reduce(lambda a,b: a*base + b, int_list)

def compute(num1: int, num2: int, op: str) -> int:
    if op=="*": return num1*num2
    if op=="/": return int(num1/num2)
    if op=="+": return num1+num2
    if op=="-": return num1-num2
    
# Get the array of mayan representations
mayans = to_mayans(lines=get_mayan_lines(h,l), height=h)

# Interpret numeral entries
s1 = int(input())
num1 = mayan_to_int(get_mayan(num_lines=s1, height=h), mayans)

s2 = int(input())
num2 = mayan_to_int(get_mayan(num_lines=s2, height=h), mayans)

# Interpret operation
operation = input()

# Compute
result = compute(num1, num2, operation)

# Translate to mayan representation


# Print result
print(mayans, file=sys.stderr, flush=True)
print(" ", file=sys.stderr, flush=True)
print(num1, file=sys.stderr, flush=True)
print(" ", file=sys.stderr, flush=True)
print(num2, file=sys.stderr, flush=True)
print(result, file=sys.stderr, flush=True)
