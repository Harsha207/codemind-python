n,m=map(int,input().split())
c=0
for i in range(n):
    a=list(map(int,input().split()))
    b=a.copy()
    b.sort()
    q=b[::-1]
    if a==q or a==b:
        c+=1
print(c)