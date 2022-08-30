s=input()
v='aeiouAEIOU'
l=[]
for i in s:
    if i in v:
        l.append(i)
if len(l)==0:
    print('-1')
else:
    f=[]
    for i in l:
        if i not in f:
            f.append(i)
print(*f)