def digit(n):
    c=0
    while n:
        r=n%10
        n//=10
        c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append(digit(l[i]))
x=max(a)
print(a.count(x))