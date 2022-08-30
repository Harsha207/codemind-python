def dig(n):
    c=0
    while n!=0:
        n//=10
        c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(n):
    s.append(dig(l[i]))
a=max(s)
print(s.count(a))