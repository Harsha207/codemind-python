def digit(n):
    c=0
    if n==0:
        return 1
    elif n<0:
        n=n*-1
    while(n):
        n//=10
        c+=1
    return c
x,y=map(int,input().split())
l=list(map(int,input().split()))
a=[]
for i in range(x):
    a.append(digit(l[i]))
print(a.count(y))