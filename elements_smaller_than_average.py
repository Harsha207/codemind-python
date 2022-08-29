n=int(input())
l=list(map(int,input().split()))
c=0
s=sum(l)
a=s/n
for i in range(n):
    if l[i]<=a:
        c+=1
print(c)