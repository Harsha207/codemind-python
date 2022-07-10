n=int(input())
for k in range(n):
    x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[]
    for i in range(x):
        l.append(a[i])
    for j in range(y):
        l.append(b[j])
    print(*sorted(l))