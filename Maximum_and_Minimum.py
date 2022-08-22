n=int(input())
l=list(map(int,input().split()))
f=0
s=[]
for i in l:
    if l.count(i)==i:
        s.append(i)
        f=1
if(f==1):
    print(min(s),max(s))
else:
    print('-1')