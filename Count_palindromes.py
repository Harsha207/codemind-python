def rev(n):
    rev=0
    temp=n
    while n>0:
        r=n%10
        rev=rev*10+r
        n//=10
    if temp==rev:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if rev(i):
        c+=1
print(c)