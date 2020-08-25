# cook your dish here
t = int(input())
for i in range(t):
    string = input()
    n = len(string)
    if n % 2 == 0:
        mid = n//2
        first = list(string[:mid])
        second = list(string[mid:])
    else:
        mid = n// 2
        first = list(string[:mid])
        second = list(string[mid+1:])
    first.sort()
    second.sort()
    if first == second:
        print('YES')
    else:
        print('NO')
        
