t=int(input())
a=list(map(int,input().split()))
for i in range(t):
    if a[i]%2!=0:
        e=i
print(e)