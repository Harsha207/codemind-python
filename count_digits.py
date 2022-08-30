def dig(n):
    if n==0:
        return 1
    elif n<0:
        n=n*-1
    c=0
    while n:
        n//=10
        c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(n):
    s.append(dig(l[i]))
print(*s)