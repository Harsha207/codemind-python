n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
f=0
for i in l:
    if i not in range(a,b+1):
        s.append(i)
        f=1
if f==0:
    print('-1')
else:
    print(min(s))