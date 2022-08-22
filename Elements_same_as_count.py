n=int(input())
l=list(map(int,input().split()))
s=[]
f=0
for i in l:
    if l.count(i)==i and i not in s:
        s.append(i)
        f=1
if(f==1):
    print(*s)
else:
    print('-1')