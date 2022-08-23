n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if l.count(i)!=1:
        if i not in s:
            s.append(i)
print(*s)