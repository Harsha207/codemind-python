n1=0
n2=1
n=int(input())
print('0 1',end=' ')
for i in range(2,n,1):
    n=n1+n2
    print(n,end=' ')
    n1=n2
    n2=n