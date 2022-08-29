def digit(n):
    if n==0:
        return 1
    c=0
    if n<0:
        n=-1*n
    while(n):
        r=n%10
        n//=10
        c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append(digit(l[i]))
for i in range(n):
    if digit(l[i])==max(a):
        print(l[i],end=' ')