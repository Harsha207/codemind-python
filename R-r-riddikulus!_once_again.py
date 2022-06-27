a,b=map(int,input().split())
c=list(map(int,input().split()))
x=(c[b:]+c[:b])
print(*x)