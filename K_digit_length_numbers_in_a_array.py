def dig(n):
    if n==0:
        return 1
    elif n<0:
        n=n*-1
    c=0
    while n!=0:
        n//=10
        c+=1
    return c
n,k=map(int,input().split())
l=list(map(int,input().split()))
s=[]
f=0
for i in range(n):
    s.append(dig(l[i]))
for i in range(n):
    if dig(l[i])==k:
        f+=1
print(f)