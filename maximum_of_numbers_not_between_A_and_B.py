n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
f=0
s=[]
for i in l:
    if i not in range(a,b+1):
        s.append(i)
        f=1
if(f==1):
    print(max(s))
else:
    print('-1')