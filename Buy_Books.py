n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s1=sum(a)
s2=sum(b)
if s1-s2>0:
    print('0')
else:
    print(s2-s1)