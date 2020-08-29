# cook your dish here
from itertools import cycle, chain
t = int(input())
for _ in range(t):
    g = int(input())
    for k in range(g):
        i,n,q = map(int,input().split())
        if n % 2 == 0:
            print(n//2)
        else:
            if q==i:
                print((n-1)//2)
            else:
                print((n+1)//2)
            
