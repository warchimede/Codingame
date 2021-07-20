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

def decompose_in_base(num: int, base: int) -> [int]:
    if num == 0: return [0]
    result = []
    n = num
    while n!=0:
        result.append(n%base)
        n = n//base
    result.reverse()
    return result

def int_in_base_to_mayan(num_in_base: [int], all_mayans: [[str]]) -> [[str]]:
    return list(map(lambda i: all_mayans[i],num_in_base))


def print_answer(result: [[str]]):
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j])
    
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
result_in_base = decompose_in_base(result, base)
answer = int_in_base_to_mayan(result_in_base, mayans)

# Print result
print_answer(answer)
