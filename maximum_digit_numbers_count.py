def dig(n):
    if n==0:
        return 1
    c=0
    if n<0:
        n=-1*n
    while n!=0:
        n//=10
        c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(n):
    s.append(dig(l[i]))
for i in range(n):
    if dig(l[i])==max(s):
        print(l[i],end=' ')