n=int(input())
l=list(map(int,input().split()))
s=sum(l)
a=s//n
f=0
for i in range(n):
    if l[i]==a:
        print('True')
        break
else:
    print('False')