n=int(input())
l=list(map(int,input().split()))
s=[]
f=0
for i in l:
    if l.count(i)==i:
        s.append(i)
        f=1
if(f==0):
    print('-1')
else:
    a=set(s)
    b=sum(a)
    c=len(a)
    d=b/c
    print("%.2f"%d)