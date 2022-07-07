s=list(map(str,input().split()))
c=0
h=len(s)
for i in s:
    c+=1
    if c==h:
        print(i[:3:3])
    