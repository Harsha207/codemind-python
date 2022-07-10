n=int(input())
c=0
for i in range(n):
    s=int(input())
    l=list(map(int,input().split()))
    for j in range(1,s):
        if l[j-1]>l[j]:
            c+=1
    if c==0:
        print(c)
    else:
        maxi=max(l)
        mini=min(l)
        print(maxi-mini)