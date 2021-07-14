import sys
from math import cos, pi, pow, sqrt

def to_f(input: str) -> float:
    return float(input.replace(',', '.'))

def to_rad(deg: float) -> float:
    return deg * pi / 180

def distance(lat_a, lon_a, lat_b, lon_b) -> float:
    x = (lon_b - lon_a) * cos((lat_a + lat_b)/2)
    y = lat_b - lat_a
    return sqrt(pow(x, 2) + pow(y, 2)) * 6371

lon = to_rad(to_f(input()))
lat = to_rad(to_f(input()))
n = int(input())
min_d = None
address = None
for i in range(n):
    defib = input()
    defib_elts = defib.split(';')
    lat_d = to_rad(to_f(defib_elts.pop()))
    lon_d = to_rad(to_f(defib_elts.pop()))
    dist = distance(lat, lon, lat_d, lon_d)
    if (min_d is None) or (dist < min_d):
        min_d = dist
        address = defib_elts[1]

print(address)
