def digit(n):
    if n==0:
        return 1
    c=0
    while n:
        n//=10
        c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append(digit(l[i]))
x=min(a)
print(a.count(x))