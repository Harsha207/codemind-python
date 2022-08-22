n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
f=0
s=[]
for i in l:
    if i in range(a,b+1):
        s.append(i)
        f=1
if f==0:
    print('-1')
else:
    print(max(s))