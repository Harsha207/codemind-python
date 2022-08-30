s=input()
v='aeiou'
u='AEIOU'
l=[]
a=[]
for i in s:
    if i in v:
        l.append(i)
k=[]
for i in l:
    if i not in k:
        k.append(i)
for j in s:
    if j in u:
        a.append(j)
b=[]
for j in a:
    if j not in b:
        b.append(j)
m=len(k)
n=len(b)
if m==5:
    print('True')
elif n==5:
    print('True')
else:
    print('False')