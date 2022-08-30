n=input()
s=n.lower()
v='aeiou'
l=[]
for i in s:
    if i in v:
        l.append(i)
k=[]
for i in l:
    if i not in k:
        k.append(i)
if len(k)==5:
    print("0")
else:
    a=[]
    for i in v:
        if i not in l:
            a.append(i)
print(*a)