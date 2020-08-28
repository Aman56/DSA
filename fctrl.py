# cook your dish here
from math import floor
t = int(input())
for _ in range(t):
    n = int(input())
    r,z = 1,0
    remain = 1
    while(remain != 0):
        remain = floor(n/(5**r))
        z += remain
        r += 1
    print(z)
