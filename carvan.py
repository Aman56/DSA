# cook your dish here
t= int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    count = 0
    speed = []
    speed.append(a[0])
    for i in range(1,n):
        speed.append(min(a[i], speed[i-1]))
    for j in range(n):
        if speed[j] == a[j]:
            count += 1
    print(count)
