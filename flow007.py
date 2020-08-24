# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    reverse = 0
    while(n>0):
        remainder = n%10
        reverse = reverse*10 + remainder
        n = n//10
    print(reverse)
