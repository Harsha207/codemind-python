n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=[]
f=0
for i in l:
    if l.count(i)==k and i not in s:
        s.append(i)
        f=1
if(f==1):
    print(*s)
else:
    print('-1')