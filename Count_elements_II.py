a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
c=0
for i in list(set(n)):
    if m.count(i)==0:
        c+=1
for j in list(set(m)):
    if n.count(j)==0:
        c+=1
print(c)